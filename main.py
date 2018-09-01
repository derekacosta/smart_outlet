import urequests, machine, time

pin = machine.Pin(15, machine.Pin.OUT)

while True:
	try:
		time.sleep(5)
		response = urequests.get('https://plant-lights.firebaseio.com/plant-lights/lights.json').json()
		if response == 'ON':
			pin.on()
			print('on')
		else:
			pin.off()
			print('off')
	except OSError:
		pass
