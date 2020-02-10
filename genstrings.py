###############################################################################
#
#   Author: Mohammed Almodawah
#   Date: 2/10/2020
#   version: v 1.0
#
#   Description:
#   An easy-to-use and a thread-safe python class for generating all possible
#   strings of a given length from a given set of characters.
#
###############################################################################

import threading

class GenStrings:
    def __init__(self, length, charset):
        self.__length = length
        #Convert to a unique list
        self.__charset = list(set(charset))
        self.__charset.sort()
        self.__firststr = True
        self.__currentstr = ""
        self.__laststr = ""
        self.__firstchar = self.__charset[0]
        self.__lastchar = self.__charset[len(self.__charset) - 1]
        #Building the first string
        for i in range(0, length):
            self.__currentstr = self.__currentstr + self.__firstchar

        #Building the last string    
        for i in range(0, length):
            self.__laststr = self.__laststr + self.__lastchar
        #A mutex for  thread-safe access to the current string
        self.__lock = threading.Lock()
    
    #increments a string
    def __incstr(self, string):
        strlen = len(string)
        if string[strlen - 1] != self.__lastchar:
            #Find the next character from the character set
            nextchar = self.__charset[self.__charset.index(string[strlen - 1]) + 1]
            string[strlen - 1] = nextchar
            return string
        else:
            string = self.__incstr(string[0:strlen - 1])
            string.append(self.__firstchar)
            return string
    
    # Returns the next string
    def nextstr(self):
        self.__lock.acquire()
        if self.__firststr:
            self.__firststr = False
            toreturn = self.__currentstr
            self.__lock.release()
            return toreturn
        if self.__currentstr == self.__laststr:
            self.__lock.release()
            return None

        currentstr = list(self.__currentstr)
        inced = self.__incstr(currentstr)
        self.__currentstr = "".join(inced)
        toreturn = self.__currentstr
        self.__lock.release()
        return toreturn
