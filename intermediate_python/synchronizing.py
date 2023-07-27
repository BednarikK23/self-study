import threading
import time


x = 8192

# if we didnt used lock we will end up in deadlock
lock = threading.Lock()


def double():
    # need to look for x in bigger scope and change it, so using global
    global x, lock
    # locking thread
    lock.acquire()
    while x < 16384:
        x *= 2
        print(x)
        time.sleep(1)
    print("Reached maximum!")
    # releasing the thread from owning, pretty simple
    lock.release()


def halve():
    # need to look for x in bigger scope and change it, so using global
    global x, lock
    lock.acquire()
    while x > 1:
        x /= 2
        print(x)
        time.sleep(1)
    print("Reached minimum!")
    lock.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=halve)
    t2 = threading.Thread(target=double)

    t1.start()
    t2.start()
