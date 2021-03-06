# coding=utf-8

hz300 = [["603888", "新华网"], ["603883", "老百姓"], ["603877", "太平鸟"], ["603868", "飞科电器"], ["603816", "顾家家居"],
         ["603806", "福斯特"], ["603766", "隆鑫通用"], ["603658", "安图生物"], ["603589", "口子窖"], ["603569", "长久物流"],
         ["603568", "伟明环保"], ["603556", "海兴电力"], ["603528", "多伦科技"], ["603515", "欧普照明"], ["603444", "吉比特"],
         ["603377", "东方时尚"], ["603369", "今世缘"], ["603355", "莱克电气"], ["603328", "依顿电子"], ["603228", "景旺电子"],
         ["603225", "新凤鸣"], ["603198", "迎驾贡酒"], ["603188", "亚邦股份"], ["603169", "兰石重装"], ["603077", "和邦生物"],
         ["603025", "大豪科技"], ["603019", "中科曙光"], ["603001", "奥康国际"], ["603000", "人民网"], ["601969", "海南矿业"],
         ["601928", "凤凰传媒"], ["601880", "大连港"], ["601811", "新华文轩"], ["601777", "力帆股份"], ["601717", "郑煤机"],
         ["601699", "潞安环能"], ["601689", "拓普集团"], ["601678", "滨化股份"], ["601311", "骆驼股份"], ["601233", "桐昆股份"],
         ["601231", "环旭电子"], ["601200", "上海环境"], ["601168", "西部矿业"], ["601128", "常熟银行"], ["601127", "小康股份"],
         ["601020", "华钰矿业"], ["601016", "节能风电"], ["601002", "晋亿实业"], ["601001", "大同煤业"], ["601000", "唐山港"],
         ["600996", "贵广网络"], ["600993", "马应龙"], ["600978", "宜华生活"], ["600971", "恒源煤电"], ["600970", "中材国际"],
         ["600967", "内蒙一机"], ["600939", "重庆建工"], ["600936", "广西广电"], ["600917", "重庆燃气"], ["600908", "无锡银行"],
         ["600894", "广日股份"], ["600885", "宏发股份"], ["600884", "杉杉股份"], ["600881", "亚泰集团"], ["600880", "博瑞传播"],
         ["600879", "航天电子"], ["600875", "东方电气"], ["600874", "创业环保"], ["600872", "中炬高新"], ["600869", "智慧能源"],
         ["600863", "内蒙华电"], ["600862", "中航高科"], ["600859", "王府井"], ["600848", "上海临港"], ["600839", "四川长虹"],
         ["600835", "上海机电"], ["600826", "兰生股份"], ["600823", "世茂股份"], ["600811", "东方集团"], ["600808", "马钢股份"],
         ["600801", "华新水泥"], ["600787", "中储股份"], ["600776", "东方通信"], ["600773", "西藏城投"], ["600770", "综艺股份"],
         ["600765", "中航重机"], ["600759", "洲际油气"], ["600757", "长江传媒"], ["600755", "厦门国贸"], ["600754", "锦江股份"],
         ["600751", "天海投资"], ["600750", "江中药业"], ["600748", "上实发展"], ["600743", "华远地产"], ["600737", "中粮糖业"],
         ["600729", "重庆百货"], ["600718", "东软集团"], ["600717", "天津港"], ["600694", "大商股份"], ["600687", "刚泰控股"],
         ["600673", "东阳光科"], ["600664", "哈药股份"], ["600657", "信达地产"], ["600655", "豫园股份"], ["600651", "飞乐音响"],
         ["600648", "外高桥"], ["600645", "中源协和"], ["600643", "爱建集团"], ["600642", "申能股份"], ["600640", "号百控股"],
         ["600639", "浦东金桥"], ["600635", "大众公用"], ["600633", "浙数文化"], ["600628", "新世界"], ["600623", "华谊集团"],
         ["600618", "氯碱化工"], ["600614", "鹏起科技"], ["600611", "大众交通"], ["600600", "青岛啤酒"], ["600598", "北大荒"],
         ["600597", "光明乳业"], ["600594", "益佰制药"], ["600587", "新华医疗"], ["600584", "长电科技"], ["600582", "天地科技"],
         ["600580", "卧龙电气"], ["600578", "京能电力"], ["600575", "皖江物流"], ["600572", "康恩贝"], ["600566", "济川药业"],
         ["600565", "迪马股份"], ["600563", "法拉电子"], ["600557", "康缘药业"], ["600545", "卓郎智能"], ["600536", "中国软件"],
         ["600525", "长园集团"], ["600521", "华海药业"], ["600517", "置信电气"], ["600516", "方大炭素"], ["600511", "国药股份"],
         ["600503", "华丽家族"], ["600500", "中化国际"], ["600499", "科达洁能"], ["600481", "双良节能"], ["600478", "科力远"],
         ["600466", "蓝光发展"], ["600460", "士兰微"], ["600458", "时代新材"], ["600438", "通威股份"], ["600435", "北方导航"],
         ["600428", "中远海特"], ["600426", "华鲁恒升"], ["600422", "昆药集团"], ["600418", "江淮汽车"], ["600416", "湘电股份"],
         ["600410", "华胜天成"], ["600409", "三友化工"], ["600395", "盘江股份"], ["600393", "粤泰股份"], ["600392", "盛和资源"],
         ["600388", "龙净环保"], ["600380", "健康元"], ["600366", "宁波韵升"], ["600348", "阳泉煤业"], ["600346", "恒力股份"],
         ["600338", "西藏珠峰"], ["600335", "国机汽车"], ["600329", "中新药业"], ["600325", "华发股份"], ["600317", "营口港"],
         ["600316", "洪都航空"], ["600315", "上海家化"], ["600312", "平高电气"], ["600307", "酒钢宏兴"], ["600300", "维维股份"],
         ["600298", "安琪酵母"], ["600292", "远达环保"], ["600291", "西水股份"], ["600289", "ST信通"], ["600284", "浦东建设"],
         ["600282", "南钢股份"], ["600280", "中央商场"], ["600277", "亿利洁能"], ["600270", "外运发展"], ["600267", "海正药业"],
         ["600266", "北京城建"], ["600260", "凯乐科技"], ["600259", "广晟有色"], ["600256", "广汇能源"], ["600240", "华业资本"],
         ["600216", "浙江医药"], ["600201", "生物股份"], ["600195", "中牧股份"], ["600187", "国中水务"], ["600184", "光电股份"],
         ["600183", "生益科技"], ["600179", "安通控股"], ["600176", "中国巨石"], ["600171", "上海贝岭"], ["600169", "太原重工"],
         ["600166", "福田汽车"], ["600161", "天坛生物"], ["600160", "巨化股份"], ["600158", "中体产业"], ["600155", "宝硕股份"],
         ["600151", "航天机电"], ["600143", "金发科技"], ["600141", "兴发集团"], ["600138", "中青旅"], ["600126", "杭钢股份"],
         ["600125", "铁龙物流"], ["600122", "宏图高科"], ["600120", "浙江东方"], ["600108", "亚盛集团"], ["600098", "广州发展"],
         ["600094", "大名城"], ["600086", "东方金钰"], ["600079", "人福医药"], ["600073", "上海梅林"], ["600064", "南京高科"],
         ["600062", "华润双鹤"], ["600060", "海信电器"], ["600059", "古越龙山"], ["600058", "五矿发展"], ["600056", "中国医药"],
         ["600053", "九鼎投资"], ["600039", "四川路桥"], ["600037", "歌华有线"], ["600026", "中远海能"], ["600022", "山东钢铁"],
         ["600017", "日照港"], ["600006", "东风汽车"], ["600004", "白云机场"], ["300383", "光环新网"], ["300376", "易事特"],
         ["300324", "旋极信息"], ["300297", "蓝盾股份"], ["300291", "华录百纳"], ["300287", "飞利信"], ["300274", "阳光电源"],
         ["300273", "和佳股份"], ["300266", "兴源环境"], ["300257", "开山股份"], ["300253", "卫宁健康"], ["300244", "迪安诊断"],
         ["300202", "聚龙股份"], ["300199", "翰宇药业"], ["300197", "铁汉生态"], ["300182", "捷成股份"], ["300166", "东方国信"],
         ["300159", "新研股份"], ["300147", "香雪制药"], ["300146", "汤臣倍健"], ["300134", "大富科技"], ["300133", "华策影视"],
         ["300116", "坚瑞沃能"], ["300115", "长盈精密"], ["300113", "顺网科技"], ["300088", "长信科技"], ["300058", "蓝色光标"],
         ["300055", "万邦达"], ["300043", "星辉娱乐"], ["300039", "上海凯宝"], ["300032", "金龙机电"], ["300026", "红日药业"],
         ["300010", "立思辰"], ["300002", "神州泰岳"], ["300001", "特锐德"], ["002818", "富森美"], ["002815", "崇达技术"],
         ["002807", "江阴银行"], ["002745", "木林森"], ["002709", "天赐材料"], ["002707", "众信旅游"], ["002701", "奥瑞金"],
         ["002699", "美盛文化"], ["002690", "美亚光电"], ["002681", "奋达科技"], ["002672", "东江环保"], ["002670", "国盛金控"],
         ["002665", "首航节能"], ["002663", "普邦股份"], ["002657", "中科金财"], ["002642", "荣之联"], ["002640", "跨境通"],
         ["002635", "安洁科技"], ["002603", "以岭药业"], ["002589", "瑞康医药"], ["002588", "史丹利"], ["002583", "海能达"],
         ["002573", "清新环境"], ["002551", "尚荣医疗"], ["002544", "杰赛科技"], ["002517", "恺英网络"], ["002512", "达华智能"],
         ["002506", "协鑫集成"], ["002505", "大康农业"], ["002503", "搜于特"], ["002491", "通鼎互联"], ["002489", "浙江永强"]]

