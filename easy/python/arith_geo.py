#*
# Have the function arithGeo(arr) take the array of numbers stored in arr and
# return the string "Arithmetic" if the sequence follows an arithmetic pattern
# or return "Geometric" if it follows a geometric pattern. If the sequence
# doesn't follow either pattern return -1. An arithmetic sequence is one where
# the difference between each of the numbers is consistent, where as in a
# geometric sequence, each term after the first is multiplied by some constant
# or common ratio. Arithmetic example: [2, 4, 6, 8] and Geometric example: [2,
# 6, 18, 54]. Negative numbers may be entered as parameters, 0 will not be
# entered, and no array will contain all the same elements.
#
# https://www.coderbyte.com/results/bhanson:Arith%20Geo:JavaScript
#


from re import I


def arithGeo(arr):
    if len(arr) == 1:
        return -1
    elif len(arr) == 0:
        return -1

    arithmetic = True
    geometric = True
    for i in (range(len(arr)-1)):
        diff = arr[1] - arr[0]
        div = arr[1] / arr[0] 
        print(i)
        print("diff: {}".format(diff))
        if arr[i+1] - arr[i] != diff:
            print(arr[i+1])
            print(arr[i])
            print('diff2 : {}'.format(arr[i+1] - arr[i]))
            arithmetic = False
        if arr[i+1] / arr[i] != div:
            geometric = False

    if arithmetic:
        return "Arithmetic"

    if geometric:
        return "Geometric"

    
    return -1 
        
arithGeo([1,2,3,4,5])