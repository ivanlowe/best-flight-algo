import random
import operator

class City:
	"""City objects are used as vertices in the MapGraph class."""
	
	def __init__(self, n):
		self.name = n

 
class MapGraph:
	"""MapGraph is a class for constructing weighted undirected graphs using cities as vertices."""

	def __init__ (self):
		self.cities = {}
		self.edges  = []
		self.adj_list = {}
		self.cities_indices = {}
	

	def add_road(self, city_x, city_y, distance):
		"""To construct a new graph add all roads between cities"""

		city_x = city_x.lower().strip()
		city_y = city_y.lower().strip()

		if city_x == city_y:
			return
		if city_x not in self.cities:
			new_city_x = City (city_x)
			self.cities[new_city_x.name] = new_city_x
			self.adj_list[new_city_x.name] = []
			for row in self.edges:
				row.append(0)
			self.edges.append([0] * (len(self.edges)+1))
			self.cities_indices[new_city_x.name] = len(self.cities_indices)

		if  city_y not in self.cities:
			new_city_y = City (city_y)
			self.cities[new_city_y.name] = new_city_y
			self.adj_list[new_city_y.name] = []
			for row in self.edges:
				row.append(0)
			self.edges.append([0] * (len(self.edges)+1))
			self.cities_indices[new_city_y.name] = len(self.cities_indices)

		if city_y not in self.adj_list[city_x]:
			self.adj_list[city_x].append(city_y)
		if city_x not in self.adj_list[city_y]:
			self.adj_list[city_y].append(city_x)
		
		self.edges[self.cities_indices[city_x]][self.cities_indices[city_y]] = distance
		self.edges[self.cities_indices[city_y]][self.cities_indices[city_x]] = distance



	def find_all_paths (self, city_x, city_y, path = []):
		"""This method is used as a backend method to support other methods in the class"""

		city_x = city_x.lower().strip()
		city_y = city_y.lower().strip()
		
		path = path + [city_x]
		
		if city_x not in self.cities:
			return []
		
		if city_x == city_y:
			return [path]
		
		paths = []
		newpaths = []
		
		for city in self.adj_list[city_x]:
			if city not in path:
				newpaths = self.find_all_paths(city, city_y, path)
			for newpath in newpaths:
				if ( len(newpath)<4 or len(newpath)>5):
					pass
				else:
					paths.append(newpath)
		return paths
		

	def all_possible_paths (self, city_x, city_y):
		"""
		To get all possible paths between 2 cities in the driver code.
		It restricts the possible paths to be transitting through 2-3 cities only
		"""

		all_possible_paths = self.find_all_paths(city_x, city_y)
		all_possible_paths = [list(t) for t in set(tuple(element) for element in all_possible_paths)]
		return all_possible_paths

 
	def shortest_path (self, city_x, city_y):
		"""This method returns a list of (shortest path index, shortest path, distance of shortest path)"""

		all_paths = self.all_possible_paths(city_x, city_y)
		shortets_value = 10**9
		shortest_path = []

		for each_path in all_paths:
			path_distance = 0
			for i in range(0,len(each_path)-1):
				path_distance += self.edges[self.cities_indices[each_path[i]]][self.cities_indices[each_path[i+1]]]
			if path_distance < shortets_value:
				shortets_value = path_distance
				shortest_path = each_path

		if shortets_value == 10**9:
			shortets_value = 0
		return [shortest_path, shortets_value]

	def sorted_paths_wrt_distances (self, city1, city2):
		paths = self.all_possible_paths(city1, city2)
		path_distance = 0
		path_list = []
		distance_list = []
		
		for each_path in paths:
			path_distance = 0
			for i in range(0,len(each_path)-1):
				path_distance += self.edges[self.cities_indices[each_path[i]]][self.cities_indices[each_path[i+1]]]
			path_list.append(each_path)
			distance_list.append(path_distance)

		paths_with_distances = list(zip(distance_list, path_list))
		sorted_list = sorted(paths_with_distances, key=operator.itemgetter(0))

		return sorted_list


	def print_graph(self):
		"""This method prints the adjacency matrix"""

		print("\t\t\t",end="")
		for city, i in self.cities_indices.items():
			print(city + '\t', end='')
		print()
		for city, i in self.cities_indices.items():
			print(city + '\t\t', end='')
			for j in range(len(self.edges)):
				print(self.edges[i][j], end='\t\t')
			print(' ')


"""
DRIVER CODE
This is a randomized grapgh between 10 different states 
and then finding shortest path between india and paskitan
"""



"""g = MapGraph()
list1 = ["Japan","India","Malaysia","UAE","Turkey","China","SKorea","Taiwan","Singapore","Pakistan"]
for city1 in list1:
	for city2 in list1:
		g.add_road(city1,city2,random.randint(100,1000))
g.print_graph()
print()
paths = g.all_possible_paths("India","Pakistan")
for path in paths:
	print(path)
shortest = g.shortest_path("India","Pakistan")
paths = g.sorted_paths_wrt_distances("india","pakistan")
print("\n")
print(paths)
print("\n")"""
