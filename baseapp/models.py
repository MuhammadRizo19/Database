from django.db import models
import uuid

class Street(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    streetName = models.CharField(max_length=20)

    def __str__(self):
        return self.streetName

class NeedHelp(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    birthDate = models.DateField()
    age = models.IntegerField()
    streetName = models.ForeignKey(Street, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return self.firstName
