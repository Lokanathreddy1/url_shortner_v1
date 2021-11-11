Before running the flask app need to run the requirements.txt as below
pip install -r requirements.txt
activate vertual_environment as below command.
source source bin/activate
once this is done need to run below command
flask run
after this take the URL given in the run try testing it from postman.
For example(curl command given below): 
curl -X POST http://127.0.0.1:5000/url_shortner -d 'url=https://www.google.com'
test 
