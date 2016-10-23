# Volunteer App Backend

### Login
Our app will live on an Amazon Web Services(AWS) EC2 instance and can be accessed through SSH with the folloing command from /login. It will take the <code>.pem</code> that will grant access. If permission errors occur, try running <code>chmod 600 intulit.pem</code>.<br>
<code>
ssh -i intulit.pem bitnami@ec2-54-153-15-7.us-west-1.compute.amazonaws.com
</code>

Our database also lives on AWS as a RDS MySQL 5.6 instance. The database can be accessed through the MySQL command line client with the following credentials:

```
mysql -h volunteer-db.ciqzndzyzwah.us-west-1.rds.amazonaws.com -u admin -p password -P 3306
```

When connected, our tables are alongside Django's resource tables on the <code>volunteerdb</code>.

### Python Dependencies
```
pip install django 
pip install mysqlclient 
pip install graphene_django 
pip install django-filter 
```


### APIs
Reverse geocoding system can be found by POSTing to this REST API.
"""
api.geonames.org/findNearbyPostalCodesJSON?postalcode=93405&country=US&radius=30&username=demo
"""