# Thanks everyone who leave token on github
#5e21a0d240ae36.51672911
#5c51afc32bfd12.13951840
#5c10e9ce8e02f6.83138424
#61f2622da85fe2.06084651
#5fca514ed5e269.07203450

import requests
import csv
from requests.exceptions import HTTPError

headers = {'X-Gismeteo-Token': '5e21a0d240ae36.51672911'}

url = 'https://api.gismeteo.net/v2/weather/forecast/aggregate/4368/?days=10'

try:
    response = requests.get(url=url, headers=headers)
    response.raise_for_status()

    json = response.json()
    data = json.get('response')
    print(data)

    for row in data:
        print('********** ********** ********** ********** **********')
        print(row)
        print('precipitation:',
              row['precipitation']['type_ext'], row['precipitation']['intensity'],
              row['precipitation']['amount'], row['precipitation']['type'])
        print('pressure:',
              row['pressure']['h_pa']['max'], row['pressure']['h_pa']['min'],
              row['pressure']['mm_hg_atm']['max'], row['pressure']['mm_hg_atm']['min'],
              row['pressure']['in_hg']['max'], row['pressure']['in_hg']['min'])
        print('humidity:',
              row['humidity']['percent']['max'], row['humidity']['percent']['min'], row['humidity']['percent']['avg'])
        print('gm:', row['gm'])
        print('description:', row['description']['full'])
        print('cloudiness:', row['cloudiness']['type'], row['cloudiness']['percent'])
        print('date:', row['date']['UTC'], row['date']['local'], row['date']['time_zone_offset'], row['date']['unix'])
        print('phenomenon:', row['phenomenon'])
        print('radiation:', row['radiation']['max'], row['radiation']['max_index'])
        print('city:', row['city'])
        print('kind:', row['kind'])
        print('storm:', row['storm'])
        print('temperature:',
              row['temperature']['comfort']['max']['C'], row['temperature']['comfort']['max']['F'],
              row['temperature']['comfort']['min']['C'], row['temperature']['comfort']['min']['F'],
              row['temperature']['water']['max']['C'], row['temperature']['water']['max']['F'],
              row['temperature']['water']['min']['C'], row['temperature']['water']['min']['F'],
              row['temperature']['air']['max']['C'], row['temperature']['air']['max']['F'],
              row['temperature']['air']['min']['C'], row['temperature']['air']['min']['F'],
              row['temperature']['air']['avg']['C'], row['temperature']['air']['avg']['F'])
        print('wind:',
              row['wind']['speed']['max']['km_h'], row['wind']['speed']['max']['m_s'], row['wind']['speed']['max']['mi_h'],
              row['wind']['speed']['min']['km_h'], row['wind']['speed']['min']['m_s'], row['wind']['speed']['min']['mi_h'],
              row['wind']['speed']['avg']['km_h'], row['wind']['speed']['avg']['m_s'], row['wind']['speed']['avg']['mi_h'],
              row['wind']['direction']['max']['degree'], row['wind']['direction']['max']['scale_8'],
              row['wind']['direction']['min']['degree'], row['wind']['direction']['min']['scale_8'],
              row['wind']['direction']['avg']['degree'], row['wind']['direction']['avg']['scale_8']),
        print('icon:', row['icon'])

    file = csv.writer(open('d:\\temp\\apidata.csv', 'w', newline='', encoding='utf-8'))

    # write header
    file.writerow([
        # precipitation
        'precipitation_typeext', 'precipitation_intensity', 'precipitation_amount', 'precipitation_type',
        # pressure
        'pressure_hpa_max', 'pressure_hpa_min', 'pressure_mmhgatm_max', 'pressure_mmhgatm_min', 'pressure_inhg_max', 'pressure_inhg_min',
        # humidity
        'humidity_percent_max', 'humidity_percent_min', 'humidity_percent_avg',
        # gm
        'gm',
        # description
        'description_full',
        # cloudiness
        'cloudiness_type', 'cloudiness_percent',
        # date
        'date_UTC', 'date_local', 'date_time_zone_offset', 'date_unix',
        # phenomenon
        'phenomenon',
        # radiation
        'radiation_max', 'radiation_maxindex',
        # city
        'city',
        # kind:
        'kind',
        # storm
        'storm',
        # temperature
        'temperature_comfort_max_C', 'temperature_comfort_max_F', 'temperature_comfort_min_C', 'temperature_comfort_min_F',
        'temperature_water_max_C', 'temperature_water_max_F', 'temperature_water_min_C', 'temperature_water_min_F',
        'temperature_air_max_C', 'temperature_air_max_F', 'temperature_air_min_C', 'temperature_air_min_F', 'temperature_air_avg_C', 'temperature_air_avg_F',
        # wind
        'wind_speed_max_kmh', 'wind_speed_max_ms', 'wind_speed_max_mih',
        'wind_speed_min_kmh', 'wind_speed_min_ms', 'wind_speed_min_mih',
        'wind_speed_avg_kmh', 'wind_speed_avg_ms', 'wind_speed_avg_mih',
        'wind_direction_max_degree', 'wind_direction_max_scale8',
        'wind_direction_min_degree', 'wind_direction_min_scale8',
        'wind_direction_avg_degree', 'wind_direction_avg_scale8',
        # icon
        'icon'
    ])


    for row in data:
        file.writerow([
            # precipitation
            row['precipitation']['type_ext'], row['precipitation']['intensity'],
            row['precipitation']['amount'], row['precipitation']['type'],
            # pressure
            row['pressure']['h_pa']['max'], row['pressure']['h_pa']['min'],
            row['pressure']['mm_hg_atm']['max'], row['pressure']['mm_hg_atm']['min'],
            row['pressure']['in_hg']['max'], row['pressure']['in_hg']['min'],
            # humidity
            row['humidity']['percent']['max'], row['humidity']['percent']['min'], row['humidity']['percent']['avg'],
            # gm
            row['gm'],
            # description
            row['description']['full'],
            # cloudiness
            row['cloudiness']['type'], row['cloudiness']['percent'],
            # date
            row['date']['UTC'], row['date']['local'], row['date']['time_zone_offset'], row['date']['unix'],
            # phenomenon
            row['phenomenon'],
            # radiation
            row['radiation']['max'], row['radiation']['max_index'],
            # city
            row['city'],
            # kind:
            row['kind'],
            # storm
            row['storm'],
            # temperature
            row['temperature']['comfort']['max']['C'], row['temperature']['comfort']['max']['F'],
            row['temperature']['comfort']['min']['C'], row['temperature']['comfort']['min']['F'],
            row['temperature']['water']['max']['C'], row['temperature']['water']['max']['F'],
            row['temperature']['water']['min']['C'], row['temperature']['water']['min']['F'],
            row['temperature']['air']['max']['C'], row['temperature']['air']['max']['F'],
            row['temperature']['air']['min']['C'], row['temperature']['air']['min']['F'],
            row['temperature']['air']['avg']['C'], row['temperature']['air']['avg']['F'],
            # wind
            row['wind']['speed']['max']['km_h'], row['wind']['speed']['max']['m_s'], row['wind']['speed']['max']['mi_h'],
            row['wind']['speed']['min']['km_h'], row['wind']['speed']['min']['m_s'], row['wind']['speed']['min']['mi_h'],
            row['wind']['speed']['avg']['km_h'], row['wind']['speed']['avg']['m_s'], row['wind']['speed']['avg']['mi_h'],
            row['wind']['direction']['max']['degree'], row['wind']['direction']['max']['scale_8'],
            row['wind']['direction']['min']['degree'], row['wind']['direction']['min']['scale_8'],
            row['wind']['direction']['avg']['degree'], row['wind']['direction']['avg']['scale_8'],
            # icon
            row['icon']
        ])

except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

