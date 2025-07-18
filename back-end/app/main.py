from fastapi import FastAPI;
from fastapi.middleware.cors import CORSMiddleware;
from app.api.v1.routes import user
from app.api.v1.routes import auth


app = FastAPI(debug=True);

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(user.router)
app.include_router(auth.router)
