import gmplot
import geocoder

def plot_map_with_marked_cities (cities_list, output_path, center_lat =0, center_long=0, zoom=2):
	
	cities_lats_dict  = {}
	cities_longs_dict = {}
	
	for each_city in cities_list:
		
		g = geocoder.google(each_city, key="AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU")
		latlng = g.latlng
		cities_lats_dict [each_city] = latlng[0]
		cities_longs_dict [each_city] = latlng[1]
		
		lats_tupl = tuple(cities_lats_dict.values())
		longs_tupl = tuple(cities_longs_dict.values())

	gmap = gmplot.GoogleMapPlotter(center_lat, center_long, zoom)
	gmap.scatter(lats_tupl, longs_tupl, color= 'red',size = 100000, marker = False)	
	gmap.apikey = "AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU"
	gmap.draw(output_path)


"""list1 = ["Tokyo","New Delhi","Kuala Lumpur","Dubai","Ankara","Beijing","Seoul","Taipei","Singapore","Islamabad"]
plot_map_with_marked_cities(list1, "C:\\Users\\aminq\\Desktop\\maps\\mapx.html")"""