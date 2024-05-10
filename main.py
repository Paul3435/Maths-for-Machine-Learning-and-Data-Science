import numpy as np

def basicsOfNumpy():
    # Create one dimensional array using array()
    a = np.array([10, 12])
    print(a)

    # Create one dimensional specifying a range
    b = np.arange(3)
    print(b)
    c = np.arange(1, 20, 3)
    print(c)

    # Five evenly spaced values within 0 and 100
    d = np.linspace(0, 100, 5, dtype=int)
    print(d)

    char_arr = np.array(['Welcome to Math for ML!'])
    print(char_arr)
    print(char_arr.dtype)  # Prints the data type of the array

    # Return a new array of shape 3, filled with ones.
    print(np.ones(3))
    # Return a new array of shape 3, filled with zeroes.
    print(np.zeros(3))
    # Return a new array of shape 3, without initializing entries.
    print(np.empty(3))
    # Return a new array of shape 3 with random numbers between 0 and 1.
    print(np.random.rand(3))

def multidimensionalArrays():
    # Create a 2 dimensional array (2-D)
    print(np.array([[1,2,3],[4,5,6]]))
    # An alternative way to create a multidimensional array is by reshaping the initial 1-D array. Using np.reshape() you can rearrange elements of the previous array into a new shape.
    one_dim_array = [1,2,3,4,5,6]
    multi_dim_array = np.reshape(one_dim_array, (2,3)) #splits in 2 rows and 3 cols, 2*3=6
    print(multi_dim_array)

    #Access the properties
    print('Number of dimensions: ', multi_dim_array.ndim, ', Shape: ', multi_dim_array.shape, ', Total Elements: ', multi_dim_array.size)

def arrayMathOperations():
    #Operate
    arr_1 = np.array([2, 4, 6])
    arr_2 = np.array([1, 3, 5])
    print('Sum: ', arr_1 + arr_2, ', Subtraction: ', arr_1 - arr_2, ', Product: ', arr_1 * arr_2, ", Divison: ", arr_1 / arr_2)

    #Vector * scalar
    print(np.array([1,2,3]) * 1.6)

def indexingAndSlicing():
    # Select the third element of the array. Remember the counting starts from 0.
    a = ([1, 2, 3, 4, 5])
    print(a[2])

    # Select the first element of the array.
    print(a[0])

    # Indexing on a 2-D array
    two_dim = np.array(([1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9]))

    # Select element number 8 from the 2-D array using indices i, j.
    print(two_dim[2][1])

    # Slice the array a to get the array [2,3,4]
    print(a[1:4])
    # Slice the array a to get the array [1,2,3]
    print(a[:3])
    # Slice the array a to get the array [3,4,5]
    print(a[2:5])
    # Slice the array a to get the array [1,3,5]
    print(a[::2])
    # Slice the two_dim array to get the first two rows
    print(two_dim[0:2])
    # Similarly, slice the two_dim array to get the last two rows
    print(two_dim[1:3])

def stacking():
    a1 = np.array([[1, 1],
                   [2, 2]])
    a2 = np.array([[3, 3],
                   [4, 4]])
    print(f'a1:\n{a1}')
    print(f'a2:\n{a2}')
    print(np.vstack((a1, a2)))
    print(np.hstack((a1, a2)))

def exercises():
    #Is there a difference between np.zeros() and np.empty()? D. np.empty() outputs an uninitialized array, but np.zeros() outputs an initialized array of value zero.

    print(np.zeros(3))
    print(np.empty(3))

if __name__ == "__main__":
    #basicsOfNumpy()
    #multidimensionalArrays()
    #arrayMathOperations()
    #indexingAndSlicing()
    #stacking()
    exercises()