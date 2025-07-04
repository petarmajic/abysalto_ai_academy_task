import httpx
from ..models.ticket import Ticket


async def get_all_tickets():
    """Dohvaća sve tickete iz DummyJSON"""
    async with httpx.AsyncClient() as client:
        # Dohvati podatke
        todos_resp = await client.get("https://dummyjson.com/todos")
        users_resp = await client.get("https://dummyjson.com/users")
        
        todos = todos_resp.json()["todos"]
        users = users_resp.json()["users"]
        
        # Mapiranje korisnika
        users_dict = {user["id"]: user["username"] for user in users}
        
        # Kreiraj tickete
        tickets = []
        for todo in todos:
            username = users_dict.get(todo["userId"])
            ticket = Ticket.from_dummyjson(todo, username)
            tickets.append(ticket)
        
        return tickets
