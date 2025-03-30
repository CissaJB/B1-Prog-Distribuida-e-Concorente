from concurrent.futures import ThreadPoolExecutor
import numpy as np
import time

MAX_THREADS = 4  
array = np.random.randint(-2**31, 2**31, size=3_000_000)

def sum_array(start, end):
    return np.sum(array[start:end])

def thread_sum():
    print("-----------Iniciando soma com multithreading----------------------")
    start_time = time.time()
    
    chunk_size = len(array) // MAX_THREADS
    futures = []

    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        for i in range(MAX_THREADS):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i != MAX_THREADS - 1 else len(array)
            futures.append(executor.submit(sum_array, start, end))

        final_sum = sum(future.result() for future in futures)
    
    print(f"Soma final é: {final_sum}")
    print(f"Tempo de execução: {time.time() - start_time} seg.")
    print("------------------------------------------------------------------")

def sequencial_sum():
    print('\n')
    print("----------Iniciando soma sequencial--------------------------------")
    start_time = time.time()
    sum = np.sum(array)
    print(f"Soma final: {sum}")
    print(f"Tempo de execução: {time.time() - start_time} seg.")

thread_sum()
sequencial_sum()
