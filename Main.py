from typing import List

def selectionSort(array, size) -> List[int]:
    for n in range(len(array)):
        min_val = n
        for num in range(n + 1, len(array)):
            if min_val > array[num]:
                min_val = num
            array[num], array[min_val] = array[min_val], array[num]
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
