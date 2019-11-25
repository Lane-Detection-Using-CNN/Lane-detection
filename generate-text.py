#Python 3.7.2
#!/usr/bin/python
import re
import os
import collections
import time

def buildIndex():
	
        currentPath = "/Users/jeffreytakyi-yeboah/Desktop/kafka_2.12-2.3.0/test.MP4"
                
        currentdir = sorted(os.listdir(currentPath))
               
        for currentfile in currentdir:
                if currentfile.endswith(".jpg"):
                        
                        my_file = os.path.join(currentPath, currentfile)
                #print(my_file)
                        print(currentfile)
                                    

               
        return
if __name__ == '__main__':
    buildIndex()
