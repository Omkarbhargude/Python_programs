import multiprocessing     
import time 
import os          

def SumEven(No):
    print("PID of SumEven : ",os.getpid()) # PID of sumeven :- 51
    print("PPID of SumEven : ",os.getppid())    # PPID of sumeven :- 21
    
    Sum = 0
    for i in range(2,No+1,2):
        Sum = Sum + i

    print("Even Sum is : ",Sum) 

def SumOdd(No):
    print("PID of SumOdd : ",os.getpid()) # PID of sumodd :- 101
    print("PPID of SumOdd : ",os.getppid()) # PPID of sumodd :- 21
    
    Sum = 0
    for i in range(1,No+1,2):
        Sum = Sum + i

    print("Odd Sum is : ",Sum) 

def main():

    print("PID of main : ",os.getpid()) # PID of main :- 21
    print("PPID of main : ",os.getppid())   # PPID of CMD :- 11

    start_time = time.time()

    t1 = multiprocessing.Process(target=SumEven,args=(10000,))
    t2 = multiprocessing.Process(target=SumOdd,args=(10000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end_time = time.time()

    print("Time required : ",end_time-start_time)
    
if __name__ == "__main__":
    main()