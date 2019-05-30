from sentiment_news import NewsSentiment
import operator

def get_best_path (graph, city1, city2):

	paths = graph.sorted_paths_wrt_distances(city1, city2)
	ns = NewsSentiment()

	cities = list(graph.cities.keys())
	polarities = {}
	sentiment = []
	polarity = 0

	for each_city in cities:
		sentiment = ns.fetch_news_sentiment(each_city)
		for i in sentiment:
			polarity = polarity + i["total"]
		polarity = round((polarity/5),2)
		polarities[each_city] = polarity

	i = 0
	for each_path in paths:
		path = each_path[1]
		del path [0]
		del path [len(path)-1]
		polarity = 0
		for city in path:
			polarity = polarity + polarities[city]
		paths[i] = paths[i] + (polarity,)
		i = i + 1

	#for loop to add another column to paths containing mixed score
	score = 0
	i = 0
	d0 = graph.edges [graph.cities_indices[city1]] [graph.cities_indices[city2]]

	for each_path in paths:
		score = ( d0 / each_path [0] ) + ( each_path[2] / 100 )
		#score =  0.5 * (each_path [0] + (-100 * each_path[2]))
		paths [i] =  paths[i] + (score,)
		i = i + 1

	sorted_paths = sorted(paths, key=operator.itemgetter(3))
	
	sorted_paths[len(sorted_paths)-1][1].append(city2)
	best_path = [city1] + sorted_paths[len(sorted_paths)-1][1]
	best_distance = sorted_paths[len(sorted_paths)-1][0]
	best = [best_path, best_distance]

	ns.showWordStatistics()

	return best