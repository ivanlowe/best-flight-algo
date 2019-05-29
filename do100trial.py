from method1 import get_best_path
from shortest_path import MapGraph
import method1
import method2
import random
from sentiment_news import NewsSentiment

def do100():
	list1 = ["Tokyo","New Delhi","Kuala Lumpur","Dubai","Ankara","Beijing","Seoul","Taipei","Singapore","Islamabad"]
	NewsSentiment().prefetch_news_city(list1)
	results_method1 = []
	results_method2 = []
	diff = []
	m1 = m2 = e = 0
	for i in range(100):
		g = MapGraph()
		for city1 in list1:
			for city2 in list1:
				g.add_road(city1,city2,random.randint(100,1000))
		
		x = method1.get_best_path(g, "kuala lumpur", "tokyo")
		y = method2.get_best_path(g, "kuala lumpur", "tokyo")
		d = x[1] - y[1]
		results_method1.append(x[1])
		results_method2.append(y[1])
		diff.append(d)
		if d > 0:
			m2 = m2 + 1
		elif d is 0:
			e = e + 1
		else:
			m1 = m1 + 1

	# m1 is the no. of times method 1 beats method 2
	# m2 is the no. of times method 2 beats method 1
	# e is the no. of times method 1 ties with method 2
	
	return [m1,m2,e]