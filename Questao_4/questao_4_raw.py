from threading import Thread
import time
import numpy as np

MAX_THREADS = 4

array = np.random.randint(-2**31, 2**31, size=3_000_000)
sum_arr = [0 for _ in range(MAX_THREADS)]
part = 0

def sum_array():
    global part
    thread_part = part
    part = part + 1

    thread_start = int(thread_part * (len(array)/MAX_THREADS))
    thread_end = int((thread_part + 1) * (len(array)/MAX_THREADS))

    for i in range(thread_start, thread_end, 1):
        sum_arr[thread_part] = sum_arr[thread_part] + array[i]

def thread_sum():
    print("-----------Iniciando soma com multithreading----------------------")
    start_time = time.time()

    thread = list(range(MAX_THREADS))
    
    for i in range(MAX_THREADS):
        thread[i] = Thread(target=sum_array)
        thread[i].start()
        # print(f'Thread[{i + 1}] com valor: {sum_arr[i]}\n')

    for i in range(MAX_THREADS):
        thread[i].join()

    final_sum = 0
    for x in sum_arr:
        final_sum += x
    print(f"Soma final é: {final_sum}")
    print(f"Tempo de execução: {time.time() - start_time} seg.")
    print("------------------------------------------------------------------")

def sequencial_sum():
    print('\n')
    print("----------Iniciando soma sequencial--------------------------------")
    start_time = time.time()
    sum = 0 
    
    for i in array:
        sum += i
    print(f"Soma final: {sum}")
    print(f"Tempo de execução: {time.time() - start_time} seg.")

thread_sum()
sequencial_sum()
