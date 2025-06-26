## Multithreading
## when to use Multi threading
### I/O bound Tasks: Tasks that spend more time waiting for I/O operations(e.g File Operations)
### Concurrent execution : When you want to imporve the throughput of your application by perfroming some actions
import threading
import time
def print_number():
    for i in range(5):
        time.sleep(2)
        print(f"Number: {i}")
def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"letter: {letter}")

## create two threads
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)


t = time.time()
## start the thread
t1.start()
t2.start()


## wait for the entire thread to complete
t1.join()
t2.join()
print_number()
print_letter()
finished_time = time.time() - t
print(finished_time)