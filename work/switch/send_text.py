import RPi.GPIO as GPIO
import smtplib, time, configparser
import Adafruit_DHT

# setup switch
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)

# setup dht11
sensor = 11
pin = 4

def get_config_values():
	config = configparser.ConfigParser()
	config.read('send_text.cfg') 
	return (config['main']['account'], config['main']['password'], config['main']['target'], config['main']['server'], config['main']['port'])

def send_text(msg):
	print("Connecting...")
	server = smtplib.SMTP( mailserver , int(port))
	print("Logging in")
	server.starttls()
	server.login(account, password)
	msg = """
	""" + msg
	print("Sending...")
	server.sendmail(account, myPhone, msg)

if __name__ == "__main__":
	account, password, myPhone, mailserver, port = get_config_values()
	while 1:
		inp = GPIO.input(17)
		if inp:
			humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
			message = "Switch Pressed!"
			temperature = temperature * 9/5.0 + 32
			message += 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
			send_text(message)
		else:
			print ("Switch NOT pressed.")
			time.sleep(1)
