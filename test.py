import threading

def task(num):
    count = 0
    for i in range(num):
        count += 1
    print(count)


nums = [100, 1000, 10000]

for num in nums:
    t = threading.Thread(target=task, args=(num,))
    t.start()