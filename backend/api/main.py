from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Image Truth API",
    description="Backend API for the Image Truth perception game.",
    version="0.1.0"
)

# Allow frontend clients (modify origins in prod)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check route
@app.get("/")
def read_root():
    return {"message": "Image Truth API is running."}

# Placeholder: Add your API routes here
# from .routes import image_challenge, leaderboard, etc.

# app.include_router(image_challenge.router, prefix="/challenge")
# app.include_router(leaderboard.router, prefix="/leaderboard")

