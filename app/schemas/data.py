from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CourseCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    area: str = Field(min_length=2, max_length=80)


class CourseRead(CourseCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    email: str = Field(min_length=5, max_length=180)
    course_id: int


class StudentRead(StudentCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ObservationCreate(BaseModel):
    title: str = Field(min_length=2, max_length=160)
    content: str = Field(min_length=1)
    tags: list[str] = Field(default_factory=list)
    course_id: int | None = None


class ObservationRead(ObservationCreate):
    id: str
    created_at: datetime