from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages



import pickle
model = pickle.load(open("model_pickle_hate","rb"))
vect = model["vect"]
classifier = model["classifier"]

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # stri = self.content
        # input_data = [stri]
        # vectorize_input_data = vect.transform(input_data)
        # result = classifier.predict(vectorize_input_data)[0]
        # if result == "Negative":
        #     return reverse("blog-hate")
        # else:
        return reverse("post-detail", kwargs={"pk": self.pk})
        
    