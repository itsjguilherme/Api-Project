from app.ports.employee_port import EmployeePort
from app.swagger_models.empregadoRequests import CreateEmpregado, UpdateEmpregado

class EmployeeAdapter:
    def __init__(self) -> None:
        pass

    def get_empregado(self):
        return EmployeePort().get_empregado()
    
    def get_empregado_by_id(self, empregado_id):
        return EmployeePort().get_empregado_by_id(empregado_id)
    
    def create_empregado(self, empregado: CreateEmpregado):
        data = empregado.model_dump()
        data['email'] = data['email'].lower()

        return EmployeePort().create_empregado(data)
    
    def update_empregado(self, empregado_id, empregado: UpdateEmpregado):
        data = empregado.model_dump()
        data['email'] = data['email'].lower()

        return EmployeePort().update_empregado(empregado_id, data)
    
    def remove_empregado(self, empregado_id):
        return EmployeePort().remove_empregado(empregado_id)