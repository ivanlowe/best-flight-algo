import gmplot

cities_lats, cities_lons = zip(*
[( 35.689487 , 139.691711) 
,( 28.613939, 77.209023)
,( 3.139003, 101.686852)
,( 25.204849, 55.270782)
,( 39.933365, 32.859741)
,( 39.904202, 116.407394)
,( 37.566536, 126.977966)
,( 25.032969, 121.565414)
,( 1.352083, 103.819839)
,( 33.684422, 73.047882)])

gmap = gmplot.GoogleMapPlotter(23, 86, 4)
gmap.scatter( cities_lats, cities_lons, color= 'red',size = 100000, marker = False)
gmap.apikey = "AIzaSyDwDkLHO-xUfosP6CeNGmJwQhPiTK6qyiU"
gmap.draw( "C:\\Users\\aminq\\Desktop\\maps\\map.html")