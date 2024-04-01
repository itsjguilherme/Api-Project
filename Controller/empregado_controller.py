from sqlalchemy.orm import Session
from Models.empregado_model import Empregado
from schemas.empregado_schema import EmpregadoSchema
from fastapi import HTTPException, status


def get_empregado(db: Session):
    return db.query(Empregado).all()


def get_empregado_by_id(db: Session, empregado_id: int):
    find_person = db.query(Empregado).filter(Empregado.id == empregado_id).first()
    if find_person is not None:
        return find_person
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee with this id not found")


def create_empregado(db: Session, empregado: EmpregadoSchema, empregado_id: int):
    _empregado = Empregado(
        id = empregado.id,
        name = empregado.name,
        email = empregado.email,
        salary = empregado.salary,
        birth = empregado.birth,
        address = empregado.address)
    
    find_person = db.query(Empregado).filter(Empregado.id == empregado_id).first()
    if find_person is not None:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Employee with this id alredy exists")

    db.add(_empregado)
    db.commit()
    db.refresh(_empregado)
    return _empregado


def remove_empregado(db: Session, empregado_id: int):
    _empregado = get_empregado_by_id(db=db, empregado_id=empregado_id)
    if _empregado is not None:
        db.delete(_empregado)
        db.commit()
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Employee deleted successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee with this id not found")


def update_empregado(db: Session, empregado_id: int, name: str, email: str, salary: float, birth: str, address: str):
    _empregado = get_empregado_by_id(db=db, empregado_id=empregado_id)
    if _empregado is not None:
        _empregado.name = name
        _empregado.email = email
        _empregado.salary = salary
        _empregado.birth = birth
        _empregado.address = address

        db.commit()
        db.refresh(_empregado)
        return _empregado
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee with this id not found")