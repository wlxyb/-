import urllib.request
import json

from WeatherVoice.weatherserver.config import *


class RealTimeWeather:

    #返回高德地图天气数据
    def get_city_weather(self,city,type):
        search_type = typedict[type]
        if search_type == 0: # 实时天气
            url_weather = 'https://restapi.amap.com/v3/weather/weatherInfo?city='+citydict[city]+'&extensions=base&key=c16c8cca95224a9d05141cc9ce0fd8f6'
        elif search_type == 1: # 预报天气
            url_weather = 'https://restapi.amap.com/v3/weather/weatherInfo?city='+citydict[city]+'&extensions=all&key=c16c8cca95224a9d05141cc9ce0fd8f6'
        else:
            return -1
        #url_weather = 'https://free-api.heweather.com/v5/'+search+'?city='+index+'&key=和风天气KEY'
        response_url = urllib.request.urlopen(url_weather)
        context = response_url.read()
        get_weather_json = json.loads(context.decode('utf-8'))
        f = open("CityWeather.txt", 'w')
        f.write(context.decode('utf-8'))
        f.close()
        if search_type == 0:
            weather = get_weather_json
            #print(weather)
            #weather = weather_json["HeWeather5"][0]['daily_forecast'][0]
        else:
            weather = get_weather_json
        return weather


    #获取JSON中具体天气数据
    def get_weather(self,city,type):
        _weather = self.get_city_weather(city,type)
        search_type = typedict[type]
        if search_type==0:

            provi = _weather['lives'][0]['province']    #省份名
            cityn = _weather['lives'][0]['city']        #城市名
            adcod = _weather['lives'][0]['adcode']      #区域编码
            weath = _weather['lives'][0]['weather']     #天气现象（汉字描述）
            tempe = _weather['lives'][0]['temperature'] #实时气温，单位：摄氏度
            windd = _weather['lives'][0]['winddirection']#风向描述
            windp = _weather['lives'][0]['windpower']   #风力级别，单位：级
            humid = _weather['lives'][0]['humidity']    #空气湿度
            repor = _weather['lives'][0]['reporttime']  #数据发布的时间
            tempe=tempe.replace("-","零下")
            return "当前城市为{},天气 {},室外温度{}度,风向 {}风,强度为{}级,空气湿度为{}，数据更新时间为{}.".format(cityn,weath,tempe,windd,windp,humid,repor)
        else:
            provi = _weather['forecasts'][0]['province']  # 省份名
            cityn = _weather['forecasts'][0]['city']  # 城市名
            adcod = _weather['forecasts'][0]['adcode']  # 区域编码
            date=_weather['forecasts'][0]['casts'][0]['date']#当天
            date1=_weather['forecasts'][0]['casts'][1]['date']#明天日期
            date2=_weather['forecasts'][0]['casts'][2]['date']#后天日期
            date3=_weather['forecasts'][0]['casts'][3]['date']#大后天日期
            day_weath = _weather['forecasts'][0]['casts'][0]['dayweather']  # 当日天气现象（汉字描述）
            day_weath1 = _weather['forecasts'][0]['casts'][1]['dayweather']  # 明日天气现象（汉字描述）
            day_weath2 = _weather['forecasts'][0]['casts'][2]['dayweather']  # 后日天气现象（汉字描述）
            day_weath3 = _weather['forecasts'][0]['casts'][3]['dayweather']  # 大后日天气现象（汉字描述）
            night_weath = _weather['forecasts'][0]['casts'][0]['nightweather']  # 当日天气现象（汉字描述）夜间
            night_weath1 = _weather['forecasts'][0]['casts'][1]['nightweather']  # 明日天气现象（汉字描述）夜间
            night_weath2 = _weather['forecasts'][0]['casts'][2]['nightweather']  # 后日天气现象（汉字描述）夜间
            night_weath3 = _weather['forecasts'][0]['casts'][3]['nightweather']  # 大后日天气现象（汉字描述）夜间
            tempe = _weather['forecasts'][0]['casts'][0]['daytemp']  # 实时气温，单位：摄氏度
            tempe1 = _weather['forecasts'][0]['casts'][1]['daytemp']  # 实时气温，单位：摄氏度
            tempe2 = _weather['forecasts'][0]['casts'][2]['daytemp']  # 实时气温，单位：摄氏度
            tempe3 = _weather['forecasts'][0]['casts'][3]['daytemp']  # 实时气温，单位：摄氏度
            windd = _weather['forecasts'][0]['casts'][0]['daywind']  # 风向描述
            windd1 = _weather['forecasts'][0]['casts'][1]['daywind']  # 风向描述
            windd2 = _weather['forecasts'][0]['casts'][2]['daywind']  # 风向描述
            windd3 = _weather['forecasts'][0]['casts'][3]['daywind']  # 风向描述
            windp = _weather['forecasts'][0]['casts'][0]['daypower']   # 风力级别，单位：级
            windp1 = _weather['forecasts'][0]['casts'][1]['daypower']   # 风力级别，单位：级
            windp2 = _weather['forecasts'][0]['casts'][2]['daypower']   # 风力级别，单位：级
            windp3 = _weather['forecasts'][0]['casts'][3]['daypower']   # 风力级别，单位：级
            humid = _weather['forecasts'][0]['casts']   # 空气湿度
            repor = _weather['forecasts'][0]['reporttime']  # 数据发布的时间
            tempe = tempe.replace("-", "零下")
            return """城市:{}, 明日{},夜间{},温度{},风向{}风,强度{}级, 后天{},夜间{},温度{},风向{}风,强度{}级,大后天{},夜间{},温度{},风向{}风,强度{}级, 发布时间{}.""".format(cityn, day_weath1,night_weath1, tempe1, windd1, windp1,day_weath2,night_weath2,tempe2, windd2, windp2,day_weath3,night_weath3,tempe3, windd3, windp3,repor)


if __name__ == "__main__":
    result = RealTimeWeather().get_weather("深圳","预报")
    print(result)
