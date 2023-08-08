import time
import random

def sequential_access(data):
    sum = 0
    for value in data:
        sum += value
    return sum

def random_access(data):
    sum = 0
    indices = list(range(len(data)))
    random.shuffle(indices)
    for i in indices:
        sum += data[i]
    return sum

# Create a large array
data = [i for i in range(1, 10000001)]

# Measure time for sequential access
start_time = time.time()
sequential_access(data)
sequential_duration = time.time() - start_time

# Measure time for random access
start_time = time.time()
random_access(data)
random_duration = time.time() - start_time

print(f"Time for sequential access: {sequential_duration:.6f} seconds")
print(f"Time for random access: {random_duration:.6f} seconds")
