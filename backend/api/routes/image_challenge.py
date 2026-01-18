from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

router = APIRouter()

# Pydantic model for incoming data
class ChallengeResponse(BaseModel):
    user_id: Optional[str] = Field(default=None, description="Anonymous or registered user ID")
    image_pair_id: str
    selected_image: str  # 'left' or 'right'
    correct_answer: str  # 'left' or 'right'
    time_taken: float  # in seconds
    marked_regions: Optional[list[str]] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.utcnow)

# Placeholder database (in-memory for now)
responses_db = []

@router.post("/submit")
def submit_response(response: ChallengeResponse):
    try:
        # Store response (in-memory for now, swap with DB later)
        responses_db.append(response.dict())
        return {"status": "success", "message": "Response submitted."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error submitting response: {e}")

