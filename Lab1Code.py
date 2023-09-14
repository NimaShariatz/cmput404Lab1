import requests

print(requests.__version__)

resp = requests.get("http://google.com")
print(resp)
#Q1: 

#Q2: version 2.31.0

#Q3: version 2.31.0. the same since you installed it using "pip install requests". the same command is used to install it on
#your real computer. "pip install requests" was called both in the venv and on my computer on 2023-09-13 and as of then the latest is 2.31 so obviously its the same version

#Q4:

#Q5: status code "HTTP/1.1 301 Moved Permanently" is returned from curl -i and "HTTP/1.1 200 OK" is returned from curl -iL. A code 
#200 simply stands for it being a succesful action. It can come from any URL.

#Q6: curl https://www.google.com/teapot returns the HTML stuff. curl -i https://www.google.com/teapot returns "HTTP/1.1 418 I'm a Teapot" and curl -iL https://www.google.com/teapot returns the same

