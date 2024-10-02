def CSM(data_structure):
    summa = 0
    if isinstance(data_structure, dict):
        for key, value in data_structure.items():
            summa += CSM(key)
            summa += CSM(value)
    elif isinstance(data_structure, (list, tuple, set)):
        for item in data_structure:
            summa += CSM(item)
    elif isinstance(data_structure, (int, float)):
        summa += data_structure
    elif isinstance(data_structure, str):
        summa += len(data_structure)
    return summa
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = CSM(data_structure)
print(result)