"""
    Arquivo de testes de usuários.
"""
import uuid

def test_read_all_employee( client_app ):
    response = client_app.get("/employee/all")
    
    assert response.status_code == 200
    assert response.json().get("error") == False

# def test_read_view_employee(client_app):
#     response = client_app.get("/employee/view/{empregado_id}")
#     assert response.status_code == 200
#     assert response.json().get("error") == False

def test_create_employee( client_app ):
    create_employee = {
        "name": "Guilherme",
        "email": "teste@email.com",
        "salary": 1000.24,
        "birth": "14/02/2002",
        "address": "Rua Teste, 123 - Testador"
    }
    response = client_app.post("/employee/add", json=create_employee)

    assert response.is_success
    assert response.json().get("error") == False

def test_create_employee_with_email_repeated( client_app ):

  employee_to_create = {
        "name": "Teste",
        "email": "testador@email.com",
        "salary": 1000.24,
        "birth": "14/02/2002",
        "address": "Rua Teste, 123 - Testador" 
  }
  response = client_app.post("/employee/add", json=employee_to_create)
  response_json = response.json()

  assert response.status_code == 409
  assert "error" in response_json
  assert "message" in response_json
  assert response_json.get("error") == True


# def test_update_employee(client_app):
#     update_employee = {
#         "name": "Daniel",
#         "email": "dantrens@email.com",
#         "salary": 198000.24,
#         "birth": "03/05/2003",
#         "address": "Rua Teste, 12345 - Testador"
#     }
#     response = client_app.put("/employee/edit", json=update_employee)
#     assert response.status_code == 202
#     assert response.json().get("error") == False


# def test_delete_user(client_app):
#     response = client_app.delete("/employee/delete/{empregado_id}")
#     assert response.status_code == 200
#     assert response.json() == {
#         "Status": "Success",
#         "Message": "User deleted successfully",
#     }