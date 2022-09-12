from typing import List

def selectionSort(array, size) -> List[int]:
    for n in range(len(array)):
        min_value = array[n]
        for num in array:
            if num < min_val:
                array[n] = num
                array[array.index(num)] = min_val
    return array
        
# Do not change the following code
input_data = input()
data = []
for item in input_data.split(', '):
  if item.isnumeric():
    data.append(int(item))
  elif item.lstrip("-").isnumeric():
    data.append(int(item))
print(selectionSort(data, len(data)))
