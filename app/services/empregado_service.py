from sqlalchemy.orm import Session
from app.models.empregado_model import Empregado
from app.routers import paginate, instance_update
from fastapi import Response, HTTPException, status
import json
from app.database import get_db


class EmployeeService:
    def __init__(self):
        pass

    def get_empregado(self):
        db = get_db()
        query = db.query(Empregado)
        employees, output = paginate(query, 1, 10)

        for employee in employees:
            output["itens"].append(employee.to_dict())

        return output


    def get_empregado_by_id(self, empregado_id):
        db = get_db()
        find_person = db.query(Empregado).get(empregado_id)
        if not find_person:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Employee with this id not found")
        
        response = {
            "error": False,
            "employee": find_person.to_dict()
        }

        return response


    def create_empregado(self, empregado):
        db = get_db()
        email = empregado.get("email").lower()

        if db.query(Empregado).filter(Empregado.email == email).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already registered")
        
        newEmpregado = Empregado(**empregado)

        db.add(newEmpregado)

        try:
            db.flush()
            db.commit()
            return {"error": False, "message": "Empregado criado com sucesso"}
        
        except:
            db.rollback()
            return {"error": True, "message": "database error"}


    def remove_empregado(self, empregado_id):
        db = get_db()
        employee = db.query(Empregado).filter(Empregado.id == empregado_id).first()

        if not employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="employee not found")
        
        db.delete(employee)
        
        try:
            db.commit()
            return Response(json.dumps({"error": False, "message": "empregado deletado com sucesso"}))

        except:
            db.rollback()
            return Response(json.dumps({"error": True, "message": "database error"}))


    def update_empregado(self, empregado_id, empregado):
        db = get_db()
        email = empregado.get("email").lower()

        employee = db.query(Empregado).get(empregado_id)

        if not employee:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="employee not found")

        if db.query(Empregado).filter(Empregado.email == email).first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="email already registered")

        instance_update(employee, empregado)
        
        try:
            db.commit()
            return {"error": False, "message": "empregado editado com sucesso"}
        
        except:
            db.rollback()
            raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="database error")