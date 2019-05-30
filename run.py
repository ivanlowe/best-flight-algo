from shortest_path import MapGraph
import method1
import method2
import random
from sentiment_news import NewsSentiment
from do100trial import do100
import plot_paths
import os
from cache import Cache
import city_mapping
import mark_cities

from flask import Flask, request, render_template
import json

city_coord = Cache("city_coordinates.json")

cities = ["Kuala Lumpur", "Kota Kinabalu", "Tokyo", "Jakarta", "Bangkok", "Beijing", "Dubai", "Paris", "London", "New York", "Moscow"]

print("Fetching news for each cities...")
NewsSentiment().prefetch_news_city(cities)

print("Plotting cities on map...")
if not os.path.exists("static\\city_on_map.html"):
    mark_cities.plot_map_with_marked_cities(cities, "static\\city_on_map.html")

print("Building graph for cities...")
graphCities = MapGraph()

print("Getting coordinates for each cities...")

for city in cities:
    print("Acquiring coordinates for ", city, "...")
    k_city = city.replace(" ", "_").lower()

    if city_coord.contains(k_city):
        print("Coordinate exist!")
    else:
        coordinate = city_mapping.convertCityToCoordinates(city)
        print(city, " is at ", coordinate)
        city_coord.set(k_city, coordinate)

for fromCity in cities:
    for toCity in cities:
        k_from = fromCity.replace(" ", "_").lower()
        k_to = toCity.replace(" ", "_").lower()

        distance = None
        if fromCity == toCity:
            print("Same origin and destination. Distance = 0")
            distance = 0
        else:
            c_from = city_coord.get(k_from)
            c_to = city_coord.get(k_to)
            distance = city_mapping.distance_on_unit_sphere(c_from[0], c_from[1], c_to[0], c_to[1])
            distance = int(distance)

            print(fromCity, " to ", toCity, " is ", distance)

        graphCities.add_road(fromCity, toCity, distance)

print("Done! Starting RESTful API...")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", cities=cities)

@app.route("/cities")
def returnCities():
    return json.dumps(cities)

@app.route("/getroute")
def getRoute():
    _from = request.args.get("from")
    _to = request.args.get("to")

    result = {}

    if (not _from in cities) or (not _to in cities):
        result["status"] = "invalid"
        result["mesage"] = "Either " + _from + " or " + _to + " is not available!";
        return json.dumps(result)

    _from = _from.lower()
    _to = _to.lower()

    shortest_1 = graphCities.shortest_path(_from, _to)
    shortest_2 = method2.get_best_path(graphCities, _from, _to)
    print(shortest_1, shortest_2)
    plot_paths.plot_map_with_one_path(shortest_1[0], "static\\result_m1.html")
    plot_paths.plot_map_with_one_path(shortest_2[0], "static\\result_m2.html")

    result = {
        "status":"success",
        "results": [
            "result_m1.html",
            "result_m2.html"
        ],
        "probability":1/graphCities.posible_path_count
    }

    return json.dumps(result)

app.run()