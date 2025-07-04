import httpx
from ..models.ticket import Ticket


async def get_all_tickets():
    """Dohvaća sve tickete iz DummyJSON"""
    async with httpx.AsyncClient() as client:
        todos = (await client.get("https://dummyjson.com/todos?limit=0")).json()["todos"]
        users = (await client.get("https://dummyjson.com/users?limit=0")).json()["users"]
        
        users_dict = {user["id"]: user["username"] for user in users}
        
        # Kreiraj tickete
        tickets = []
        for todo in todos:
            username = users_dict.get(todo["userId"]) 
            ticket = Ticket.from_dummyjson(todo, username)
            tickets.append(ticket)

        return tickets

async def get_ticket_by_id(ticket_id: int):
    """Dohvaća detalje ticketa po ID-u"""
    async with httpx.AsyncClient() as client:
        todo = (await client.get(f"https://dummyjson.com/todos/{ticket_id}")).json()
        user = (await client.get(f"https://dummyjson.com/users/{todo['userId']}")).json()

        return {
            "id": todo["id"],
            "title": todo["todo"],
            "status": "closed" if todo["completed"] else "open",
            "priority": ["high", "low", "medium"][todo["id"] % 3],
            "assignee": user["username"],
            "todo_data": todo,
            "user_data": user
        }


