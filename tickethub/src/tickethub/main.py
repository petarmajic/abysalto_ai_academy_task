from fastapi import FastAPI
from .routers import tickets

app = FastAPI(title="TicketHub API")

app.include_router(tickets.router)

@app.get("/")
async def root():
    return {"message": "TicketHub API"}
