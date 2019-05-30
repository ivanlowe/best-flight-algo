from shortest_path import MapGraph
import method1
import method2
import random
from sentiment_news import NewsSentiment
from do100trial import do100
from plot_paths import plot_map_with_one_path
from plot_paths import plot_map_with_many_paths

g = MapGraph()

list1 = ["Tokyo","New Delhi","Kuala Lumpur","Dubai","Ankara","Beijing","Seoul","Taipei","Jakarta","Islamabad"]

NewsSentiment().prefetch_news_city(list1)

for city1 in list1:
	for city2 in list1:
		g.add_road(city1,city2,random.randint(100,1000))

allpaths = g.sorted_paths_list("kuala lumpur", "tokyo")
shortest = g.shortest_path("kuala lumpur", "tokyo")
best = method2.get_best_path(g, "kuala lumpur", "tokyo")

plot_map_with_many_paths(allpaths, "C:\\Users\\aminq\\Desktop\\maps\\mapfff.html")
plot_map_with_one_path(shortest[0], "C:\\Users\\aminq\\Desktop\\maps\\mapf.html")
plot_map_with_one_path(best[0], "C:\\Users\\aminq\\Desktop\\maps\\mapff.html")



# Take care this method (do100) takes around 2 minutes running time
# Cause it creates 100 random graphs
"""
x = do100()
print(x)
"""