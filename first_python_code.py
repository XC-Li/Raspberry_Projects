# the first python code
import sys
print (sys.version)
print ("Hello World!")
f = open("test_text","r+")
f.write('this is a test\n')
print(f.read())
