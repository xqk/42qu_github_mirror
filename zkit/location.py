# -*- coding: utf-8 -*-

import earth
from earth import PID2NAME
from lcs import  ordered_LSS_list

EVENT_LOCATION = {
"ali":"阿里",
"yushu":"玉树",
"ningxia":"宁夏",
"sichuan":"四川",
"qiannan":"黔南",
"huaihua":"怀化",
"liupanshui":"六盘水",
"shanghai":"上海",
"anshun":"安顺",
"puyang":"濮阳",
"dongying":"东营",
"huangshi":"黄石",
"hetian":"和田",
"jiyuan":"济源",
"zhejiang":"浙江",
"sanming":"三明",
"kaiping":"开平",
"yangzhou":"扬州",
"bayinguolengzhou":"巴音郭楞州",
"pingdingshan":"平顶山",
"wuxi":"无锡",
"fujian":"福建",
"ankang":"安康",
"boertalazhou":"博尔塔拉州",
"qujing":"曲靖",
"tongliao":"通辽",
"qiqihaer":"齐齐哈尔",
"zhuhai":"珠海",
"changdou":"昌都",
"zhangjiakou":"张家口",
"changsha":"长沙",
"jilin":"吉林",
"aba":"阿坝",
"ziyang":"资阳",
"xinzhou":"忻州",
"yingtan":"鹰潭",
"tianmen":"天门",
"tongling":"铜陵",
"xingtai":"邢台",
"huaibei":"淮北",
"hebei":"河北",
"guangzhou":"广州",
"zhangzhou":"漳州",
"tianshui":"天水",
"wuhan":"武汉",
"changzhi":"长治",
"wuhai":"乌海",
"chongqing":"重庆",
"fuyang":"阜阳",
"eerduosi":"鄂尔多斯",
"hulunbeier":"呼伦贝尔",
"shangrao":"上饶",
"changzhou":"常州",
"hengshui":"衡水",
"lishui":"丽水",
"wujiang":"吴江",
"guangan":"广安",
"nanjing":"南京",
"hezhou":"贺州",
"langfang":"廊坊",
"rikaze":"日喀则",
"zunyi":"遵义",
"fuxin":"阜新",
"yibin":"宜宾",
"datong":"大同",
"dandong":"丹东",
"kelamayi":"克拉玛依",
"anqing":"安庆",
"pingliang":"平凉",
"dingxi":"定西",
"zhangjiagang":"张家港",
"kezilesu":"克孜勒苏",
"shanwei":"汕尾",
"jiaxing":"嘉兴",
"guyuan":"固原",
"xiamen":"厦门",
"lijiang":"丽江",
"qitaihe":"七台河",
"shijiazhuang":"石家庄",
"yichang":"宜昌",
"changshu":"常熟",
"beijing":"北京",
"benxi":"本溪",
"jieyang":"揭阳",
"shanxi":"山西",
"bazhong":"巴中",
"kezilesukeerkezi":"克孜勒苏柯尔克孜",
"shihezi":"石河子",
"aletai":"阿勒泰",
"shiyan":"十堰",
"dehong":"德宏",
"yunnan":"云南",
"changchun":"长春",
"xinganmeng":"兴安盟",
"bozhou":"亳州",
"118378":"榆林",
"nanchang":"南昌",
"nanchong":"南充",
"tangshan":"唐山",
"tongren":"铜仁",
"baishan":"白山",
"enshi":"恩施",
"zhoukou":"周口",
"hengyang":"衡阳",
"songyuan":"松原",
"xinyang":"信阳",
"lincang":"临沧",
"liaoyang":"辽阳",
"anhui":"安徽",
"kaifeng":"开封",
"linyi":"临沂",
"jiuquan":"酒泉",
"qinzhou":"钦州",
"neimenggu":"内蒙古",
"maoming":"茂名",
"huaian":"淮安",
"fushun":"抚顺",
"yueyang":"岳阳",
"boertala":"博尔塔拉",
"nujiang":"怒江",
"sanya":"三亚",
"huhehaote":"呼和浩特",
"panjin":"盘锦",
"linzhi":"林芝",
"foshan":"佛山",
"shaoxing":"绍兴",
"yanan":"延安",
"heyuan":"河源",
"jingzhou":"荆州",
"haibei":"海北",
"guangdong":"广东",
"heze":"菏泽",
"118152":"伊春",
"changde":"常德",
"chaohu":"巢湖",
"xilinguole":"锡林郭勒",
"baiyin":"白银",
"dazhou":"达州",
"nantong":"南通",
"yangling":"杨凌",
"tieling":"铁岭",
"bangbu":"蚌埠",
"longnan":"陇南",
"zhumadian":"驻马店",
"shaanxi":"陕西",
"yangjiang":"阳江",
"weifang":"潍坊",
"binzhou":"滨州",
"shenyang":"沈阳",
"qinghai":"青海",
"pingxiang":"萍乡",
"zhuzhou":"株洲",
"chongzuo":"崇左",
"zhenjiang":"镇江",
"lianyungang":"连云港",
"guigang":"贵港",
"zhongshan":"中山",
"lvliang":"吕梁",
"hanzhong":"汉中",
"haian":"海安",
"shennongjialinqu":"神农架林区",
"jinchang":"金昌",
"ganzi":"甘孜",
"jinhua":"金华",
"taizhou":"泰州",
"jiangsu":"江苏",
"jingdezhen":"景德镇",
"zhaoqing":"肇庆",
"laiwu":"莱芜",
"naqu":"那曲",
"wuzhong":"吴忠",
"jincheng":"晋城",
"ningbo":"宁波",
"118399":"海南",
"gansu":"甘肃",
"nanping":"南平",
"dalian":"大连",
"yingkou":"营口",
"panzhihua":"攀枝花",
"mianyang":"绵阳",
"simao":"思茅",
"yangquan":"阳泉",
"baise":"百色",
"qiandongnan":"黔东南",
"yantai":"烟台",
"tianjin":"天津",
"quanzhou":"泉州",
"suihua":"绥化",
"huludao":"葫芦岛",
"chifeng":"赤峰",
"yunfu":"云浮",
"chuzhou":"滁州",
"haikou":"海口",
"longyan":"龙岩",
"jiangxi":"江西",
"xinxiang":"新乡",
"xiaogan":"孝感",
"yinchuan":"银川",
"shaoguan":"韶关",
"heihe":"黑河",
"beihai":"北海",
"xiuqian":"宿迁",
"huainan":"淮南",
"shannan":"山南",
"huanggang":"黄冈",
"wuhu":"芜湖",
"siping":"四平",
"deyang":"德阳",
"heilongjiang":"黑龙江",
"jiamusi":"佳木斯",
"xinjiang":"新疆",
"diqing":"迪庆",
"118218":"抚州",
"weihai":"威海",
"jiaozuo":"焦作",
"hangzhou":"杭州",
"alaer":"阿拉尔",
"guizhou":"贵州",
"huizhou":"惠州",
"zhangjiajie":"张家界",
"shuozhou":"朔州",
"tulufan":"吐鲁番",
"xingan":"兴安",
"honghe":"红河",
"hebi":"鹤壁",
"dongguan":"东莞",
"qinhuangdao":"秦皇岛",
"qionghai":"琼海",
"jiangmen":"江门",
"xining":"西宁",
"hefei":"合肥",
"leshan":"乐山",
"xuzhou":"徐州",
"jiayuguan":"嘉峪关",
"bayinguoleng":"巴音郭楞",
"cangzhou":"沧州",
"anyang":"安阳",
"zigong":"自贡",
"lasa":"拉萨",
"xianning":"咸宁",
"rizhao":"日照",
"guangxi":"广西",
"xiangtan":"湘潭",
"jinan":"济南",
"meishan":"眉山",
"qingyuan":"清远",
"wuzhou":"梧州",
"zaozhuang":"枣庄",
"yaan":"雅安",
"taian":"泰安",
"zhangye":"张掖",
"tongchuan":"铜川",
"guilin":"桂林",
"yanbian":"延边",
"lanzhou":"兰州",
"shantou":"汕头",
"qianxinan":"黔西南",
"yuxi":"玉溪",
"wenshan":"文山",
"kunming":"昆明",
"danzhou":"儋州",
"tacheng":"塔城",
"suzhou":"苏州",
"wuwei":"武威",
"baoshan":"保山",
"hunan":"湖南",
"xian":"西安",
"yichun":"宜春",
"jinzhong":"晋中",
"guoluo":"果洛",
"hechi":"河池",
"baicheng":"白城",
"akesu":"阿克苏",
"baoding":"保定",
"laibin":"来宾",
"huzhou":"湖州",
"qianjiang":"潜江",
"yancheng":"盐城",
"haerbin":"哈尔滨",
"baotou":"包头",
"ezhou":"鄂州",
"118181":"台州",
"jinzhou":"锦州",
"xiuzhou":"宿州",
"liaocheng":"聊城",
"kashen":"喀什",
"daqing":"大庆",
"putian":"莆田",
"anshan":"鞍山",
"qingyang":"庆阳",
"yuncheng":"运城",
"ganzhou":"赣州",
"zhongwei":"中卫",
"haidong":"海东",
"zhengzhou":"郑州",
"suizhou":"随州",
"xuancheng":"宣城",
"changji":"昌吉",
"shaoyang":"邵阳",
"xizang":"西藏",
"liaoyuan":"辽源",
"neijiang":"内江",
"xiantao":"仙桃",
"daning":"大宁",
"shangqiu":"商丘",
"liangshan":"凉山",
"zhanjiang":"湛江",
"dehongjingpozu":"德宏景颇族",
"nanning":"南宁",
"guiyang":"贵阳",
"fuzhou":"福州",
"shenzhen":"深圳",
"linfen":"临汾",
"loudi":"娄底",
"handan":"邯郸",
"yulin":"玉林",
"yongzhou":"永州",
"chaozhou":"潮州",
"maanshan":"马鞍山",
"shuangyashan":"双鸭山",
"mudanjiang":"牡丹江",
"jining":"济宁",
"wulumuqi":"乌鲁木齐",
"puer":"普洱",
"xuchang":"许昌",
"jiujiang":"九江",
"alashanmeng":"阿拉善盟",
"linxia":"临夏",
"quzhou":"衢州",
"hubei":"湖北",
"gannan":"甘南",
"luoyang":"洛阳",
"hegang":"鹤岗",
"qingdao":"青岛",
"bayannaoer":"巴彦淖尔",
"ningde":"宁德",
"shangluo":"商洛",
"jian":"吉安",
"meizhou":"梅州",
"zibo":"淄博",
"wulanchabu":"乌兰察布",
"chengde":"承德",
"liaoning":"辽宁",
"tonghua":"通化",
"daxinganling":"大兴安岭",
"haixi":"海西",
"shizuishan":"石嘴山",
"xilinguolemeng":"锡林郭勒盟",
"yiyang":"益阳",
"zhaotong":"昭通",
"guangyuan":"广元",
"xianyang":"咸阳",
"dezhou":"德州",
"xishuangbanna":"西双版纳",
"wenzhou":"温州",
"zhoushan":"舟山",
"luzhou":"泸州",
"weinan":"渭南",
"liuzhou":"柳州",
"luohe":"漯河",
"henan":"河南",
"chizhou":"池州",
"jingmen":"荆门",
"shandong":"山东",
"huangnan":"黄南",
"sanmenxia":"三门峡",
"chuxiong":"楚雄",
"yili":"伊犁",
"bijie":"毕节",
"chenzhou":"郴州",
"jixi":"鸡西",
"alashan":"阿拉善",
"chaoyang":"朝阳",
"hami":"哈密",
"nanyang":"南阳",
"tumushuke":"图木舒克",
"fangchenggang":"防城港",
"kunshan":"昆山",
"xiangfan":"襄樊",
"xinyu":"新余",
"dali":"大理",
"liuan":"六安",
"chengdu":"成都",
"baoji":"宝鸡",
"xiangxi":"湘西",
"huangshan":"黄山",
"suining":"遂宁",
"taiyuan":"太原",
}
SEARCH = dict([(v,k) for k,v in PID2NAME.iteritems()])
for pinyin, pin_city  in EVENT_LOCATION.iteritems():
    best_match, match = ordered_LSS_list(pin_city,SEARCH.keys())[0]
    print pin_city, pinyin  , best_match ,SEARCH[best_match] 

