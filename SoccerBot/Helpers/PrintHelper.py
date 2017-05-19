
import time
from time import gmtime, strftime

def getTimeStr(): 
    return time.strftime("%Y-%m-%d %H:%M:%S", gmtime())

def tPrint(printMessage):
    return print(getTimeStr() + " - " + printMessage)