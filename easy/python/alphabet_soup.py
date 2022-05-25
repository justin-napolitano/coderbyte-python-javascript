#
#Have the function alphabetSoup(str) take the str string parameter being
#passed and return the string with the letters in alphabetical order (ie.
#hello becomes ehllo). Assume numbers and punctuation symbols will not be
#included in the string.
#@param  {string} str
#@return {string}
#

def Convert(s):
    list1=[]
    list1[:0]=s
    return list1

def alphabetSoup(s):
    s = Convert(s)
    s.sort()
    s= "".join(s)

 
    return s




