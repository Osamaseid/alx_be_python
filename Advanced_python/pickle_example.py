import pickle

data = {'name': 'Alice', 'age': 30}

# Serialize to a binary format
with open('data.pkl', 'wb') as f:
    pickle.dump(data, f)

# Deserialize from binary format
with open('data.pkl', 'rb') as f:
    loaded_data = pickle.load(f)
print(loaded_data)  # Outputs: {'name': 'Alice', 'age': 30}