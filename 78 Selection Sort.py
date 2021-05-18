# 78 Selection Sort
def selection_sort(alist):
    for i in range(0, len(alist) - 1):
        smallest = i
        for j in range(i + 1, len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i], alist[smallest] = alist[smallest], alist[i] 
alist = input('Enter the list of numbers : ').split()
alist = [int(x) for x in alist]
selection_sort(alist)
print('List sorted using Selection Sort : ', end='')
print(alist)


string = 'chegg'

for c in string [::-1]:
    print (c, end = "")
    string = string.upper()