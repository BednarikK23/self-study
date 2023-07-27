import threading
import time


semaphore = threading.BoundedSemaphore(value=5)


def access(thread_number):
    print("{} is trying to access".format(thread_number))
    # we will try to acquire the semaphore ->
    # if we havent have 5 accesses already we will be granted access to the resource
    semaphore.acquire()
    print("{} was granted access!".format(thread_number))
    time.sleep(10)
    semaphore.release()


if __name__ == '__main__':
    for thread_number in range(1, 11):
        # this is how we will pas arguments to the work function
        # args takes tuple, so even if there is only one argument it has to
        # be written as tuple... ...like this:
        t = threading.Thread(target=access, args=(thread_number,))
        t.start()
        time.sleep(1)
