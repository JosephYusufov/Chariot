import json
import urllib.request

def getRestaurant(origin,miles,matches){
      g = urllib.request.urlopen("https://www.mapquestapi.com/search/v2/radius?origin={}&radius={}&maxMatches={}&ambiguities=ignore&hostedData=mqap.ntpois|group_sic_code=?|581208&outFormat=json&key=KEY".format(origin.replace(" ","+"),miles,matches) # Some API link goes here
      places = json.loads(g.read())
      return places
}