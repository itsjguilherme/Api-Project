from app.services.empregado_service import EmployeeService

class EmployeePort:
    def __init__(self) -> None:
        pass

    def get_empregado(self):
        return EmployeeService().get_empregado()
    
    def get_empregado_by_id(self, empregado_id):
        return EmployeeService().get_empregado_by_id(empregado_id)
    
    def create_empregado(self, empregado):
        return EmployeeService().create_empregado(empregado)
    
    def update_empregado(self, empregado_id, empregado):
        return EmployeeService().update_empregado(empregado_id, empregado)
    
    def remove_empregado(self, empregado_id):
        return EmployeeService().remove_empregado(empregado_id)