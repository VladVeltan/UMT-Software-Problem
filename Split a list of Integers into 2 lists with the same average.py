def splitArraySameAverage(A):
    if len(A) <= 1:                         # if the length of the list is below 1 we return False
        return False
    list = sorted(A)                        # we sort the list we are going to work on
    length = len(list)                      # we save the length of the original list
    sum_tot = sum(list)                     # we save the sum of all the elements as sum_tot
    start = list[0]                         # first element of the list
    finish = list[len(list) - 1]            # last element of the list
    nrInB = 2                               # how many numbers are in B 
    sumB = start + finish                   # Here we are going to store the sum of elements that are currently in B
    avgB = (start + finish) / nrInB         # here we are going to store the average of B
    if length - nrInB == 0 and list[0] != list[1]: # We check to see if the given list length if 2 and the elements are not equal
        return False
    elif length - nrInB == 0 and list[0] == list[1]: # We check to see if the given list length is 2 and the elements are equal
        return True
    avgC = (sum_tot - sumB) / (length - nrInB)# We calculate the average of C knowing the total sum,the sum of B, the list length and the length of B
    i = 1                                   # we are using i as the index
    if avgB == avgC:                        # we check to see if the given list has consecutive increasing numbers like [1, 2, 3, 4],[2, 4, 6, 8, 10]
        return True
    while avgB != avgC and i <= length - 2: # while the averages are different and while we didn't go through all the possibilities
        nrInB += 1                          # inscrese the count of numbers in B
        for x in range(i,length - 2):       # we go through all the possibility of 3 numbers in B and n-3 numbers in the list
            if length - nrInB == 0:         # if this is 0 we went through all the possibilities and return false
                return False
            if (sumB + list[x]) / nrInB == (sum_tot - sumB - list[x]) / (
                    length - nrInB):        # we check if the new average of B is equal to the C average
                return True
        sumB = sumB + list[i]               # we add the next element in B list
        nrInB += 1                          # we increase the count of numbers in B
        avgB = sumB / nrInB                 # calculate the avg of B
        if length - nrInB == 0:             # we went to all possibility's
            return False
        avgC = (sum_tot - sumB) / (length - nrInB)  # calculate the AVG of C
        i += 1  # increase the index
    return False


testCases = [[2, 2, 33], [2, 4, 4], [], [1], [75, 2], [11, 23, 37, 45, 54, 86, 90], [1, 2, 3, 4, 5, 6,7,8],
             [2, 4, 6, 8, 10, 12, 14, 16],
             [11, 23, 37, 45, 54, 86, 94], [10, 20, 30, 40, 50, 60, 70, 120], [2, 2, 2]]
for lst in testCases:
    print(splitArraySameAverage(lst))
