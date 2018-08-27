from django.db import models
from django.contrib.auth.models import User # imports all users we created either for admin or from the site sign up page

class Product(models.Model):
    title = models.CharField(max_length=140)
    url = models.CharField(max_length=300)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=1)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE) 	
# foreign key connects other models to this model. Different to primary key. In this instance lets us see all users that are connected to this project.
# on_delete is what happens when the other model is deleted this one also deletes the entry in this model.
# We pass user in the function so django knows we want to see the users.
    def __str__(self):
        return self.title

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')	# returns date as day month year.	

    def summary(self):
        return self.body[:100]	
        	
    	
