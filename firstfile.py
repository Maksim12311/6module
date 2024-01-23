
import timeit
from threading import Thread


def sequential_function():
    result = sum(range(1000000))
    return result

def parallel_function():
    results = []


    def worker(start, end):
        partial_result = sum(range(start, end))
        results.append(partial_result)

    
    threads = []
    for i in range(0, 1000000, 100000):
        thread = Thread(target=worker, args=(i, i+100000))
        threads.append(thread)
        thread.start()

    
    for thread in threads:
        thread.join()

    return sum(results)


sequential_time = timeit.timeit(sequential_function, number=1)


parallel_time = timeit.timeit(parallel_function, number=1)

print(f"Sequential Time: {sequential_time} seconds")
print(f"Parallel Time: {parallel_time} seconds")