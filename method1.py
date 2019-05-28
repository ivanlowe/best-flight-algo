from shortest_path import MapGraph
from sentiment_news import NewsSentiment

def get_best_path (graph, city1, city2):

	paths = graph.sorted_paths_wrt_distances(city1, city2)
	ns = NewsSentiment()

	best_path = []
	best_distance = 0
	safe = False
	polarity = 0

	for each_path in paths:
		path = each_path[1]
		del path [0]
		del path [len(path)-1]
		for city in path:
			polarity = 0
			safe = False
			sentiment = ns.fetch_news_sentiment(city)
			for i in sentiment:
				polarity = polarity + i["total"]
			if polarity < 0:
				safe = False
				break
			else:
				safe = True
		if safe is True:
			best_path = each_path [1]
			best_distance = each_path[0]
			break

	best = [best_path, best_distance]
	return best