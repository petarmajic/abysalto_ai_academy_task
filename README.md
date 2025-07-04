# abysalto_ai_academy_task

# TicketHub API

TicketHub API je Middleware REST servis za prikupljanje ticketa iz vanjskih izvora. Razvijen je kao dio pristupnog zadatka za Abysalto AI Akademiju 2025.

## Pregled

TicketHub transformira podatke iz DummyJSON servisa u strukturirane tickete organizirane u paginiranu listu s mogućnostima filtriranja pretrage.

### Vanjski izvori podataka

- **Ticketi**: https://dummyjson.com/todos
- **Korisnici**: https://dummyjson.com/users

### Ticket model transformacija

| Polje | Izvor | Transformacija |
|-------|-------|----------------|
| `id` | `todos.id` | Direktno preuzeto |
| `title` | `todos.todo` | Direktno preuzeto |
| `status` | `todos.completed` | `true` → "closed", `false` → "open" |
| `priority` | `todos.id` | `id % 3` → 0="high", 1="low", 2="medium" |
| `assignee` | `users.username` | Mapiranje preko `userId` |

### Implementirani endpointovi

- **GET /tickets** - Paginirana lista ticketa s filtriranjem
- **GET /tickets/{id}** - Detalji ticketa + puni JSON iz izvora
- **GET /tickets?status=<>&priority=<>** - Filtriranje po statusu i prioritetu
- **GET /tickets/search?q=...** - Pretraga ticketa po nazivu

### Korišteni izvori
- https://stackoverflow.com/questions/73700879/interaction-between-pydantic-models-schemas-in-the-fastapi-tutorial
- https://docs.pydantic.dev/latest/
- https://fastapi.tiangolo.com/tutorial/first-steps/#recap
- https://fastapi.tiangolo.com/tutorial/extra-models/
- https://fastapi.tiangolo.com/tutorial/middleware/
- https://www.python-httpx.org/async/

### Korištenje AI alata

Tijekom razvoja koristio sam ChatGPT za početnu strukturu projekta, pydantic transformaciju i async/await pozive. 
