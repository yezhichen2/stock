# coding=utf-8


class PBB(object):

    @classmethod
    def count_probability(cls, myiter):
        """计算概率"""
        my_map = {}

        all_count = 0.0
        for ss in myiter:
            if ss not in my_map:
                my_map[ss] = [ss, 0, 0]

            my_map.get(ss)[2] += 1
            all_count += 1

        for value in my_map.values():
            value[1] = value[2] / all_count

        values = list(my_map.values())

        values.sort(key=lambda item: 1-item[1])

        return values

    @classmethod
    def count_probability2(cls, info_dict):
        """
        info_dict => {'DC': 1, 'DD': 1, 'EB': 1}
        """
        letters = ""
        _info_dicts = [info_dict] if isinstance(info_dict, dict) else info_dict

        for _info_dict in _info_dicts:
            for key, count in _info_dict.items():
                letters += key * count

        return cls.count_probability(letters)

    @classmethod
    def weight_probability(cls, info_dicts, weights=[0.6, 0.4]):
        """
        将信息计算概率，把概率按权重分配，再求和
        """

        weights_index = 0

        my_map = {}

        for _info_dict in info_dicts:
            letters = ""
            for key, count in _info_dict.items():
                letters += key * count

            cps = cls.count_probability(letters)

            for cp in cps:
                kw, p, count = cp[0], cp[1], cp[2]
                if kw not in my_map: my_map[kw] = [kw, 0, 0]

                my_map[kw][1] += p * weights[weights_index]
                my_map[kw][2] += count

            weights_index += 1

        values = list(my_map.values())
        values.sort(key=lambda item: 1 - item[1])

        return values

    @classmethod
    def forecast(cls, last_states, xy_pdatas):
        weights = [0.4, 0.4, 0.2]

        x3pattern = last_states[-3:]
        x5pattern = last_states[-5:]
        x8pattern = last_states[-8:]

        info_dicts = [xy_pdatas.get(x3pattern, {}), xy_pdatas.get(x5pattern, {}), xy_pdatas.get(x8pattern, {})]

        print(info_dicts)

        wps = cls.weight_probability(info_dicts, weights=weights)

        return wps[0:2]


