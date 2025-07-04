from pydantic import BaseModel
from typing import Optional


class Ticket(BaseModel):
    id: int
    title: str
    status: str
    priority: str
    assignee: Optional[str] = None
    
    @classmethod
    def from_dummyjson(cls, todo, username=None):
        priorities = ["high", "low", "medium"]
        return cls(
            id=todo["id"],
            title=todo["todo"],
            status="closed" if todo["completed"] else "open",
            priority=priorities[todo["id"] % 3],
            assignee=username
        )
