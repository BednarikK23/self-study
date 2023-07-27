# https://docs.python.org/3/library/queue.html?highlight=queue#module-queue
import queue

# ques have many advantages,
q = queue.Queue(maxsize=10)

# most usful functions:
q.empty()
q.put(10, block=True, timeout=None) # these args are default, blocks if necessary - useful for use with threads
q.size()
q.full()
q.get(block=True, timeout=None) # these args default, block if necessary until item is available - threads
# q.join() - Blocks until all items in the queue have been gotten and processed.

# actualy stack
s = queue.LifoQueue(maxsize=10)

# if maxsize is <= 0 -> max size = infinity...
p = queue.PriorityQueue(maxsize=0)
# sorted ascending...
p.put((2, "a"))  # we can do tuples and add priority as first elem of tuple
p.put((3, "b"))
p.put((1, "z"))
p.get(), p.get(), p.get()



if __name__ == '__main__':
    pass

