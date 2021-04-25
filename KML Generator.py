import json



def retKML(name,latitude,longitude, thresh):
    if int(thresh) > 1000:
        security="lowConfidence"
    else:
        security="highConfidence"
    try:
        kml = (
        '<Placemark>\n'
        '<name>%s - %s</name>\n'
        '<styleUrl>#'+security+'</styleUrl>\n' 
        '<Point>\n' 
        '<coordinates>%s,%s</coordinates>\n' 
        '</Point>\n' 
        '</Placemark>\n'
        )%(name.translate({ord(i):None for i in '&'}), longitude, latitude)
        #print(kml)
        return kml
    except:
        return ''

def plotPoints():
    kmlPts = ''
    with open('complete_responses.txt', 'r') as f:
        for line in f:
            data = json.loads(line)
            try:
                
                lat = data['result']['location']['latitude']
                lon = data['result']['location']['longitude']
                name = data['result']['meta']['displayName']
                thresh = data['result']['thresh']
                kmlPts = kmlPts + retKML(name, lat, lon, thresh)
            except:
                pass
    return kmlPts

def main():
    

	
	kmlheader = '<?xml version="1.0" encoding="UTF-8"?>\
		\n<kml xmlns="http://www.opengis.net/kml/2.2">\n<Document>\
		\n<Style id="highConfidence">\
            \n<IconStyle id="highConfidenceStyle">\
                \n<scale>1.0</scale>\
                \n<heading>0.0</heading>\
                \n<Icon>\
                    \n<href>http://maps.google.com/mapfiles/ms/icons/green.png</href>\
                    \n<refreshInterval>0.0</refreshInterval>\
                    \n<viewRefreshTime>0.0</viewRefreshTime>\
                    \n<viewBoundScale>0.0</viewBoundScale>\
                \n</Icon>\
            \n</IconStyle>\
        \n</Style>\
        \n<Style id="lowConfidence">\
            \n<IconStyle id="lowConfidenceStyle">\
                \n<scale>1.0</scale>\
                \n<heading>0.0</heading>\
                \n<Icon>\
                    \n<href>http://maps.google.com/mapfiles/ms/icons/red.png</href>\
                    \n<refreshInterval>0.0</refreshInterval>\
                    \n<viewRefreshTime>0.0</viewRefreshTime>\
                    \n<viewBoundScale>0.0</viewBoundScale>\
                \n</Icon>\
            \n</IconStyle>\
        \n</Style>\n'
	kmlfooter = '</Document>\n</kml>\n'


	kmldoc=kmlheader+plotPoints()+kmlfooter
	print(kmldoc)

if __name__ == '__main__':
	main()
