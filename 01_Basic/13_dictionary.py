my_dict = {
    'name': 'om',
    'age': 78
}

print(my_dict['name'])
print(my_dict['age'])

del my_dict['age']  # delete key-value pair

for key, value in my_dict.items():
    print(key, value)




# Server configurations dictionary
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active'}
}

# Retrieving information
def get(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Example usage
server_name = 'server2'
status = get(server_name)
print(f"{server_name} status: {status}")