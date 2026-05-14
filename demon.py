import threading
import time

def background_task():
    while True:
        print("Background task running..")
        time.sleep(1)

# creat demon thread

thread = threading.Thread(target=background_task)
thread.daemon = True # set the thread as daemon
thread.start()

# main program ends here 
time.sleep(3)
print("Main program ends.")
