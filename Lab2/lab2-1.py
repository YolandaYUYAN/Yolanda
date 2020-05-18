# Q1  Implement Insertion Sort.


def insertionSort(list):
    numOfComp = 0
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = key
        numOfComp = numOfComp + 1
    print("Number of Comparisons:", numOfComp)
import random

#Mylist = [99, 10, 15, 85, 56, 28, 17, 5,5,645,958,126,56,15,65,84,5441,545,51,56445,645,1,545,4]

def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list
random_list = random_int_list(1,1000,10)
#print(random_list)
insertionSort(random_list)
print(random_list)


import time

start = time.time()
random_list.sort()
stop = time.time()
time_taken = stop - start
print("Time taken:", time_taken)