zz500 = [["603888", "新华网"], ["603883", "老百姓"], ["603877", "太平鸟"], ["603868", "飞科电器"], ["603816", "顾家家居"],
         ["603806", "福斯特"], ["603766", "隆鑫通用"], ["603658", "安图生物"], ["603589", "口子窖"], ["603569", "长久物流"],
         ["603568", "伟明环保"], ["603556", "海兴电力"], ["603528", "多伦科技"], ["603515", "欧普照明"], ["603444", "吉比特"],
         ["603377", "东方时尚"], ["603369", "今世缘"], ["603355", "莱克电气"], ["603328", "依顿电子"], ["603228", "景旺电子"],
         ["603225", "新凤鸣"], ["603198", "迎驾贡酒"], ["603188", "亚邦股份"], ["603169", "兰石重装"], ["603077", "和邦生物"],
         ["603025", "大豪科技"], ["603019", "中科曙光"], ["603001", "奥康国际"], ["603000", "人民网"], ["601969", "海南矿业"],
         ["601928", "凤凰传媒"], ["601880", "大连港"], ["601811", "新华文轩"], ["601777", "力帆股份"], ["601717", "郑煤机"],
         ["601699", "潞安环能"], ["601689", "拓普集团"], ["601678", "滨化股份"], ["601311", "骆驼股份"], ["601233", "桐昆股份"],
         ["601231", "环旭电子"], ["601200", "上海环境"], ["601168", "西部矿业"], ["601128", "常熟银行"], ["601127", "小康股份"],
         ["601020", "华钰矿业"], ["601016", "节能风电"], ["601002", "晋亿实业"], ["601001", "大同煤业"], ["601000", "唐山港"],
         ["600996", "贵广网络"], ["600993", "马应龙"], ["600978", "宜华生活"], ["600971", "恒源煤电"], ["600970", "中材国际"],
         ["600967", "内蒙一机"], ["600939", "重庆建工"], ["600936", "广西广电"], ["600917", "重庆燃气"], ["600908", "无锡银行"],
         ["600894", "广日股份"], ["600885", "宏发股份"], ["600884", "杉杉股份"], ["600881", "亚泰集团"], ["600880", "博瑞传播"],
         ["600879", "航天电子"], ["600875", "东方电气"], ["600874", "创业环保"], ["600872", "中炬高新"], ["600869", "智慧能源"],
         ["600863", "内蒙华电"], ["600862", "中航高科"], ["600859", "王府井"], ["600848", "上海临港"], ["600839", "四川长虹"],
         ["600835", "上海机电"], ["600826", "兰生股份"], ["600823", "世茂股份"], ["600811", "东方集团"], ["600808", "马钢股份"],
         ["600801", "华新水泥"], ["600787", "中储股份"], ["600776", "东方通信"], ["600773", "西藏城投"], ["600770", "综艺股份"],
         ["600765", "中航重机"], ["600759", "洲际油气"], ["600757", "长江传媒"], ["600755", "厦门国贸"], ["600754", "锦江股份"],
         ["600751", "天海投资"], ["600750", "江中药业"], ["600748", "上实发展"], ["600743", "华远地产"], ["600737", "中粮糖业"],
         ["600729", "重庆百货"], ["600718", "东软集团"], ["600717", "天津港"], ["600694", "大商股份"], ["600687", "刚泰控股"],
         ["600673", "东阳光科"], ["600664", "哈药股份"], ["600657", "信达地产"], ["600655", "豫园股份"], ["600651", "飞乐音响"],
         ["600648", "外高桥"], ["600645", "中源协和"], ["600643", "爱建集团"], ["600642", "申能股份"], ["600640", "号百控股"],
         ["600639", "浦东金桥"], ["600635", "大众公用"], ["600633", "浙数文化"], ["600628", "新世界"], ["600623", "华谊集团"],
         ["600618", "氯碱化工"], ["600614", "鹏起科技"], ["600611", "大众交通"], ["600600", "青岛啤酒"], ["600598", "北大荒"],
         ["600597", "光明乳业"], ["600594", "益佰制药"], ["600587", "新华医疗"], ["600584", "长电科技"], ["600582", "天地科技"],
         ["600580", "卧龙电气"], ["600578", "京能电力"], ["600575", "皖江物流"], ["600572", "康恩贝"], ["600566", "济川药业"],
         ["600565", "迪马股份"], ["600563", "法拉电子"], ["600557", "康缘药业"], ["600545", "卓郎智能"], ["600536", "中国软件"],
         ["600525", "长园集团"], ["600521", "华海药业"], ["600517", "置信电气"], ["600516", "方大炭素"], ["600511", "国药股份"],
         ["600503", "华丽家族"], ["600500", "中化国际"], ["600499", "科达洁能"], ["600481", "双良节能"], ["600478", "科力远"],
         ["600466", "蓝光发展"], ["600460", "士兰微"], ["600458", "时代新材"], ["600438", "通威股份"], ["600435", "北方导航"],
         ["600428", "中远海特"], ["600426", "华鲁恒升"], ["600422", "昆药集团"], ["600418", "江淮汽车"], ["600416", "湘电股份"],
         ["600410", "华胜天成"], ["600409", "三友化工"], ["600395", "盘江股份"], ["600393", "粤泰股份"], ["600392", "盛和资源"],
         ["600388", "龙净环保"], ["600380", "健康元"], ["600366", "宁波韵升"], ["600348", "阳泉煤业"], ["600346", "恒力股份"],
         ["600338", "西藏珠峰"], ["600335", "国机汽车"], ["600329", "中新药业"], ["600325", "华发股份"], ["600317", "营口港"],
         ["600316", "洪都航空"], ["600315", "上海家化"], ["600312", "平高电气"], ["600307", "酒钢宏兴"], ["600300", "维维股份"],
         ["600298", "安琪酵母"], ["600292", "远达环保"], ["600291", "西水股份"], ["600289", "ST信通"], ["600284", "浦东建设"],
         ["600282", "南钢股份"], ["600280", "中央商场"], ["600277", "亿利洁能"], ["600270", "外运发展"], ["600267", "海正药业"],
         ["600266", "北京城建"], ["600260", "凯乐科技"], ["600259", "广晟有色"], ["600256", "广汇能源"], ["600240", "华业资本"],
         ["600216", "浙江医药"], ["600201", "生物股份"], ["600195", "中牧股份"], ["600187", "国中水务"], ["600184", "光电股份"],
         ["600183", "生益科技"], ["600179", "安通控股"], ["600176", "中国巨石"], ["600171", "上海贝岭"], ["600169", "太原重工"],
         ["600166", "福田汽车"], ["600161", "天坛生物"], ["600160", "巨化股份"], ["600158", "中体产业"], ["600155", "宝硕股份"],
         ["600151", "航天机电"], ["600143", "金发科技"], ["600141", "兴发集团"], ["600138", "中青旅"], ["600126", "杭钢股份"],
         ["600125", "铁龙物流"], ["600122", "宏图高科"], ["600120", "浙江东方"], ["600108", "亚盛集团"], ["600098", "广州发展"],
         ["600094", "大名城"], ["600086", "东方金钰"], ["600079", "人福医药"], ["600073", "上海梅林"], ["600064", "南京高科"],
         ["600062", "华润双鹤"], ["600060", "海信电器"], ["600059", "古越龙山"], ["600058", "五矿发展"], ["600056", "中国医药"],
         ["600053", "九鼎投资"], ["600039", "四川路桥"], ["600037", "歌华有线"], ["600026", "中远海能"], ["600022", "山东钢铁"],
         ["600017", "日照港"], ["600006", "东风汽车"], ["600004", "白云机场"], ["300383", "光环新网"], ["300376", "易事特"],
         ["300324", "旋极信息"], ["300297", "蓝盾股份"], ["300291", "华录百纳"], ["300287", "飞利信"], ["300274", "阳光电源"],
         ["300273", "和佳股份"], ["300266", "兴源环境"], ["300257", "开山股份"], ["300253", "卫宁健康"], ["300244", "迪安诊断"],
         ["300202", "聚龙股份"], ["300199", "翰宇药业"], ["300197", "铁汉生态"], ["300182", "捷成股份"], ["300166", "东方国信"],
         ["300159", "新研股份"], ["300147", "香雪制药"], ["300146", "汤臣倍健"], ["300134", "大富科技"], ["300133", "华策影视"],
         ["300116", "坚瑞沃能"], ["300115", "长盈精密"], ["300113", "顺网科技"], ["300088", "长信科技"], ["300058", "蓝色光标"],
         ["300055", "万邦达"], ["300043", "星辉娱乐"], ["300039", "上海凯宝"], ["300032", "金龙机电"], ["300026", "红日药业"],
         ["300010", "立思辰"], ["300002", "神州泰岳"], ["300001", "特锐德"], ["002818", "富森美"], ["002815", "崇达技术"],
         ["002807", "江阴银行"], ["002745", "木林森"], ["002709", "天赐材料"], ["002707", "众信旅游"], ["002701", "奥瑞金"],
         ["002699", "美盛文化"], ["002690", "美亚光电"], ["002681", "奋达科技"], ["002672", "东江环保"], ["002670", "国盛金控"],
         ["002665", "首航节能"], ["002663", "普邦股份"], ["002657", "中科金财"], ["002642", "荣之联"], ["002640", "跨境通"],
         ["002635", "安洁科技"], ["002603", "以岭药业"], ["002589", "瑞康医药"], ["002588", "史丹利"], ["002583", "海能达"],
         ["002573", "清新环境"], ["002551", "尚荣医疗"], ["002544", "杰赛科技"], ["002517", "恺英网络"], ["002512", "达华智能"],
         ["002506", "协鑫集成"], ["002505", "大康农业"], ["002503", "搜于特"], ["002491", "通鼎互联"], ["002489", "浙江永强"],
         ["002482", "广田集团"], ["002479", "富春环保"], ["002477", "雏鹰农牧"], ["002463", "沪电股份"], ["002444", "巨星科技"],
         ["002440", "闰土股份"], ["002439", "启明星辰"], ["002437", "誉衡药业"], ["002434", "万里扬"], ["002431", "棕榈股份"],
         ["002428", "云南锗业"], ["002422", "科伦药业"], ["002416", "爱施德"], ["002414", "高德红外"], ["002410", "广联达"],
         ["002408", "齐翔腾达"], ["002407", "多氟多"], ["002405", "四维图新"], ["002400", "省广股份"], ["002392", "北京利尔"],
         ["002390", "信邦制药"], ["002384", "东山精密"], ["002375", "亚厦股份"], ["002373", "千方科技"], ["002371", "北方华创"],
         ["002368", "太极股份"], ["002366", "台海核电"], ["002359", "北讯集团"], ["002358", "森源电气"], ["002354", "天神娱乐"],
         ["002353", "杰瑞股份"], ["002345", "潮宏基"], ["002344", "海宁皮城"], ["002342", "巨力索具"], ["002340", "格林美"],
         ["002332", "仙琚制药"], ["002325", "洪涛股份"], ["002317", "众生药业"], ["002311", "海大集团"], ["002308", "威创股份"],
         ["002299", "圣农发展"], ["002285", "世联行"], ["002281", "光迅科技"], ["002280", "联络互动"], ["002277", "友阿股份"],
         ["002276", "万马股份"], ["002273", "水晶光电"], ["002271", "东方雨虹"], ["002269", "美邦服饰"], ["002268", "卫士通"],
         ["002266", "浙富控股"], ["002261", "拓维信息"], ["002254", "泰和新材"], ["002251", "步步高"], ["002250", "联化科技"],
         ["002249", "大洋电机"], ["002244", "滨江集团"], ["002242", "九阳股份"], ["002233", "塔牌集团"], ["002223", "鱼跃医疗"],
         ["002221", "东华能源"], ["002195", "二三四五"], ["002191", "劲嘉股份"], ["002190", "成飞集成"], ["002183", "怡亚通"],
         ["002179", "中航光电"], ["002176", "江特电机"], ["002155", "湖南黄金"], ["002152", "广电运通"], ["002147", "新光圆成"],
         ["002131", "利欧股份"], ["002128", "露天煤业"], ["002127", "南极电商"], ["002123", "梦网集团"], ["002122", "天马股份"],
         ["002118", "紫鑫药业"], ["002106", "莱宝高科"], ["002093", "国脉科技"], ["002092", "中泰化学"], ["002078", "太阳纸业"],
         ["002073", "软控股份"], ["002064", "华峰氨纶"], ["002063", "远光软件"], ["002056", "横店东磁"], ["002051", "中工国际"],
         ["002050", "三花智控"], ["002049", "紫光国芯"], ["002048", "宁波华翔"], ["002041", "登海种业"], ["002038", "双鹭药业"],
         ["002032", "苏泊尔"], ["002030", "达安基因"], ["002028", "思源电气"], ["002022", "科华生物"], ["002019", "亿帆医药"],
         ["002018", "华信国际"], ["002013", "中航机电"], ["002011", "盾安环境"], ["002005", "德豪润达"], ["002004", "华邦健康"],
         ["002002", "鸿达兴业"], ["002001", "新和成"], ["001696", "宗申动力"], ["000999", "华润三九"], ["000998", "隆平高科"],
         ["000997", "新大陆"], ["000990", "诚志股份"], ["000988", "华工科技"], ["000987", "越秀金控"], ["000981", "银亿股份"],
         ["000979", "中弘股份"], ["000977", "浪潮信息"], ["000975", "银泰资源"], ["000970", "中科三环"], ["000969", "安泰科技"],
         ["000960", "锡业股份"], ["000939", "凯迪生态"], ["000937", "冀中能源"], ["000930", "中粮生化"], ["000926", "福星股份"],
         ["000897", "津滨发展"], ["000887", "中鼎股份"], ["000878", "云南铜业"], ["000877", "天山股份"], ["000860", "顺鑫农业"],
         ["000848", "承德露露"], ["000830", "鲁西化工"], ["000829", "天音控股"], ["000825", "太钢不锈"], ["000816", "智慧农业"],
         ["000807", "云铝股份"], ["000806", "银河生物"], ["000786", "北新建材"], ["000778", "新兴铸管"], ["000777", "中核科技"],
         ["000766", "通化金马"], ["000762", "西藏矿业"], ["000761", "本钢板材"], ["000758", "中色股份"], ["000732", "泰禾集团"],
         ["000729", "燕京啤酒"], ["000727", "华东科技"], ["000718", "苏宁环球"], ["000712", "锦龙股份"], ["000703", "恒逸石化"],
         ["000690", "宝新能源"], ["000685", "中山公用"], ["000681", "视觉中国"], ["000680", "山推股份"], ["000669", "金鸿控股"],
         ["000667", "美好置业"], ["000662", "天夏智慧"], ["000661", "长春高新"], ["000656", "金科股份"], ["000652", "泰达股份"],
         ["000636", "风华高科"], ["000612", "焦作万方"], ["000600", "建投能源"], ["000598", "兴蓉环境"], ["000596", "古井贡酒"],
         ["000592", "平潭发展"], ["000587", "金洲慈航"], ["000581", "威孚高科"], ["000572", "海马汽车"], ["000566", "海南海药"],
         ["000563", "陕国投A"], ["000552", "靖远煤电"], ["000547", "航天发展"], ["000543", "皖能电力"], ["000541", "佛山照明"],
         ["000536", "华映科技"], ["000528", "柳工"], ["000519", "中兵红箭"], ["000513", "丽珠集团"], ["000501", "鄂武商A"],
         ["000488", "晨鸣纸业"], ["000426", "兴业矿业"], ["000418", "小天鹅A"], ["000401", "冀东水泥"], ["000400", "许继电气"],
         ["000158", "常山北明"], ["000156", "华数传媒"], ["000099", "中信海直"], ["000090", "天健集团"], ["000089", "深圳机场"],
         ["000078", "海王生物"], ["000066", "中国长城"], ["000062", "深圳华强"], ["000061", "农产品"], ["000050", "深天马A"],
         ["000049", "德赛电池"], ["000039", "中集集团"], ["000031", "中粮地产"], ["000028", "国药一致"], ["000027", "深圳能源"],
         ["000025", "特力A"], ["000021", "深科技"], ["000012", "南玻A"], ["000009", "中国宝安"], ["000006", "深振业A"]]

