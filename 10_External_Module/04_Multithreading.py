import threading
import time

def worker(n):
    print(f"Thread {n}: Starting")
    time.sleep(2) #stimulate some work means pause for 2sec or hold for 2sec before running the program.
    print(f"Thread {n}: Finishing")
    
threads=[]

for i in range(3):
    thread=threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join() #Wait for all the thread to finish
print("All threads completed.")