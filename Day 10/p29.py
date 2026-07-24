# Process : An independent program with its own memory space.
# 1. Heavy Weight
# 2. Seperate memory 
# 3. Communication is harder

# Thread : A lightweight unit of execution within a process.
# Lighweight
# Shared Memory 
# Communication is simpler

import time

# I/O Bound Task 
def download_file(url):
    print(f"Starting download from {url}")
    time.sleep(2)

    return f"Downloaded {url}"

# CPU-bound task
def calculate_prime(n):
    count = 0 
    num = 2

    while count < n:
        is_prime = True
        for i in range(2, int(num ** 5))
        