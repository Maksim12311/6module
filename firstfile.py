

import requests
import threading
import time

def get_html(link):
    response = requests.get(link)
    html_content = response.text
   

start_time = time.time()


links = ["https://example.com", "https://example.org", "https://example.net", "https://example.edu", "https://example.gov"]
for link in links:
    get_html(link)

sequential_time = time.time() - start_time
start_time = time.time()


threads = []
for link in links:
    thread = threading.Thread(target=get_html, args=(link,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

parallel_time = time.time() - start_time

print(f"Sequential Time: {sequential_time} seconds")
print(f"Parallel Time: {parallel_time} seconds")