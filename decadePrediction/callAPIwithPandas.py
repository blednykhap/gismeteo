# Thanks everyone who leave token on github
#5e21a0d240ae36.51672911
#5c51afc32bfd12.13951840
#5c10e9ce8e02f6.83138424
#61f2622da85fe2.06084651
#5fca514ed5e269.07203450

import requests
import pandas as pd
from requests.exceptions import HTTPError

def getCityData(path):
    try:

        headers = {'X-Gismeteo-Token': '5e21a0d240ae36.51672911'}
        response = requests.get(url=path, headers=headers)
        response.raise_for_status()

        jsonResponse = response.json()
        dataBlock = jsonResponse.get('response')

        normalizedDF = pd.json_normalize(dataBlock)
        renamedDF = normalizedDF.rename(columns={
            "precipitation.type_ext": "precipitation_type_ext",         "precipitation.intensity": "precipitation_intensity",
            "precipitation.amount": "precipitation_amount",             "precipitation.type": "precipitation_type",
            "pressure.h_pa.max": "pressure_h_pa_max",                   "pressure.h_pa.min": "pressure_h_pa_min",
            "pressure.mm_hg_atm.max": "pressure_mm_hg_atm_max",         "pressure.mm_hg_atm.min": "pressure_mm_hg_atm_min",
            "pressure.in_hg.max": "pressure_in_hg_max",                 "pressure.in_hg.min": "pressure_in_hg_min",
            "humidity.percent.max": "humidity_percent_max",             "humidity.percent.min": "humidity_percent_min",
            "humidity.percent.avg": "humidity_percent_avg",             "description.full": "description_full",
            "cloudiness.type": "cloudiness_type",                       "cloudiness.percent": "cloudiness_percent",
            "date.UTC": "date_UTC",                                     "date.local": "date_local",
            "date.time_zone_offset": "date_time_zone_offset",           "date.unix": "date_unix",
            "radiation.max": "radiation_max",                           "radiation.max_index": "radiation_max_index",
            "temperature.comfort.max.C": "temperature_comfort_max_C",   "temperature.comfort.max.F": "temperature_comfort_max_F",
            "temperature.comfort.min.C": "temperature_comfort_min_C",   "temperature.comfort.min.F": "temperature_comfort_min_F",
            "temperature.water.max.C": "temperature_water_max_C",       "temperature.water.max.F": "temperature_water_max_F",
            "temperature.water.min.C": "temperature_water_min_C",       "temperature.water.min.F": "temperature_water_min_F",
            "temperature.air.max.C": "temperature_air_max_C",           "temperature.air.max.F": "temperature_air_max_F",
            "temperature.air.min.C": "temperature_air_min_C",           "temperature.air.min.F": "temperature_air_min_F",
            "temperature.air.avg.C": "temperature_air_avg_C",           "temperature.air.avg.F": "temperature_air_avg_F",
            "wind.speed.max.km_h": "wind_speed_max_km_h",               "wind.speed.max.m_s": "wind_speed_max_m_s",
            "wind.speed.max.mi_h": "wind_speed_max_mi_h",               "wind.speed.min.km_h": "wind_speed_min_km_h",
            "wind.speed.min.m_s": "wind_speed_min_m_s",                 "wind.speed.min.mi_h": "wind_speed_min_mi_h",
            "wind.speed.avg.km_h": "wind_speed_avg_km_h",               "wind.speed.avg.m_s": "wind_speed_avg_m_s",
            "wind.speed.avg.mi_h": "wind_speed_avg_mi_h",               "wind.direction.max.degree": "wind_direction_maxdegree",
            "wind.direction.max.scale_8": "wind_direction_max_scale_8", "wind.direction.min.degree": "wind_direction_min_degree",
            "wind.direction.min.scale_8": "wind_direction_min_scale_8", "wind.direction.avg.degree": "wind_direction_avg_degree",
            "wind.direction.avg.scale_8": "wind_direction_avg_scale_8"})

        columnsTitles = ['city', 'cloudiness_percent', 'cloudiness_type', 'date_local', 'date_time_zone_offset',
                         'date_unix', 'date_utc', 'description_full', 'gm', 'humidity_percent_avg', 'humidity_percent_max',
                         'humidity_percent_min', 'kind', 'phenomenon', 'precipitation_amount', 'precipitation_intensity',
                         'precipitation_type', 'pressure_h_pa_max', 'pressure_h_pa_min', 'pressure_in_hg_max',
                         'pressure_in_hg_min', 'pressure_mm_hg_atm_max', 'pressure_mm_hg_atm_min', 'storm',
                         'temperature_air_avg_c', 'temperature_air_avg_f', 'temperature_air_max_c', 'temperature_air_max_f',
                         'temperature_air_min_c', 'temperature_air_min_f', 'temperature_comfort_max_c', 'temperature_comfort_max_f',
                         'temperature_comfort_min_c', 'temperature_comfort_min_f', 'temperature_water_max_c',
                         'temperature_water_max_f', 'temperature_water_min_c', 'temperature_water_min_f',
                         'wind_direction_avd_scale_8', 'wind_direction_avg_degree', 'wind_direction_max_degree',
                         'wind_direction_max_scale_8', 'wind_direction_min_degree', 'wind_direction_min_scale_8',
                         'wind_speed_avg_km_h', 'wind_speed_avg_m_s', 'wind_speed_avg_mi_h', 'wind_speed_max_km_h',
                         'wind_speed_max_m_s', 'wind_speed_max_mi_h', 'wind_speed_min_km_h', 'wind_speed_min_m_s',
                         'wind_speed_min_mi_h']

        reindexDF = renamedDF.reindex(columns=columnsTitles)
        #renamedDF.info()
        return reindexDF
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')

cityCodes = [4079, 4368, 4517, 4693, 4720, 5136, 4674, 4355, 4690, 4578, 3994, 4501, 4565, 4313]
resutlDf = pd.DataFrame()

for cod in cityCodes:
    url = 'https://api.gismeteo.net/v2/weather/forecast/aggregate/{}/?days=10'.format(cod)
    df = getCityData(url)
    resutlDf = pd.concat([resutlDf, df])

resutlDf.to_csv('d:\\temp\\apidata.csv', encoding='utf-8', index=False)
