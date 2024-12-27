from collections import defaultdict

# Default dictionary to handle missing keys
data = defaultdict(int)  # Default value is 0
data['apple'] += 1
data['banana'] += 2
print(data)  # Outputs: defaultdict(<class 'int'>, {'apple': 1, 'banana': 2})