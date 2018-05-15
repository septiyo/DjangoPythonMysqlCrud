from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.


AGAMA = (
    ('islam','ISLAM'),
    ('kristen', 'KRISTEN'),
    ('budha','BUDHA'),

)


class Member(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    alamat = models.TextField(null=True, validators=[MaxLengthValidator(500)])
    agama = models.CharField(max_length=20, choices=AGAMA, default='null')




    def __str__(self):
        return self.firstname + " " + self.lastname
