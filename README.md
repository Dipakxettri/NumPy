# My NumPy Learning Notebooks 📚

Click on any notebook to open it in GitHub:

- [./venv/phase-1.ipynb](././venv/phase-1.ipynb)

---

## 📖 Notebook Contents

### ⚙️ Activating Virtual Environment:

Run the following commands to set up and activate the virtual environment:

```sh
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate  # For Windows
```


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
    
     List operation time: 0.6777400970458984
    
     Numpy operation time: 0.0328669548034668


### creating array from scratch 

```python
zeroes = np.zeros((4,4))
print("zeroes array:", zeroes)
```

    zeroes array: [[0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]
     [0. 0. 0. 0.]]



---

