from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status
from pymongo.errors import PyMongoError
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from sqlalchemy.orm import Session

from app.db.mongo import get_observations_collection
from app.db.sql import get_session
from app.models import Course, Student
from app.schemas.data import (
    CourseCreate,
    CourseRead,
    ObservationCreate,
    ObservationRead,
    StudentCreate,
    StudentRead,
)

router = APIRouter(prefix="/api")


@router.post("/courses", response_model=CourseRead, status_code=status.HTTP_201_CREATED)
def create_course(payload: CourseCreate, session: Session = Depends(get_session)):
    course = Course(**payload.model_dump())
    session.add(course)
    try:
        session.commit()
        session.refresh(course)
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(status_code=409, detail="Ya existe un curso con ese nombre") from error
    return course


@router.get("/courses", response_model=list[CourseRead])
def list_courses(session: Session = Depends(get_session)):
    return session.scalars(select(Course).order_by(Course.id)).all()


@router.post("/students", response_model=StudentRead, status_code=status.HTTP_201_CREATED)
def create_student(payload: StudentCreate, session: Session = Depends(get_session)):
    if session.get(Course, payload.course_id) is None:
        raise HTTPException(status_code=404, detail="El curso indicado no existe")
    student = Student(**payload.model_dump())
    session.add(student)
    try:
        session.commit()
        session.refresh(student)
    except IntegrityError as error:
        session.rollback()
        raise HTTPException(status_code=409, detail="Ya existe un estudiante con ese correo") from error
    return student


@router.get("/students", response_model=list[StudentRead])
def list_students(session: Session = Depends(get_session)):
    return session.scalars(select(Student).order_by(Student.id)).all()


@router.post(
    "/observations", response_model=ObservationRead, status_code=status.HTTP_201_CREATED
)
def create_observation(payload: ObservationCreate):
    document = payload.model_dump()
    document["created_at"] = datetime.now(timezone.utc)
    try:
        result = get_observations_collection().insert_one(document)
    except PyMongoError as error:
        raise HTTPException(status_code=503, detail="MongoDB no está disponible") from error
    return {**document, "id": str(result.inserted_id)}


@router.get("/observations", response_model=list[ObservationRead])
def list_observations():
    try:
        documents = get_observations_collection().find().sort("created_at", -1).limit(100)
        return [
            {**document, "id": str(document.pop("_id"))}
            for document in documents
        ]
    except PyMongoError as error:
        raise HTTPException(status_code=503, detail="MongoDB no está disponible") from error