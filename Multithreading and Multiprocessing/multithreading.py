import threading
import time


def print_num():
    for i in range(10):
        time.sleep(1)
        print(i)


def print_letter():
    for letter in "Python":
        time.sleep(1)
        print(letter)


th1 = threading.Thread(target=print_num)
th2 = threading.Thread(target=print_letter)

starting_time = time.time()
th1.start()
th2.start()

th1.join()
th2.join()

finish_time = time.time() - starting_time
print(finish_time)
