from django.db import models
import uuid

class UserSignUpModel(models.Model):
    __tablename__ = "user"

    uuid = models.UUIDField(default=uuid.uuid4, primary_key=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    name = models.CharField(max_length=30)
    created_on = models.DateTimeField()
    last_modified_on = models.DateTimeField() 
