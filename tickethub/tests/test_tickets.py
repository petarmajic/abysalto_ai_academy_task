import requests
from src.tickethub.models.ticket import Ticket

# Dohvati podatke
todos_response = requests.get('https://dummyjson.com/todos')
users_response = requests.get('https://dummyjson.com/users')

todos = todos_response.json()['todos']
users = users_response.json()['users']

# Napravi dictionary korisnika (id -> username)
users_dict = {user['id']: user['username'] for user in users}

# Transformiraj prvi todo u ticket
first_todo = todos[0]
username = users_dict.get(first_todo['userId'])
ticket = Ticket.from_dummyjson(first_todo, username)

print(f"Ticket: {ticket.model_dump()}")
