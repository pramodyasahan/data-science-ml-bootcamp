import time
from concurrent.futures import ProcessPoolExecutor


def print_number(num):
    time.sleep(2)
    return f"number is {num}"


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if __name__ == '__main__':
    t = time.time()
    with ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(print_number, numbers)

    for result in results:
        print(result)

    t1 = time.time() - t
    print(f"Time taken: {t1}")
