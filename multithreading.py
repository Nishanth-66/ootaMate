import time
import threading

def print_number():
    print(f"Hello from {threading.current_thread().name}!")
    for i in range (1, 6):
        print(f"Numbers: {i}")
        time.sleep(2)

def print_letter():
    print(f"Hello from {threading.current_thread().name}!")
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letters: {letter}")    
        time.sleep(1)   

# creat thread
thread1 = threading.Thread(target=print_number, name="NumberThread")
thread2 = threading.Thread(target=print_letter, name="LetterThread")

# Start Executing thread 
thread1.start()
thread2.start()

print(f"Is thread alive? {thread1.is_alive()}") # true

thread1.join()
thread2.join()

print("All tasks are completed!")    

print(f"Is thread alive? {thread1.is_alive()}") # true