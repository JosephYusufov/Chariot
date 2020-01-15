
[logo]: https://raw.githubusercontent.com/JosephYusufov/Chariot/master/static/img/chariot-logo.png#logo
![Chariot Logo][logo]

**By The Cavalry:** Joseph Yusufov *(PM)*, William Cao *(JavaScript)*, Moody Rahman *(Backend)*, Coby Sontag *(API Implementation)* 

---
### Description
Chariot is an interactive itinerary generator that leverages the power of existing mapping utilities to generate an itinerary for its user, facilitating an efficient, convenient, and almost entirely hands-off approach to its users.   
    
Chariot allows its user to generate a detailed itinerary given the user’s location, preference, and amount of time available. This itinerary will lead the user on a path to see relevant events, landmarks, and other establishments of interest within the given parameters. 

### Setup
**NOTE:** Python3 is required to use Chariot.
1. Clone Chariot onto your machine from this repository using `$ git clone https://github.com/JosephYusufov/Chariot.git`
2. Change into the `Chariot` directory  
3. Procure MapQuest API key [here](https://developer.mapquest.com/), and paste the key into `keys/mapquest.txt`
4. Create a virtual environment using `$ python3 -m venv Chariot`
5. Activate the virtual environment:
    - If using **bash**, run `$ . Chariot/bin/activate`.
    - If using **zsh**, run `$ source Chariot/bin/activate`.
6. Install necessary packages into the virtual environment using `$ pip3 install -r ./doc/requirements.txt`. (This may take a couple of minutes)
7. Flush any existing database files with `$ rm *.db`
8. Start the Flask app using `$ python3 app.py`
9. Navigate to `127.0.0.1:5000` in a browser's URL window, and use Chariot!
 
### APIs Used
[MapQuest Place Search API](https://docs.google.com/document/d/1s0pH9YNA_j9r2tTLWS5gOZhO5M40VFZID99lQ9LsO44/edit) -- Used for the core itinerary generation function, allowing us to search for specific types of places located around an origin point.   

[MapQuest Static Maps API](https://docs.google.com/document/d/17K1jnj402jsN6UOQUFZAnnpB--rPzZkNBWme44Biltw/edit) -- Display directions, locations of points of interest, find current user location.   

[MapQuest Open Geocoding API](https://docs.google.com/document/d/1HnzToCm_MkkXAyboatQQb0dZiSAYDD04QcwS2UFF4XI/edit) -- Convert street addresses into Geographic Coordinates (e.g. Longitude and Lattitude), and vice versa.
