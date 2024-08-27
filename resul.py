import time 
import threading
import sys
class Semaphore(object):
    def __init__(self,initial):
        self.lock =threading.condition(threading.Lock())
        self.valve=initial
        
    def up(self):
        with self.lock:
            while self.valve ==0
               self.lock.wait()
            self.valve -=1
            
    class ChopStick(object):
        def __init__(self,number):
            self.number=number
            self.user=1
            self.lock=threading.Condition(threading.Lock())
            self.taken=False
            
        def take(self,user):
            with self.lock:
                while self.token= =True:
                   self.lock.wait()
                self.user=user
                self.taken=True
                sys.stdout.write("Folosofo [%s] toma el palillo:%S\n"%(user,self,number))
                self.lock.notifyAll()
        
        def drop(self,user):
            with self.lock:
                while self.taken= =False:
                   self.lock.wait()
                self.user= -1 
                self.taken=False
                sys.stdout.write("Filosofo[%S] deja el palillo:%s\n"%(user,self.number))
                self.lock.notifyAll()
                
    class Philosofer(Threading.Thread):
        def __init__(self,number,left,right,butler):
            threading.Thread. __init__(self)
            self.number= number
            self.left= left
            self.right=right
            self.butler=butler
        
        def run(self):
            for i in range(1):
                self.butler.down()
                print("Filosofo",self.number, "piensa")
                time.sleep(0.1)
                self.left.take(self.number)
                print("Filosofo",self.number,"come")
                time.sleep(0.1)
                self.right.drop(self.number)
                self.butler.up()
            sys.stdout.write("Filosofo[%s]Termina de pensar y comer"%self.number)
            
    def main():
        n=5
        butler=semaphore(n-1)
        c=[chopstick(i) for i in range(n)]
        p=[Philosopher (i,c[i], c[(i+1)%n],butler)for i in range(n)]
        for i in range(n):
            p[i].start()
            
    if __name__=" __main__":
        main()
