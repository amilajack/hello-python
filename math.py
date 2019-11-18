import numpy

# Create an array of 1's of size 2
[1, 2, 3] * 2 # [1, 2, 3, 1, 2, 3]


# Divide each element of an array
myList = [10,20,30,40,50,60,70,80,90]
myInt = 10
newList = [x / myInt for x in myList]

# Divide each element of an array using numpy
myArray = numpy.array([10,20,30,40,50,60,70,80,90])
myInt = 10
newArray = myArray/myInt