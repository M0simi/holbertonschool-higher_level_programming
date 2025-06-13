#!/usr/bin/env python3
from task_01_pickle import CustomObject

# Create an instance
obj = CustomObject(name="John", age=25, is_student=True)
print("Original Object:")
obj.display()

# Serialize
obj.serialize("object.pkl")

# Deserialize
new_obj = CustomObject.deserialize("object.pkl")
print("\nDeserialized Object:")
if new_obj:
    new_obj.display()
else:
    print("Failed to deserialize object.")
#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Sample data to be serialized
data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# Serialize the data to JSON and save it to a file
serialize_and_save_to_file(data_to_serialize, 'data.json')
print("Data serialized and saved to 'data.json'.")

# Load and deserialize data from 'data.json'
deserialized_data = load_and_deserialize('data.json')
print("Deserialized Data:")
print(deserialized_data)
