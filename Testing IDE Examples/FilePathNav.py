import os.path

#manually setting filepath:
filepath = "/Users/jembox/OneDrive/ASU/SER_402/arduino-tests/README.md"

#__file__ can also be used if referencing the module with which it was loaded:
# "__file__ is the pathname of the file from which the module was loaded, if it was loaded from a file."
# https://docs.python.org/3/reference/datamodel.html

print globals()
print __file__

#Print out the directory
print(os.path.dirname(filepath))

#Get the file name
print(os.path.dirname(filepath))

#Print filepath and filename separately
print(os.path.split(filepath))

#Does file exist?
print(os.path.exists(filepath))

#Print absolute path
print(os.path.abspath(filepath))

#navigating fp directory up one level and into another folder
os.path.abspath(os.path.join(os.path.dirname(filepath), '..', 'jthoma74_FlagTests'))

#print parent directory
os.path.dirname(os.path.dirname(filepath))