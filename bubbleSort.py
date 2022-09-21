# write your bubble sort algorithm below


def bubble_sort(list_to_sort):
    s = list_to_sort.copy()
    for i in range(len(s) - 1):
        for j in range(len(s) - 1):
            if s[j] > s[j+1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s


unsorted = [33, 5, 17, 81, 22, 12, 2, 55]
print(bubble_sort(unsorted))
