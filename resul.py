import time
import threading
import sys

class Semaphore(object):
    def _init_(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.valve = initial

    def up(self):
        with self.lock:
            self.valve += 1
            self.lock.notify()  # Notify one waiting thread

    def down(self):
        with self.lock:
            while self.valve == 0:
                self.lock.wait()
            self.valve -= 1

class ChopStick(object):
    def _init_(self, number):
        self.number = number
        self.user = None
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):
        with self.lock:
            while self.taken:
                self.lock.wait()
            self.user = user
            self.taken = True
            sys.stdout.write(f"Filósofo [{user+1}] toma el palillo: {self.number+1}\n")
            self.lock.notify_all()

    def drop(self, user):
        with self.lock:
            while not self.taken:
                self.lock.wait()
            self.user = None
            self.taken = False
            sys.stdout.write(f"Filósofo [{user+1}] deja el palillo: {self.number+1}\n")
            self.lock.notify_all()

class Philosopher(threading.Thread):
    def _init_(self, number, left, right, butler):
        super()._init_()
        self.number = number
        self.left = left
        self.right = right
        self.butler = butler

    def run(self):
        for _ in range(5):  # Adjusted to think and eat multiple times
            self.butler.down()
            sys.stdout.write(f"Filósofo {self.number + 1} piensa\n")
            time.sleep(0.1)
            self.left.take(self.number)
            sys.stdout.write(f"Filósofo {self.number + 1} come\n")
            time.sleep(0.1)
            self.right.drop(self.number)
            self.butler.up()
        sys.stdout.write(f"Filósofo [{self.number + 1}] termina de pensar y comer\n")

def main():
    n = 5
    butler = Semaphore(n - 1)
    chopsticks = [ChopStick(i) for i in range(n)]
    philosophers = [Philosopher(i, chopsticks[i], chopsticks[(i + 1) % n], butler) for i in range(n)]
    
    for p in philosophers:
        p.start()
    
    for p in philosophers:
        p.join()  # Ensure all philosophers finish before the program exits

if _name_ == "_main_":
    main()
