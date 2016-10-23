## Volunteer App Backend




### Login
The EC2 instance can be SSHed into through the folloing command from /login. It will take the <code>.pem</code> that will grant access. If permission errors occur, try running <code>chmod 600 intulit.pem</code>.<br>
<code>
ssh -i intulit.pem bitnami@ec2-54-153-15-7.us-west-1.compute.amazonaws.com
</code>

### Python Dependencies
```
pip install django 
pip install mysqlclient 
pip install graphene_django 
pip install django-filter 
```