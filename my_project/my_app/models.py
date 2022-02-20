from django.db import models

# Create your models here.


class UserInfo(models.Model):
    "Information saving for the VESIT user"
    name = models.CharField(max_length=100)
    date_recorded = models.DateTimeField(auto_now_add=True)
    email_address = models.EmailField(max_length=250, blank=True)
    roll_no = models.IntegerField()
    feedback = models.CharField(max_length=1000)
    rating = models.IntegerField(max_length=10)

    def __str__(self):
        "Return a string representation of all the information"
        return self.name


class Entry(models.Model):
    name = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    date_recorded = models.DateTimeField(auto_now_add=True)
    email_address = models.EmailField(max_length=250, blank=True)
    roll_no = models.IntegerField()
    feedback = models.CharField(max_length=1000)
    rating = models.IntegerField(max_length=10)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        return self.name
