import json
from django.db import models
import uuid


class Offer(models.Model):
     title = models.CharField(max_length=255)
     companyName = models.CharField(max_length=255)
     Keyword = models.CharField(max_length=255)
     place = models.CharField(max_length=255)



     def toJSON(self):
         return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
   


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=False, null=False)
    
    def __str__(self):
        return self.file.name