from fastapi import FastAPI

app = FastAPI(
    title="TicketHub API",
    description="Middleware REST servis za tickete",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "TicketHub API"}
