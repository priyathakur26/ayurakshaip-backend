from uuid import uuid4

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/api/v1/assessments", tags=["Assessments"])


class AssessmentCreate(BaseModel):
    title: str
    description: str


@router.post("")
def create_assessment(data: AssessmentCreate):
    assessment_id = str(uuid4())

    return {
        "assessment_id": assessment_id,
        "status": "created",
        "title": data.title,
    }


@router.get("/{assessment_id}")
def get_assessment(assessment_id: str):
    return {
        "assessment_id": assessment_id,
        "status": "processing",
    }