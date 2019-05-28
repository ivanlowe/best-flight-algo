from shortest_path import MapGraph
import method1
import random

g = MapGraph()

list1 = ["Tokyo","New Delhi","Kuala Lumpur","Dubai","Ankara","Beijing","Seoul","Taipei","Singapore","Islamabad"]

for city1 in list1:
	for city2 in list1:
		g.add_road(city1,city2,random.randint(100,1000))

print(method1.get_best_path(g, "kuala lumpur", "tokyo"))