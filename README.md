# My NumPy Learning Notebooks 📚

Click on any notebook to open it in GitHub:

- [./venv/phase-1.ipynb](././venv/phase-1.ipynb)
## ⚙️ Activating Virtual Environment:

Run the following commands to set up and activate the virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
pip install numpy  # install numpy library 
```


---

## 📖 Notebook Contents


---

### ./venv/phase-1.ipynb

## Numpy array and basics


```python
import numpy as np  
import time as tm                                     
```

### creating array from numpy

```python
arry_1d = np.array([1,2,3,4]) #1D Array
print("1D arrays", arry_1d)

arry_2d = np.array([[1,2,3,4],[5,6,7,8]]) #2D Array
print("1D arrays", arry_2d)

```

    1D arrays [1 2 3 4]
    1D arrays [[1 2 3 4]
     [5 6 7 8]]


### List vs numpy array

```python


py_list = [1,2,3,4] #index wise multplication
print("python list multiplication", py_list * 2)

np_array = np.array([1,2,3,4]) #element wise multiplication
print("python list multiplication", np_array * 2)

#Checking which is fast list or numpy array:
start = tm.time()
py_list = [i*2 for i in range(10000000)]
print("\n List operation time:", tm.time() - start)

start = tm.time()
np_array = np.arange(10000000) * 2
print("\n Numpy operation time:", tm.time() - start)
```

    python list multiplication [1, 2, 3, 4, 1, 2, 3, 4]
    python list multiplication [2 4 6 8]
    
     List operation time: 1.0705020427703857
    
     Numpy operation time: 0.050539493560791016


### creating array from scratch 

```python
zeros = np.zeros((4,4)) #2D Array
print("zeroes array: \n", zeros)

ones = np.ones((2,4)) #1D Array
print("ones array: \n", ones)

full = np.full((2,2), 7) #Constant Array
print("full array: \n", full)

random = np.random.random((2,4)) #random numbers 2*4 array
print("random array: \n", random)

sequence = np.arange(0, 10, 2) # sequence of numbers in an array
print("sequence array: \n", sequence)

```

    zeroes array: 
     [[0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]]
    ones array: 
     [[1. 1. 1. 1.]
     [1. 1. 1. 1.]]
    full array: 
     [[7 7]
     [7 7]]
    random array: 
     [[0.12729727 0.22552876 0.86790304 0.78062619]
     [0.89569978 0.92643782 0.92396273 0.74902979]]
    sequence array: 
     [0 2 4 6 8]


### Vector, Matrix and Tensor

```python
vector = np.array([1,2,3]) #1D Array = vector
print("Vector: \n", vector)

matrix = np.array([[1,2,3],
                   [4,5,6]]) #2D Array = matrix
print("Matrix: \n", matrix)

tensor = np.array([[[1,2], [3,4]],
                   [[5,6],[7,8]]]) #3D+ Array = tensor
print("Tensor: \n", tensor)
```

    Vector: 
     [1 2 3]
    Matrix: 
     [[1 2 3]
     [4 5 6]]
    Tensor: 
     [[[1 2]
      [3 4]]
    
     [[5 6]
      [7 8]]]


### Array properties

```python
arr = np.array(([1,2,3,4],
                [5,6,7,True] #Should be similar data types
                ))
print("Shape: ", arr.shape)
print("Dimension :", arr.ndim)
print("Size: ", arr.size)
print("Size: ", arr.dtype)
```

    Shape:  (2, 4)
    Dimension : 2
    Size:  8
    Size:  int64


### Array Reshaping

```python
arr = np.arange(12)
print("ORignal array: ", arr)

reshaped = arr.reshape((3,4)) #reshape array into 3 by 4
print("Reshaped array:\n", reshaped)

#flatten (returns orginal)
flattened = reshaped.flatten()
print("\n Flattened array :", flattened)

#ravel (returns view, instead of copy)
raveled = reshaped.ravel()
print("\n Raveled array :", raveled)

#Transpoze 
transpozed = reshaped.T
print("\n Transpozed array :\n", transpozed)
```

    ORignal array:  [ 0  1  2  3  4  5  6  7  8  9 10 11]
    Reshaped array:
     [[ 0  1  2  3]
     [ 4  5  6  7]
     [ 8  9 10 11]]
    
     Flattened array : [ 0  1  2  3  4  5  6  7  8  9 10 11]
    
     Raveled array : [ 0  1  2  3  4  5  6  7  8  9 10 11]
    
     Transpozed array :
     [[ 0  4  8]
     [ 1  5  9]
     [ 2  6 10]
     [ 3  7 11]]



---

