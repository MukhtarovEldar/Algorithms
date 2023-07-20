def Merge_Sort(lst):
    n = len(lst)
    portion = 1 # the starting portion
    while portion < n: # looping while the portions are less than the size of the list
        temp = [] # temporary list to keep the sorted values
        left = 0 # left portion of the lst
        while left + portion < n: # looping until the end
            right = left + portion # right portion of the lst
            left_end = right - 1 # end of the left portion
            right_end = left_end + portion if left_end + portion < n else n - 1 # end of the right portion which is less than the size of the list
            i = left
            j = right
            while i <= left_end and j <= right_end: # looping through the separated lists
                if lst[i] < lst[j]: # sorting two separated portions
                    temp.append(lst[i])
                    i += 1
                else:
                    temp.append(lst[j])
                    j += 1
            while i <= left_end: # if the sizes of portions are different adding the rest to the end of the temp list
                temp.append(lst[i])
                i += 1
            while j <= right_end: # if the sizes of portions are different adding the rest to the end of the temp list
                temp.append(lst[j])
                j += 1
            left += 2 * portion # going to the next portion 1/2, 1/4, 1/8...
        portion *= 2
        for i in range(0, right_end + 1):
            lst[i] = temp[i] # changing the values of the lst to the sorted ones

lst = [3, 2, 1, 5, 4, 7, 6, 9, 10, 8]
Merge_Sort(lst)
print(lst)