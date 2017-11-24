# coding=utf-8
import pandas as pd


class ZB(object):

    @classmethod
    def kdj(cls, stock_data):
        """
        RSV:=(CLOSE-LLV(LOW,N))/(HHV(HIGH,N)-LLV(LOW,N))*100;
        K:SMA(RSV,M1,1);
        D:SMA(K,M2,1);
        J:3*K-2*D;

        :param stock_data:
        :return:
        """
        df = stock_data.loc[:, ["close", "low", "high"]]
        min_low = df['low'].rolling(window=9, min_periods=1).min()
        max_high = df['high'].rolling(window=9, min_periods=1).max()

        rsv = (df["close"] - min_low) / (max_high - min_low) * 100

        df["kdj_k"] = rsv.ewm(com=2).mean()  # 加权移动平均
        df["kdj_d"] = df["kdj_k"].ewm(com=2).mean()
        df["kdj_j"] = 3 * df["kdj_k"] - 2 * df["kdj_d"]

        return df.loc[:, ["kdj_k", "kdj_d", "kdj_j"]]


    @classmethod
    def _max(self, s1, s2):
        df_temp = pd.DataFrame({"a": s1, "b": s2})
        df_temp['max'] = 0

        df_temp.ix[df_temp['a'] >= df_temp['b'], 'max'] = df_temp['a']
        df_temp.ix[df_temp['a'] < df_temp['b'], 'max'] = df_temp['b']

        return df_temp['max']

    @classmethod
    def mdi(cls, stock_data, n=14, m=6):
        """
        MTR:=SUM(MAX(MAX(HIGH-LOW,ABS(HIGH-REF(CLOSE,1))),ABS(REF(CLOSE,1)-LOW)),N);
        HD :=HIGH-REF(HIGH,1);
        LD :=REF(LOW,1)-LOW;
        DMP:=SUM(IF(HD>0&&HD>LD,HD,0),N);
        DMM:=SUM(IF(LD>0&&LD>HD,LD,0),N);
        PDI: DMP*100/MTR;
        MDI: DMM*100/MTR;
        ADX: MA(ABS(MDI-PDI)/(MDI+PDI)*100,M);
        ADXR:(ADX+REF(ADX,M))/2;

        :param stock_data:
        :param n:
        :param m:
        :return:
        """

        df = stock_data.loc[:, ["close", "low", "high", "open"]]

        h_l = df['high'] - df['low']
        h_ref_c = abs(df['high'] - df['close'].shift(1))
        ref_c_l = abs(df["close"].shift(1) - df['low'])

        tt1 = cls._max(cls._max(h_l, h_ref_c), ref_c_l)

        MTR = tt1.rolling(center=False, min_periods=1, window=n).sum()
        HD = df["high"] - df["high"].shift(1)
        LD = df["low"].shift(1) - df["low"]

        df_tmp = pd.DataFrame({"MTR": MTR, "HD": HD, "LD": LD})

        df_tmp["DMP"] = 0
        df_tmp.ix[(df_tmp['HD'] > 0) & (df_tmp['HD'] > df_tmp['LD']), "DMP"] = df_tmp['HD']
        df_tmp["DMP"] = df_tmp["DMP"].rolling(center=False, min_periods=1, window=n).sum()

        df_tmp["DMM"] = 0
        df_tmp.ix[(df_tmp['LD'] > 0) & (df_tmp['LD'] > df_tmp['HD']), "DMM"] = df_tmp['LD']
        df_tmp["DMM"] = df_tmp["DMM"].rolling(center=False, min_periods=1, window=n).sum()

        df_tmp['PDI'] = df_tmp["DMP"] * 100 / df_tmp['MTR']
        df_tmp['MDI'] = df_tmp["DMM"] * 100 / df_tmp['MTR']

        df_tmp['ADX'] = abs(df_tmp['MDI'] - df_tmp['PDI']) / (df_tmp['MDI'] + df_tmp['PDI']) * 100
        df_tmp['ADX'] = df_tmp['ADX'].rolling(center=False, min_periods=1, window=m).mean()  # 简单移动平均

        df_tmp['ADXR'] = (df_tmp['ADX'] + df_tmp['ADX'].shift(m)) / 2

        return df_tmp.loc[:, ['PDI', 'MDI', 'ADX', 'ADXR']]


    @classmethod
    def ma(cls, stock_data, m1=5, m2=10, m3=20, m4=60):
        """
        MA1:MA(CLOSE,M1);
        MA2:MA(CLOSE,M2);
        MA3:MA(CLOSE,M3);
        MA4:MA(CLOSE,M4);

        :param stock_data:
        :return:
        """
        df = stock_data.loc[:, ["close"]]
        names = []
        for m in [m1, m2, m3, m4]:
            if m<=0:continue
            name = 'MA%d' % m
            names.append(name)
            df[name] = df['close'].rolling(center=False, min_periods=1, window=m).mean()

        return df.loc[:, names]


    @classmethod
    def vol(cls, stock_data, m1=3, m2=5, m3=10):
        """
        :param stock_data:
        :return:
        """
        df = stock_data.loc[:, ["volume"]]
        df['VOL'] = df['volume']
        names = []
        for m in [m1, m2, m3]:
            if m <= 0: continue
            name = 'VMA%d' % m
            names.append(name)
            df[name] = df['volume'].rolling(center=False, min_periods=1, window=m).mean()

        return df.loc[:, names + ['VOL']]





