from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database_startup import SessionLocal
from . import models, schemas, hashing

router = APIRouter()

# Dependency to get database session
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# User Create Route
@router.post('/', response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(username=user.username, email=user.email, password=hashing.hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# User Login Route
@router.post('/login')
def login_user(request: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials")
    if not hashing.verify_password(request.password, user.password):
        raise HTTPException(status_code=404, detail="Incorrect Password")
    return {"user_id": user.id, "username": user.username, "email": user.email}