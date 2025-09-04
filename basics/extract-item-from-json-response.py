import json

# If the JSON response is received as a string from an API call, it needs to be
# converted into a Python object.
json_string = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_string)

# If the JSON data is being read from a file, use json.load():
#with open('data.json', 'r') as f:
#    data = json.load(f)

# Accessing items in a dictionary
name = data['name']
age = data['age']
print(f"Name: {name}, Age: {age}")

# Accessing items in a list
json_list_string = '[{"item": "apple", "price": 1.0}, {"item": "banana", "price": 0.5}]'
items_list = json.loads(json_list_string)
first_item_name = items_list[0]['item']
first_item_price = items_list[0]['price']
print(f"First item: {first_item_name}, {first_item_price}")

# Accessing nested items
nested_json_string = '{"user": {"id": 123, "details": {"email": "test@example.com"}}}'
nested_data = json.loads(nested_json_string)
user_email = nested_data['user']['details']['email']
print(f"User email: {user_email}")
        
