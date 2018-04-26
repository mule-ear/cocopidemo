## Simple demo for the RPi written in Python

The Python script work/switch/send_text.py just checks the status of the switch. When the switch is pressed, it reads the DHT11 and sends a text to the phone number it gets from the config file.

* Requires python 3
* and the Adafruit DHT11 library installed https://github.com/adafruit/DHT-sensor-library.git

If you want to run the daemon, install the etc_systemd_system-start_test.service file in (as you may have guessed by the name) /etc/systemd/system and enable it with `systemctl enable`

### Make sure that everything points to the right place:
* start_test.service contains the path to the bash script
* The bash script contains the path to the python script


send_text.py gets the account info from send_text.cfg. Where:

* account = the name of the email account you'll be sending from e.g. user@email.com
* password = the email account password
* target = the phone's email address - varies by carrier
* server = the smtp address of the mail server
* port = the port you want to use (25 or 587) 
