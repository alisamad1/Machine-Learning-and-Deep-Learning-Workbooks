## Allows you to run that processes in parallel
## CPU bound tasks:- Tasks that are heavy on CPU usage )eg mathematical computation , data computing etc
## parallele execution:- Multiple cores of the cpu
import multiprocessing
import time
def square_name():
    for i in range(5):
        time.sleep(1)
        print(f"Square is: {i*i}")
def cube_number():
    for i in range(5):
        time.sleep(2)
        print(f"cube is {i*i*i}")

if __name__ == "__main__":
    ## Create 2 processes
    p1 = multiprocessing.Process(target=square_name)
    p2= multiprocessing.Process(target=cube_number)
    t = time.time()
    ## start the process
    p1.start()
    p2.start()
    ## wait for the process to complete
    p1.join()
    p2.join()
    finished_time = time.time() - t
    print(finished_time)