from geopy.geocoders import Nominatim
from math import radians, cos, sin, atan, sqrt, pi, acos
import requests

# -----------------------
# Variables declaration
# -----------------------
cityList = ["Tokyo", "New Delhi", "Kuala Lumpur", "Dubai", "Ankara", "Beijing", "Seoul", "Taipei", "Singapore",
            "Islamabad"]
cityCoordinates = []
# anotherCitiesList = ["Boston", "Santa Fe", "London", "Bangkok", "Miami", "Vienna", "Oslo", "Johannesburg",
# "Copenhagen", "Melbourne"]


""" -----------------------------------------------------------------
Converts city names from the given list to latitudes and longitudes.
----------------------------------------------------------------- """
def convertCityToCoordinates(city):
	"""geolocator = Nominatim(user_agent="flight-route-planner-fsktm")
	location = geolocator.geocode(city)
	locationArray = [location.latitude, location.longitude]
	return locationArray"""
	params = {
		"q":city,
		"format":"json"
	}
	req = requests.get("https://nominatim.openstreetmap.org/search", params)
	data = req.json()
	lat = data[0]["lat"];
	lon = data[0]["lon"];
	return [float(lat), float(lon)]


""" --------------------------------------------------------------------------------
Stores every single latitude and longitude value of each city for future reference.
Useful for quick coordinates retrieval.
-------------------------------------------------------------------------------- """
def saveCoordinates():
	# index = 0   # For incremeting purposes
	for ind_city in cityList:
		exact_coor = convertCityToCoordinates(ind_city)
		print(exact_coor)
		cityCoordinates.append(exact_coor)

	return cityCoordinates


""" ------------------------------------------------------------------------------------------------------------
Obtains the geodesic distance between 2 cities given their respective latitudes and longitudes.
The geodesic distance between 2 cities is calculated using the special case of the Vincenty formula for an 
ellipsoid with equal major and minor axes.
The function will generate a matrix such that every value (V)ij represents the distance between cities i and j.
------------------------------------------------------------------------------------------------------------ """
def getDistance(lat1, lng1, lat2, lng2):
	authalic_earth_radius = 6371
	a = cos(radians(lat1))
	b = cos(radians(lat2))
	c = sin(radians(lat1))
	d = sin(radians(lat2))
	lng_diff = radians(lng2 - lng1)
	central_angle = atan(sqrt((b*sin(lng_diff))**2 + (a*d - b*c*cos(lng_diff))**2) / (c*d + a*b*cos(lng_diff)))
	distance = authalic_earth_radius*central_angle
	return int(distance)   # returns distance to the nearest integer in km


def distance_on_unit_sphere(lat1, long1, lat2, long2):
	# Convert latitude and longitude to
	# spherical coordinates in radians.
	degrees_to_radians = pi / 180.0

	# phi = 90 - latitude
	phi1 = (90.0 - lat1) * degrees_to_radians
	phi2 = (90.0 - lat2) * degrees_to_radians

	# theta = longitude
	theta1 = long1 * degrees_to_radians
	theta2 = long2 * degrees_to_radians

	# Compute spherical distance from spherical coordinates.

	# For two locations in spherical coordinates
	# (1, theta, phi) and (1, theta, phi)
	# cosine( arc length ) =
	#    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
	# distance = rho * arc length

	_cos = (sin(phi1) * sin(phi2) * cos(theta1 - theta2) + cos(phi1) * cos(phi2))
	arc = acos(_cos)

	# Remember to multiply arc by the radius of the earth
	# in your favorite set of units to get length.
	return arc * 6371

""" -----------------------------------------------------------------
Converts city names from the given list to latitudes and longitudes.
----------------------------------------------------------------- """
def getDistanceMatrix():
	initMatrix = []
	cityCopy = cityCoordinates.copy()

	for city1 in cityCoordinates:
		for city2 in cityCopy:
			dist_diff = getDistance(city1[0], city1[1], city2[0], city2[1])
			initMatrix.append(dist_diff)

	finalMatrix = stackMatrix(initMatrix)
	return finalMatrix


""" -----------------------------------------------------------------
Converts the 1-D distance matrix into a 2-D stacked matrix.
----------------------------------------------------------------- """
def stackMatrix(mat):
	size = len(cityCoordinates)
	tempMat = []
	stackedMatrix = [[] for h in range(size)]
	counter = 0

	# Transforming a 1-D matrix of size 100 into a 10x10 matrix
	for i in range(int(len(mat)/size)):
		for j in range(size):
			tempMat.append(mat[j + counter])
		counter += j
		stackedMatrix[i] = tempMat
		tempMat = []   # Empty temporary matrix
		counter += 1   # To ensure the next ((multiple of 10)+1)th element is not left out when j resets to zero

	return stackedMatrix
