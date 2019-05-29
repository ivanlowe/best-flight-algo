from shortest_path import MapGraph
import method1
import method2
import random
from sentiment_news import NewsSentiment
from do100trial import do100
from plot_paths import plot_map_with_one_path


g = MapGraph()

list1 = ["Tokyo","New Delhi","Kuala Lumpur","Dubai","Ankara","Beijing","Seoul","Taipei","Singapore","Islamabad"]

NewsSentiment().prefetch_news_city(list1)

for city1 in list1:
	for city2 in list1:
		g.add_road(city1,city2,random.randint(100,1000))

x = method1.get_best_path(g, "kuala lumpur", "tokyo")
print(x)
print("\n")
print(method2.get_best_path(g, "kuala lumpur", "tokyo"))

plot_map_with_one_path (x[0], "C:\\Users\\aminq\\Desktop\\maps\\mapf.html")

# Take care this method takes around 2 minutes running time
# Cause it creates 100 random graphs
"""
x = do100()
print(x)
"""