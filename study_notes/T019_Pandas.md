````
-------------------------------------------------------------------------------------
-> Title : Pandas
-> Author : @neeraj-singh-jr
-> Status : Ongoing...
-> Created : 2024-04-14
-> Updated : 2024-04-14
-> Summary : Notes indices are as follows (**** pending)
-------------------------------------------------------------------------------------
-> Q004 : Dataframe with Python Datastructure;;
-> Q003 : Series with Python Datastructure;;
-> Q002 : What is Pandas;;
-> Q001 : Introduction To Data Analysis;;
-------------------------------------------------------------------------------------
````

### PANDAS NOTES : BEGINNING

-------------------------------------------------------------------------------------
### Q004 : Dataframe with Python Datastructure;;

Pandas Dataframe are two-dimensional form of representing the data

**Ex1: Creating Pandas Dataframe**

```example: Creating Pandas Dataframe

import pandas as pd

data = [1,2,3,4,5]

d1 = pd.DataFrame(data)
print(d1)
# output:=
#    0
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5

d1 = pd.DataFrame({'a': data})
print(d1)
# output:-
#    a
# 0  1
# 1  2
# 2  3
# 3  4
# 4  5

data = {'a': [1,2,3], 'b': [4,5,6]}
d1 = pd.DataFrame(data)
print(d1)
# output:
#    a  b
# 0  1  4
# 1  2  5
# 2  3  6

# error will be thrown if there is unmatched column values;;
data = {'a': [1,2,3], 'b': [4,5]}
d1 = pd.DataFrame(data)
print(d1)
# output:
# ValueError: All arrays must be of the same length
```

-------------------------------------------------------------------------------------
### Q003 : Pandas Series with Python Datastructure;;

Pandas Series are only one dimensional form of representing the data.

**Ex1: Creating Pandas series from the basic python list**

```example: Creating Pandas series from the basic python list

import pandas as pd

data = [1,2,3,4]

# basic series
s = pd.Series(data)
print(s)

# output:
# column 0 : index 
# column 1 : value
# datetype : int base64
# 0    1
# 1    2
# 2    3
# 3    4
# dtype: int64

print("series type : ", type(s))
# series type :  <class 'pandas.core.series.Series'>
```

**Ex2: Creating Series with Custom index**

```example: Creating Series with Custom index

import pandas as pd


d1 = [1,2,3,4]

# custom indexing are also supposed to match exactly in the order of the 
# data provided in the very first place.
s1 = pd.Series(d1, index=['a', 'b', 'c', 'd'])

# this will throw you an error saying... length mismatch;;
# s1 = pd.Series(d1, index=['a', 'b'])

print(s1)

# output:
# a    1
# b    2
# c    3
# d    4
# dtype: int64
```

**Ex3: Creating Series with custom python dictionary**

```example 1 : mapping heterogeneous dictionary with pandas series directly;;

# example 1: mapping heterogeneous dictionary with pandas series directly

# heterogeneous dictionary
hashmap = {
    'id_001': {
        'first_name': 'neeraj',
        'middle_name': 'singh',
        'last_name': 'junior',
        'language': ['hindi', 'english']
    },
    'id_002': {
        'first_name': 'adam',
        'middle_name': 'ray',
        'last_name': 'jensen',
        'language': ['hindi', 'english']
    },
    'id_003': ['hindi', 'english'],
    'id_004': 12
}

hm1 = pd.Series(hashmap)
print(hm1)

# output:
# id_001    {'first_name': 'neeraj', 'middle_name': 'singh...
# id_002    {'first_name': 'adam', 'middle_name': 'ray', '...
# id_003                                     [hindi, english]
# id_004                                                   12
# dtype: object
````

```example 2: mapping the same dictionary with custom index directly;;

# example 2: mapping the same dictionary with custom index directly;; 

# the provided dictionary hashmap contains nested dictionaries and lists, 
# which cannot be directly converted to a pandas Series

hm1 = pd.Series(hashmap, index=['a', 'b', 'c', 'd'])
print(hm1)
# output:-
# a    NaN
# b    NaN
# c    NaN
# d    NaN
# dtype: object

```

```example 3: Mapping the same dictionary with different approach;; 

# example 3: Mapping the same dictionary with different approach;;

hmap_series = pd.Series(hashmap)
print(hmap_series)
# output:
# id_001    {'first_name': 'neeraj', 'middle_name': 'singh...
# id_002    {'first_name': 'adam', 'middle_name': 'ray', '...
# id_003                                     [hindi, english]
# id_004                                                   12
# dtype: object

hmap_series.index = range(10, len(hmap_series) + 10) 
print(hmap_series)
# output:
# 10    {'first_name': 'neeraj', 'middle_name': 'singh...
# 11    {'first_name': 'adam', 'middle_name': 'ray', '...
# 12                                     [hindi, english]
# 13                                                   12
# dtype: object
```


-------------------------------------------------------------------------------------
### Q002 : What is Pandas;;

#### Pandas Getting Started;;

1. The name Pandas has a reference to both `Panel Data` and `Python Data Analysis`
and was created by `Wes Mckinney` in 2008.
2. Pandasn is a python library used for working with dataset.
3. It has function for analyzing, cleaning, exploring and manipulating for data.
4. Read and write data structure and different formats : CSV, XML, JSON, ZIP etc.

#### Pandas Data Structure;;
There are three types of dataset in pandas 
1. `Series`: One dimensional labelled array eg, `pd.Series(data)`
2. `Dataframes`: Two dimensional data structure with columns much like a table.
3. `Panel`: A Panel is a 3D Container of data

````
Output of Series and Dataframe;;

      | Apple |              | Mango |           | Apple | Mango |
---------------        ---------------              -----------------------
| 0   |  4    |        | 0   |  5    |              | 0   |  4    |  5    |
| 1   |  5    |    +   | 1   |  3    |      =       | 1   |  5    |  3    |
| 2   |  2    |        | 2   |  2    |              | 2   |  2    |  2    |
| 3   |  10   |        | 3   |  20   |              | 3   |  10   |  20   |
---------------        ---------------              -----------------------
   Series 1               Series 2                       Data Frame
````

#### Importance of Pandas in Python;;

1. Pandas allows us to analyze big data and make statistical theories.
2. Pandas can clean messy data sets and make them readable and relevant.
3. Easy handling of missing data (representation as NaN) in floating point as well 
as non-floating point data.
4. Size mutuability: Column can be inserted and deleted from dataframe and higher
dimensional objects
5. Dataset merging and joining. Flexing reshaping and pivoting of datasets provide
6. time series funtionality.


-------------------------------------------------------------------------------------
### Q001 : Introduction To Data Analysis;;

`Data Analysis` is a process of inspecting, cleansing, transforming and modelling
of data with the goal fo discovering useful information, informing conclusion and 
also support decision-making when parsing raw data.

#### Python Libraries for Data Analysis;;
1. Numpy
2. StatsModel
3. Matplotlib
4. Scipy
5. Scikit Learn
6. Pandas
7. Seaborn


-------------------------------------------------------------------------------------