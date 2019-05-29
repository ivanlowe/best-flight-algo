from shortest_path import MapGraph
import method1
import method2
import random
from sentiment_news import NewsSentiment

g = MapGraph()

list1 = ["Tokyo","New Delhi","Kuala Lumpur","Dubai","Ankara","Beijing","Seoul","Taipei","Singapore","Islamabad"]

NewsSentiment().prefetch_news_city(list1)

for city1 in list1:
	for city2 in list1:
		g.add_road(city1,city2,random.randint(100,1000))


print(method1.get_best_path(g, "kuala lumpur", "tokyo"))
print("\n")
print(method2.get_best_path(g, "kuala lumpur", "tokyo"))