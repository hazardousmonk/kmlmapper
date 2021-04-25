# kmlmapper
A quick python script to import a json file with Lat/Lon data, and convert it to a KML which can be opened in Google Earth

# Use Cases
This script is great for mapping any geo-spatial data for intelligence purposes. 

# How To Use
This script will require some tweaking to suit your use case. It iterates line by line over a file (assuming that each file contains a single JSON response). You may edit that portion if you have a list of JSON responses to suit your use case.

You can easily modify the script to take a csv as an input or basically any sort file which has structured geo-spatial data. You will just have to write the appropriate parser and push it through.

In this script, we have a particular value 'thresh', or threshold which decides what the icon on the map should be. You may modify this logic to suit your requirements. 

You may also add additional KML tags as per your requirement. You can add a 'Description' for each point, that will bring up a nice card on Google Earth describing the point. 


# References
https://developers.google.com/kml/documentation/kml_tut

