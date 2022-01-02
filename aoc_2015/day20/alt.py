import time

N = 29000000
limiter = int(N / 10)

time_start = time.perf_counter()

house = [0] * limiter

print(len(house))

for i in range(1,limiter):
    for j in range(i, limiter, i):
        house[j] += i * 10

print(house[-10:])

time_end = time.perf_counter()
print(f"Execution total: {time_end-time_start:.4f} seconds")