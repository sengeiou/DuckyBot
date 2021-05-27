from src.utils.request import get_text
import json

with open(r'src/data/area.txt') as file_obj:
    areas = file_obj.read().split()


async def get_now_weather(area: str):
    # 获取地区id
    location_url = 'https://geoapi.qweather.com/v2/city/lookup'
    location_params = {
        'key': '0c5d383ed2db4b27a69f0de2b8135e6a',
        'location': area
    }
    data = json.loads(
        await get_text(location_url, params=location_params))
    # 获取实时天气
    now_weather_url = 'https://devapi.qweather.com/v7/weather/now'
    now_weather_params = {
        'key': '0c5d383ed2db4b27a69f0de2b8135e6a',
        'location': data['location'][0]['id']
    }
    data = json.loads(
        await get_text(now_weather_url, params=now_weather_params))['now']
    return data
