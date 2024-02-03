#!/usr/bin/python

import os
import time
import argparse
from pisugar import *

conn, event_conn = connect_tcp('pizero2.local')
pi_sugar_server = PiSugarServer(conn, event_conn)
parser = argparse.ArgumentParser()
parser.add_argument('-t', '--timeout', type=int)
parser.add_argument('-r', '--rate', type=int)
args = parser.parse_args()
timeout = args.timeout or 30
rate = args.rate or 10
disconnected_time = 0;

print(timeout)

while True:
	power = pi_sugar_server.get_battery_power_plugged()

	if power and disconnected_time:
		disconnected_time = 0
		# print('Power Reconnected')

	if not power and not disconnected_time:
		disconnected_time = time.time()
		# print('Power Disconnected')

	if disconnected_time and time.time() - disconnected_time >= timeout:
		os.system('sudo shutdown now')

	time.sleep(rate)
