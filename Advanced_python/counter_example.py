from collections import Counter

# Count occurrences of elements in a list
data = ['apple', 'banana', 'orange', 'apple', 'banana', 'banana']
counter = Counter(data)
print(counter)  # Outputs: Counter({'banana': 3, 'apple': 2, 'orange': 1})