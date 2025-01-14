import multiprocessing
import time


def print_num():
    """Print numbers from 0 to 9 with a delay of 1 second between each."""
    for i in range(10):
        time.sleep(1)
        print(i)


def print_letter():
    """Print each letter of 'Python' with a delay of 1.5 seconds between each."""
    for letter in "Python":
        time.sleep(1.5)
        print(letter)


if __name__ == '__main__':
    # Create processes for each task
    p1 = multiprocessing.Process(target=print_num)
    p2 = multiprocessing.Process(target=print_letter)

    # Start timer
    start_time = time.time()

    # Start the processes
    p1.start()
    p2.start()

    # Wait for processes to complete
    p1.join()
    p2.join()

    # Calculate total time taken
    elapsed_time = time.time() - start_time
    print(f"Total execution time: {elapsed_time:.2f} seconds")
