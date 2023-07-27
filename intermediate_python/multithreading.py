# https://docs.python.org/3/library/threading.html?highlight=threading#module-threading

import threading


def helloworld():
    print("Hello world!")


def foo():
    for _ in range(100):
        print("f")


def bar():
    for _ in range(100):
        print("u")


if __name__ == '__main__':
    # we define new object of the Thread class:
    # we pass worker function to the thread, we are not calling the function we
    # are just referring to it not calling it, so we do not add () after name.
    t1 = threading.Thread(target=helloworld)
    t1.start()

    t2 = threading.Thread(target=foo)
    t3 = threading.Thread(target=bar)

    t2.start()
    t3.start()
    # every thread that is running is running from main thread that is used by this program itself

    # if i dont want to continue until some thread is done i can use join and wait for that thread
    t4 = threading.Thread(target=bar)
    t4.start()
    t4.join()
