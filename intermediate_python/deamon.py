import threading
import time

# as you know daemons are running in the background, eventually are listening
# or doing their thing and then are terminated in the process or in the end
# of the program


path = "text.txt"
text = ""


def readFile():
    global path, text
    while True:
        with open(path,"r") as f:
            text = f.read()
        time.sleep(3)


def printLoop():
    for x in range(30):
        print(text)
        time.sleep(1)


if __name__ == '__main__':
    t1 = threading.Thread(target=readFile, daemon=True)
    t2 = threading.Thread(target=printLoop)

    t1.start()
    t2.start()
