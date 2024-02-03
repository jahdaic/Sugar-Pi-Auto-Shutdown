#!/usr/bin/python

import os
import time
from pisugar import *

conn, event_conn = connect_tcp('pizero2.local')
pi_sugar_server = PiSugarServer(conn, event_conn)
disconnected_time = 0;

while True:
	power = pi_sugar_server.get_battery_power_plugged()

	if power and disconnected_time:
		disconnected_time = 0
		# print('Power Reconnected')

	if not power and not disconnected_time:
		disconnected_time = time.time()
		# print('Power Disconnected')

	if disconnected_time and time.time() - disconnected_time >= 30:
		os.system('sudo shutdown now')

	time.sleep(10)
