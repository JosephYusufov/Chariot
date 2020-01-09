
[logo]: https://raw.githubusercontent.com/JosephYusufov/Chariot/master/static/img/chariot-logo.png#logo
![Chariot Logo][logo]

**By The Cavalry:** Joseph Yusufov *(PM)*, William Cao *(JavaScript)*, Moody Rahman *(Backend)*, Coby Sontag *(API Implementation)* 

---
### Description
Generate a detailed itinerary given the user’s location, preference, and amount of time available. This itinerary will lead the user on a path to see relevant events, landmarks, and other establishments of interest within the given parameters. 

### Usage: 
**NOTE:** Python3 is required to use Chariot.
- Clone Chariot onto your machine from this repository using `$ git clone https://github.com/JosephYusufov/Chariot.git`
- Change into the `Chariot` directory  
- Create a virtual environment using `$ python3 -m venv Chariot`
- Activate the virtual environment:
    - If using **bash**, run `$ . Chariot/bin/activate`.
    - If using **zsh**, run `$ source Chariot/bin/activate`.
- Install necessary packages into the virtual environment using `$ pip3 install -r ./doc/requirements.txt`. (This may take a couple of minutes)
- Initialize the database with `$ python3 db_init.py`
- Start the Flask app using `$ python3 app.py`
- Navigate to `127.0.0.1:5000` in a browser's URL window, and use Chariot!
 
