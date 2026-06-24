import requests
import threading
import time
import keyboard





#Main Loop
print("Press Ctrl+C to exit.")

try:
    while True:
        
        #ISS Position
        response = requests.get("http://api.open-notify.org/iss-now.json")
        position = response.json()['iss_position']
        latitude = position['latitude']
        longitude = position['longitude']

        #Display
        print("Latitude:", latitude)
        print("Longitude:", longitude)
        time.sleep(1)

#Quit
except KeyboardInterrupt:
    print("Goodbye!")