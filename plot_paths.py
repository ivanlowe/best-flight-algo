import gmplot
import geocoder
import random

def plot_map_with_many_paths (path_list, output_dir, center_lat =0, center_long=0, zoom=2):
	gmap = gmplot.GoogleMapPlotter(center_lat, center_long, zoom)
	gmap.apikey = "AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU"

	cities_lats_dict  = {}
	cities_longs_dict = {}
	fetched_cities = []
	path_lats = []
	path_longs = []

	for each_path in path_list[:10]:
		path_lats = []
		path_longs = []
		for each_city in each_path:
			if each_city not in fetched_cities:
				g = geocoder.google(each_city, key="AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU")
				latlng = g.latlng
				cities_lats_dict [each_city] = latlng[0]
				cities_longs_dict [each_city] = latlng[1]
				fetched_cities.append(each_city)
			gmap.scatter((cities_lats_dict [each_city],), (cities_longs_dict [each_city],), color= 'red',size = 100000, marker = False)
			path_lats.append(cities_lats_dict[each_city])
			path_longs.append(cities_longs_dict[each_city])
		color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
		gmap.plot(tuple(path_lats), tuple(path_longs), color, edge_width = 3.0)

	g = geocoder.google(path_list[0][0], key="AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU")
	latlng = g.latlng
	for i in range(10):
		gmap.scatter( (latlng[0],) , (latlng[1],), color= 'black',size = 100000, marker = False)

	g = geocoder.google(path_list[0][len(path_list[0]) - 1], key="AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU")
	latlng = g.latlng
	for i in range(10):
		gmap.scatter( (latlng[0],) , (latlng[1],), color= 'black',size = 100000, marker = False)

	gmap.draw(output_dir)





def plot_map_with_one_path (path, output_dir, center_lat =0, center_long=0, zoom=2):
	
	pathx = path
	gmap = gmplot.GoogleMapPlotter(center_lat, center_long, zoom)
	gmap.apikey = "AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU"
	
	path_lats = []
	path_longs = []
	
	for each_city in pathx:
		g = geocoder.google(each_city, key="AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU")
		latlng = g.latlng
		gmap.scatter( (latlng[0],) , (latlng[1],), color= 'red',size = 100000, marker = False)
		path_lats.append(latlng[0])
		path_longs.append(latlng[1])

	g = geocoder.google(pathx[0], key="AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU")
	latlng = g.latlng
	for i in range(10):
		gmap.scatter( (latlng[0],) , (latlng[1],), color= 'black',size = 100000, marker = False)

	g = geocoder.google(pathx[len(path) - 1], key="AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU")
	latlng = g.latlng
	for i in range(10):
		gmap.scatter( (latlng[0],) , (latlng[1],), color= 'black',size = 100000, marker = False)

	gmap.plot(tuple(path_lats), tuple(path_longs), "blue", edge_width = 3.0)
	gmap.draw(output_dir)