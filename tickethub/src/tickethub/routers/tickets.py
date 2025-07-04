from fastapi import APIRouter, Query, HTTPException
from ..services.external_api import get_all_tickets, get_ticket_by_id

router = APIRouter(prefix="/tickets", tags=["tickets"])

def paginate_tickets(tickets, page: int, limit: int):
    """Paginacija ticketa"""
    start = (page - 1) * limit
    end = start + limit
    paginated = tickets[start:end]
    
    return {
        "tickets": [
            {
                "id": t.id,
                "title": t.title,
                "status": t.status,
                "priority": t.priority,
                "description": t.title[:100]
            }
            for t in paginated
        ],
        "total": len(tickets),
        "page": page,
        "limit": limit
    }


@router.get("/")
async def get_tickets(
    page: int = Query(1),
    limit: int = Query(10),
    status: str = None,
    priority: str = None
):
    """Paginirana lista ticketa + filtiranje po statusu i prioritetu"""

    tickets = await get_all_tickets()
    if status:
        tickets = [t for t in tickets if t.status == status]
    if priority:
        tickets = [t for t in tickets if t.priority == priority]

    return paginate_tickets(tickets, page, limit)
    
@router.get("/search")
async def search_tickets(q: str, page: int = 1, limit: int = 10):
    """Pretraga ticketa po nazivu"""
    tickets = await get_all_tickets()
    tickets = [t for t in tickets if q.lower() in t.title.lower()]
    
    return paginate_tickets(tickets, page, limit)


@router.get("/{ticket_id}")
async def get_ticket_detail(ticket_id: int):
    """Detalji ticketa po ID-u"""
    ticket = await get_ticket_by_id(ticket_id)
    
    if ticket is None:
        raise HTTPException(status_code=404, detail="Ticket not found")
    
    return ticket

