## mergesort.py
def mergesort(arr):
  if len(arr) <= 1:
    return arr
  
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]
  
  left_half = mergesort(left_half)
  right_half = mergesort(right_half)
  
  return merge(left_half, right_half)

def merge(left, right):
  merged = []
  i = j = 0
  
  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      merged.append(left[i])
      i += 1
    else:
      merged.append(right[j])
      j += 1
  
  while i < len(left):
    merged.append(left[i])
    i += 1
  
  while j < len(right):
    merged.append(right[j])
    j += 1
  
  return merged