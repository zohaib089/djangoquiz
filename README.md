
## Backend development workflow

```json
virtualenv env
pip install -r requirements.txt
python manage.py runserver
Install django-remote-debug
python version 3.x.x
django verion 2.x.x
Add django_remote_debug to your INSTALLED_APPS settings
./manage.py runsever –remote-debug –noreload
```
<!-- per fare sign up endpoints -->
Post Request
http://d196ea58.ngrok.io/rest-auth/registration/

per fare request 
 username,
 email,
 password1,
 password2,
 is_candidate,
 is_admin
 
la risposta sarà come
 token,
 username,
 userId,
 is_candidate,
 is_admin

<!-- per fare Login usi questo end point -->
Post Request
http://d196ea58.ngrok.io/rest-auth/login/

per fare request
username,
password

la risposta sarà come
 token,
 username,
 userId,
 is_candidate,
 is_admin


