import threading
import datetime
import logging
import time

first = threading.Thread(target=logging.type_300)

def time_now():
	for j in range(0,300):
		now = datetime.datetime.now()
		print(now)
		time.sleep(0.1)
	

second = threading.Thread(target=time_now)

first.start()
second.start()
first.join()
second.join()
