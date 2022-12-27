import numpy as np
# x = np.array([1.3,2.1,4.5])
# print("x : ", x)
# print("x ndim ", x.ndim)

# print("x shape", x.shape)
# print("x size", x.size)
# print("x dtype", x.dtype)


# Broadcast
# a  = np.array((3,4,5)) #[3 4 5]
# b = np.expand_dims(a,axis=1)  #[[3][4][5]]
# print(a, a.shape) 
# print(b, b.shape)

# x = a+b # This won't work as a has a  shape(3,) and not (3,1)


# a  =a.reshape(-1,1)
# print(a.shape) # Now can do airthmetic operations


#Transpose
# Transposing
x = np.array([[1,2,3], [4,5,6]])
print ("x:\n", x)
print ("x.shape: ", x.shape)
y = np.transpose(x, (1,0)) # flip dimensions at index 0 and 1
print ("y:\n", y)
print ("y.shape: ", y.shape)

#More Topics include REshaping , joining and expanding/squeezing dimensions