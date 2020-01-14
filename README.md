
[logo]: https://raw.githubusercontent.com/JosephYusufov/Chariot/master/static/img/chariot-logo.png#logo
![Chariot Logo][logo]

**By The Cavalry:** Joseph Yusufov *(PM)*, William Cao *(JavaScript)*, Moody Rahman *(Backend)*, Coby Sontag *(API Implementation)* 

---
### Description
Chariot is an interactive itinerary generator that leverages the power of existing mapping utilities to generate an itinerary for its user, facilitating an efficient, convenient, and almost entirely hands-off approach to its users.   
    
Chariot allows its user to generate a detailed itinerary given the user’s location, preference, and amount of time available. This itinerary will lead the user on a path to see relevant events, landmarks, and other establishments of interest within the given parameters. 

### Usage: 
**NOTE:** Python3 is required to use Chariot.
1. Clone Chariot onto your machine from this repository using `$ git clone https://github.com/JosephYusufov/Chariot.git`
2. Change into the `Chariot` directory  
3. Create a virtual environment using `$ python3 -m venv Chariot`
4. Activate the virtual environment:
    - If using **bash**, run `$ . Chariot/bin/activate`.
    - If using **zsh**, run `$ source Chariot/bin/activate`.
5. Install necessary packages into the virtual environment using `$ pip3 install -r ./doc/requirements.txt`. (This may take a couple of minutes)
6. Initialize the database with `$ python3 db_init.py`
7. Start the Flask app using `$ python3 app.py`
8. Navigate to `127.0.0.1:5000` in a browser's URL window, and use Chariot!
 
### APIs (Working List)
[MapQuest Place Search API](https://docs.google.com/document/d/1s0pH9YNA_j9r2tTLWS5gOZhO5M40VFZID99lQ9LsO44/edit)  
[MapQuest Statuc Maps API](https://docs.google.com/document/d/17K1jnj402jsN6UOQUFZAnnpB--rPzZkNBWme44Biltw/edit)  
[MapQuest Open Geocoding API](https://docs.google.com/document/d/1HnzToCm_MkkXAyboatQQb0dZiSAYDD04QcwS2UFF4XI/edit)
