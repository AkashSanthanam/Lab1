"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import timeit
import matplotlib.pyplot as plot


# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)

def bubble_sort2(L):
  for i in range(len(L)):
    swapped = False
    for j in range(0, len(L) - i - 1):
      if L[j] > L[j + 1]:
        swap(L, j, j+1)
        swapped = True

    if not swapped:
      break


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)

def selection_sort2(L):
    left = 0
    right = len(L) - 1
    while left < right:
        min_index = left
        max_index = right
        for i in range(left, right + 1):
            if L[i] < L[min_index]:
                min_index = i
            if L[i] > L[max_index]:
                max_index = i

        swap(L, left, min_index)

        if max_index == left:
            max_index = min_index
        
        swap(L, right, max_index)

        left += 1
        right -= 1


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

total1 = 0
total2 = 0
total3 = 0
total4 = 0
data = []
n = 1000
k = 100

for _ in range(n):
    L = create_random_list(k, k)
    L2 = L.copy()
    L3 = L.copy()
    L4 = L.copy()

    start = timeit.default_timer()
    insertion_sort(L)
    end = timeit.default_timer()
    total1 += end - start

    start = timeit.default_timer()
    insertion_sort2(L2)
    end = timeit.default_timer()
    total2 += end - start

    start = timeit.default_timer()
    bubble_sort(L3)
    end = timeit.default_timer()
    total3 += end - start

    start = timeit.default_timer()
    selection_sort(L4)
    end = timeit.default_timer()
    total4 += end - start


# step is space between
# n is highest length list
# m is number of lists
size_plot = []

def experiement1(n, m, step):
    times1 = []
    times2 = []
    times3 = []
    times4 = []
    timesAll = []
    for i in range(0, n, step):
        timeIns = 0
        timeSel = 0
        timeBub = 0
        timeOptSel = 0
        L = create_random_list(i, i)
        size_plot.append(i)
        for _ in range(m):
            print("Experiement 1 Running")
            copy1 = L.copy()
            copy2 = L.copy()
            copy3 = L.copy()
            copy4 = L.copy()

            # Insertion Sort
            start1 = timeit.default_timer()
            insertion_sort(copy1)
            end1 = timeit.default_timer()
            timeIns += end1 - start1


            # Selection Sort
            start2 = timeit.default_timer()
            selection_sort(copy2)
            end2 = timeit.default_timer()
            timeSel += end2 - start2
            

            # Bubble Sort
            start3 = timeit.default_timer()
            bubble_sort(copy3)
            end3 = timeit.default_timer()
            timeBub += end3 - start3

            # Optimized Insertion Sort
            start4 = timeit.default_timer()
            insertion_sort2(copy4)
            end4 = timeit.default_timer()
            timeOptSel += end4 - start4


            # print(time)
        times1.append(timeIns/m)
        times2.append(timeSel/m)
        times3.append(timeBub/m)
        times4.append(timeOptSel/m)
        timesAll.append(times1)
        timesAll.append(times2)
        timesAll.append(times3)
        timesAll.append(times4)

    
        
    
    return timesAll


# Selection vs Optimized Selection

def experiement2(n, m, step):
    times1 = []
    times2 = []
    timesAll = []
    for i in range(0, n, step):
        timeSel = 0
        timeOptSel = 0
        L = create_random_list(i, i)
        size_plot.append(i)
        for _ in range(m):
            print("Experiement 2 Running")
            copy1 = L.copy()
            copy2 = L.copy()

            # Selection Sort
            start1 = timeit.default_timer()
            selection_sort(copy1)
            end1 = timeit.default_timer()
            timeSel += end1 - start1


            # Optimized Selection Sort
            start2 = timeit.default_timer()
            selection_sort2(copy2)
            end2 = timeit.default_timer()
            timeOptSel += end2 - start2
            

        


            # print(time)
        times1.append(timeSel/m)
        times2.append(timeOptSel/m)
        timesAll.append(times1)
        timesAll.append(times2)
      

    
        
    
    return timesAll

# Bubble vs Optimized Bubble
def experiement3(n, m, step):
    times1 = []
    times2 = []
    timesAll = []
    for i in range(0, n, step):
        timeBub = 0
        timeOptBub = 0
        L = create_random_list(i, i)
        size_plot.append(i)
        for _ in range(m):
            print("Experiement 3 Running")
            copy1 = L.copy()
            copy2 = L.copy()

            # Bubble Sort
            start1 = timeit.default_timer()
            bubble_sort(copy1)
            end1 = timeit.default_timer()
            timeBub += end1 - start1


            # Optimized Bubble Sort
            start2 = timeit.default_timer()
            bubble_sort2(copy2)
            end2 = timeit.default_timer()
            timeOptBub += end2 - start2
            

        


            # print(time)
        times1.append(timeBub/m)
        times2.append(timeOptBub/m)
        timesAll.append(times1)
        timesAll.append(times2)
      

    
        
    
    return timesAll

step = 100
size = 1000
number_of_lists = 1000
times = experiement3(size, number_of_lists, step)

plot.plot(size_plot, times[0], label = "Bubble Sort")

plot.plot(size_plot, times[1], label = "Optimized Bubble Sort")



# plot.plot(size_plot, times[0], label = "Insertion Sort")

# plot.plot(size_plot, times[1], label = "Selection Sort")

# plot.plot(size_plot, times[2], label = "Bubble Sort")

# plot.plot(size_plot, times[3], label = "Optimized Insertion Sort")

plot.ylabel("Time")
plot.xlabel("List Size")
plot.title("Bubble Sort vs Optimized Bubble Sort")
plot.legend()
plot.show()





# print("Improvement of ", (1 - total2/total1) * 100, "%")
