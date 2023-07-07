from django.db import models
    
class Journal(models.Model):
    name = models.CharField(max_length=200, null=True)
    about = models.CharField(max_length=200, null=True, blank=True)
    abbrv = models.CharField(max_length=200, null=True, blank = True)
    impact = models.FloatField(null=True, blank=True)
    pic = models.ImageField(default="static/assets/imgs/vaccines-11-00991-g001-550.jpg",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True) # This basically takes a snapshot of when the object was added to the database automatically

    def __str__(self):
        return self.name
    
class Volume(models.Model):
    number = models.IntegerField(null=True)
    journal = models.ForeignKey(Journal, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return str(self.number) +" "+ self.journal.name

class Issue(models.Model):
    number = models.IntegerField(null=True)
    volume = models.ForeignKey(Volume, null=True, on_delete=models.SET_NULL)
    journal = models.ForeignKey(Journal, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null = True) # This basically takes a snapshot of when the object was added to the database automatically

    def __str__(self):
        return str(self.number) + '. Volume' + ' ' + str(self.volume.number) + '. ' + self.volume.journal.name

class Paper(models.Model):
    title = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    institution = models.CharField(max_length=200, null=True)
    keywords = models.CharField(max_length=200, null=True)
    issue = models.ForeignKey(Issue, null=True, on_delete=models.SET_NULL)
    journal = models.ForeignKey(Journal, null=True, on_delete=models.SET_NULL)
    recieved = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True) # This basically takes a snapshot of when the object was added to the database automatically
    doi = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.title

class HomeSlider(models.Model):
    title = models.CharField(max_length=200, null=True)
    body = models.TextField(null=True)
    pic = models.ImageField(default="assets/imgs/vaccines-11-00991-g001-550.jpg",null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.title

class Submission(models.Model):
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phonenumber = models.CharField(max_length=200, null=True)
    institution = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    manuscript = models.FileField(upload_to ='papers/%Y/%m/%d/')
    supplementary =  models.FileField(upload_to ='papers/%Y/%m/%d/')
    journal = models.ForeignKey(Journal, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.firstname + " " + self.lastname





