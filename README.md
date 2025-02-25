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

### creating array from list  

```python
arry_1d = np.array([1,2,3,4])
print("1D arrays", arry_1d)

arry_2d = np.array([[1,2,3,4],[5,6,7,8]])
print("1D arrays", arry_2d)

```

    1D arrays [1 2 3 4]
    1D arrays [[1 2 3 4]
     [5 6 7 8]]


### List vs numpy array

```python


py_list = [1,2,3,4]
print("python list multiplication", py_list * 2)

np_array = np.array([1,2,3,4]) #element wise multiplication
print("python list multiplication", np_array * 2)

start = tm.time()
py_list = [i*2 for i in range(10000000)]
print("\n List operation time:", tm.time() - start)

start = tm.time()
np_array = np.arange(10000000) * 2
print("\n Numpy operation time:", tm.time() - start)
```

    python list multiplication [1, 2, 3, 4, 1, 2, 3, 4]
    python list multiplication [2 4 6 8]
    
     List operation time: 0.7219171524047852
    
     Numpy operation time: 0.028927326202392578


### creating array from scratch 

```python
zeros = np.zeros((4,4)) #2D Array
print("zeroes array: \n", zeros)

ones = np.ones((2,4)) #1D Array
print("ones array: \n", ones)

full = np.full((2,2), 7)#Constant Array
print("full array: \n", full)

random = np.random.random((2,4))
print("random array: \n", random)

sequence = np.arange(0, 10, 2)
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
     [[0.93748043 0.01553677 0.02877828 0.97461458]
     [0.73796814 0.13492485 0.84614389 0.33575778]]
    sequence array: 
     [0 2 4 6 8]


### Vector, Matrix and Tensor

```python
vector = np.array([1,2,3])
print("Vector: \n", vector)

matrix = np.array([[1,2,3],
                   [4,5,6]])
print("Matrix: \n", matrix)

tensor = np.array([[[1,2], [3,4]],
                   [[5,6],[7,8]]])
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



---

