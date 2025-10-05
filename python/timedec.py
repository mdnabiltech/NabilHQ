import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        t = end - start
        print(f"This function took {t:.5f}{" of a" if t < 1 else ""} second{"s" if t > 1 else ""} to run")
        return t
    return wrapper

@timer
def slow_sum(num):
    sum = 0
    for i in range(num):
        sum += i
    return sum

n = int(input(f"Number: "))
print(slow_sum(n))
