#/python3

#/python3

import json
import pygal_maps_world.maps
from Download_Data.country_codes import get_country_code

# 将数据加载到一个列表中
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)
    # print(pop_data)

# 创建一个包含人口数量的字典
cc_populations = {}
# 打印每个国家2010年的人口数量
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country = pop_dict['Country Name']
        # country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country)
        if code:
            cc_populations[code] = population
            # print(code + ": " + str(population))
        # else:
        #     print('ERROR - ' + country_name)
        # print(country_name + ": " + str(population))
wm = pygal_maps_world.maps.World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')

