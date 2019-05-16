# You have been assigned to develop a system to help the end user to find the best flight to use when there is
# no direct flight available.
# The system will recommend the end user the best flight only based on route and political sentiment of the country.
# The best flight does not necessarily base on the shortest route but also considering the political situation each
# country the flight transited.
# Please note that there is no price of ticket involved in this recommendation system.


# Load instance of Flight recommender class
import flight_recommender as flt

# Main program
if __name__ == '__main__':
    flt.getBestFlight("KL", "New York")
