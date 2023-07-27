import threading


event = threading.Event()


def foo():
    print("Waiting for event to trigger...")
    event.wait()

    print("Performing action XYZ now...")

if __name__ == '__main__':
    t1 = threading.Thread(target=foo)
    t1.start()

    x = input("Do you want to trigger event? (y/n)\n")
    if x == "y":
        event.set()
