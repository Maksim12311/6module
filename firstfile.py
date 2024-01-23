import time
from threading import Thread

def get_thread(thread_name):
	time.sleep(1)
	print(f'The flow {thread_name} started!')

list = ['a','b','c','d','e']
threads = [Thread(target = get_thread,args = (i,)) for i in list]

for t in threads:
	t.start()

for t in threads:
	t.join()