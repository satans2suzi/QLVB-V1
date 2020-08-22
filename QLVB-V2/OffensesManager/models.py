from django.db import models

# Create your models here.


class DomainName(models.Model):
    domainID = models.IntegerField(primary_key=True)
    domainName = models.CharField(max_length=100)

    def __str__(self):
        return self.domainName


class Offenses(models.Model):
    number = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    offensenID = models.IntegerField()
    domainID = models.ForeignKey(
        DomainName, on_delete=models.CASCADE, related_name="DomainName2Offenses")
    descriptions = models.CharField(max_length=1000)
    category = models.CharField(max_length=200)
    sourceIP = models.GenericIPAddressField()
    destinationIP = models.GenericIPAddressField()
    severity = models.IntegerField()

    def __str__(self):
        return self.descriptions
