import json

# Sample data
data = {'name': 'Alice', 'age': 30}

# Write JSON to a file
with open('data.json', 'w') as f:
    json.dump(data, f)

# Read JSON from a file
with open('data.json', 'r') as f:
    loaded_data = json.load(f)
print(loaded_data)  # Outputs: {'name': 'Alice', 'age': 30}