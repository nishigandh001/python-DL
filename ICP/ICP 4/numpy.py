import numpy as np
from collections import Counter
from statistics import mode

array = np.random.randint(0,21,15)
print(array)
# mode(array)


data = Counter(array)
data2=data.most_common()   # Returns all unique items and their counts
data3=data.most_common(1)   # Returns the highest occurring item
print(data3)