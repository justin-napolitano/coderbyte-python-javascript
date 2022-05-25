

#
 # Have the function abCheck(str) take the str parameter being passed and return
 # the string true if the characters a and b are separated by exactly 3 places
 # anywhere in the string at least once (ie. "lane borrowed" would result in
 # true because there is exactly three characters between a and b). Otherwise
 # return the string false.
 #
 # https://www.coderbyte.com/results/bhanson:AB%20Check:JavaScript
 #
 # @param  {string} str
 # @return {string} 'true' or 'false'
 
def ab_check(str):
    
    searchLetters = ['a','b']
    letterSpace = 3


    if len(str) < letterSpace +2:
        return False

    i = 0
    while i < len(str) - letterSpace -1:
        try:
            if str[i] == searchLetters[0]:
                if (str[ i+ letterSpace + 1] == searchLetters[1]):
                    return True
            elif str[i] == searchLetters[1]:
                if str[i + letterSpace + 1] == searchLetters[0]: 
                  return True
        except:
            return False
        i = i +1
    return False

print(ab_check(''))



