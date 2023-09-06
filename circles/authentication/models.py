from django.db import models

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=10000)
    email = models.CharField(max_length=256)
    display_name = models.CharField(max_length=128, blank=True)
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    online = models.BooleanField(default=0)
    location_server = models.ForeignKey("main.Server", on_delete=models.CASCADE, blank=True, null=True)
    location_circle = models.ForeignKey("main.Circle", on_delete=models.CASCADE, blank=True, null=True)
    followers = models.ManyToManyField("self", blank=True)
    date_created = models.DateField(blank=True)
    
    def __str__(self):
         return(self.username)

class WhitelistedEmails(models.Model):
    email = models.CharField(max_length=256)

    class Meta:
        verbose_name_plural = "Whitelisted Emails"

    def __str__(self):
         return(self.email)