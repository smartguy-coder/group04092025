import threading
import time


# def worker(num):
#     print(555)
#     print(f"Worker {num}")
#     return (f"Worker {num}")
#
# threads = []
#
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i, ))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
number = 0

def do_job(num, second_arg=None):
    for i in range(50):
        global number
        number += 1
        print(f'From child thread1 {num}: {i=}, {num=} {second_arg=}')
        time.sleep(0.8)
        print(number)

def do_job2(num, second_arg=None):
    for i in range(50):
        global number
        number += 1
        print(f'From child thread2 {num}: {i=}, {num=} {second_arg=}')
        time.sleep(1)
        print(number)

thread1 = threading.Thread(target=do_job, args=(2, ), kwargs={"second_arg": 25})
thread2 = threading.Thread(target=do_job2, args=(50, ), kwargs={"second_arg": 40})
thread1.start()
thread2.start()

for i in range(100):
    print(f'From main thread: {i=} ')
    time.sleep(0.3)

