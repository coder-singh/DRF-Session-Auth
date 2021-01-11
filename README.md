# DRF-Session-Auth

### API Endpoints  
- /api/register/  
method : POST  
payload : {
            "username": "simple",
            "email": "simplea@gmail.com",
            "name": "simple",
            "phone": 9898989899,
            "password": "abcd1#",
            "password2": "abcd1#"
        }

- /api/login/
method : POST
payload : {
            "username": "test",
            "password": "test1#"
        }
        
- /api/logout
method : GET

- /api/profile
method : GET

### How to run the project
- docker-compose up --build
- (in different terminal)  
  - get current running container's id using docker ps
  - docker exec -it <container id> sh
  - python DRF_Session_Auth/manage.py createsuperuser
  
 ### How to test the APIs
 - POST requests can be tested using POSTMAN/SOAPUI
 - GET requests can be tested using admin console
  - log into admin console using admin and password just set
  - Once logged in, visit localhost:8000/api/profile
  - localhost:8000/api/logout will log you out
