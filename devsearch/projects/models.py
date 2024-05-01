from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    #max length is one of the required parameters for charfield
    description = models.TextField(null=True, blank=True)
    # allowed to create null values for a row
    # whenever we're submitting some kind of form or making a post request, we cannot submit this with this, thus we are allowed to subkit this form with this field being empty
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)

    tags = models.ManyToManyField('Tag', blank = True)
    vote_total = models.IntegerField(default=0, null = True, blank = True)
    vote_ratio = models.IntegerField(default=0, null = True, blank = True)


    created = models.DateTimeField(auto_now_add=True)
    #will give us a date and a time stamp
    # whenever created automatically go ahead and generate a timestamp for us  
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    # vaise by default django will create an id for us
    # UUIDField - 16 character consisting of nos and letters and it does have to be unique
    #default=uuid.uuid4 - encoding type right there
    # editable is false - so no one can edit this in the form

    def __str__(self) -> str:
        return self.title
    

class Review(models.Model):
    VOTE_TYPE = (
        ('up','Up Vote'),
        ('down','Down Vote'),

    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    #whenever a project is deleted, all reviews of it are also deleted
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)


    def __str__(self) -> str:
        return self.name    