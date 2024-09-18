import requests

def get_users():
    response = requests.get('http://jsonplaceholder.typicode.com/users')
    return response.json()

def get_todos(user_id):
    response = requests.get(f'http://jsonplaceholder.typicode.com/todos?userId={user_id}')
    return response.json()