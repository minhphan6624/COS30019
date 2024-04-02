import sys

filename = sys.argv[1]

country_map = {}  # The cities dictionary

with open(filename) as aFile:
    for line in aFile:
        content = line.strip()  # Remove redundant spaces

        content_list = content.split(" ")
        city1 = content_list[0]
        city2 = content_list[1]
        actualD = content_list[2]
        flightD = content_list[3]

        if country_map.get(city1):  # If city1 is not in the dictionary yet
            city1_list = country_map.get(city1)
            city1_list.append((city2, int(actualD), int(flightD)))
            country_map.update({city1: city1_list})
        else:
            country_map.update({city1: [(city2, int(actualD), int(flightD))]})

        if country_map.get(city2):  # Do the same for city2
            city2_list = country_map.get(city2)
            city2_list.append((city1, int(actualD), int(flightD)))
            country_map.update({city2: city2_list})
        else:
            country_map.update({city2: [(city1, int(actualD), int(flightD))]})

print(country_map)
