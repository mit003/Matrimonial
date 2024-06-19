from django.db import models

# Create your models here.

class login(models.Model):
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    dp = models.ImageField(upload_to='photos')
    role = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return self.email

class state(models.Model):
    statename = models.CharField(max_length=30)

    def __str__(self):
        return self.statename

class city(models.Model):
    cityname = models.CharField(max_length=30)
    stateid = models.ForeignKey(state,on_delete=models.CASCADE)

    def __str__(self):
        return self.cityname

TYPE = {
    ('M','Male'),
    ('F','Female'),
}

class detail(models.Model):
    lid = models.ForeignKey(login,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    dob = models.DateField()
    address = models.CharField(max_length=100)
    gender = models.CharField(choices=TYPE, max_length=10)
    cityid = models.ForeignKey(city,on_delete=models.CASCADE)
    stateid = models.ForeignKey(state,on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class biodata(models.Model):
    lid = models.ForeignKey(login,on_delete=models.CASCADE)
    pname = models.CharField(max_length=30)
    picture = models.ImageField(upload_to='photos')
    height = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    caste = models.CharField(max_length=30)
    income = models.CharField(max_length=30)
    skintone = models.CharField(max_length=30)
    siblings = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    expectation = models.CharField(max_length=70)
    meternal = models.CharField(max_length=30)
    # native_state = models.ForeignKey(state,on_delete=models.CASCADE)
    # cityid = models.ForeignKey(city,on_delete=models.CASCADE, blank=True)
    mobile = models.IntegerField()

    def __str__(self):
        return self.pname

class choices(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    height = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    caste = models.CharField(max_length=30)
    income = models.CharField(max_length=30)
    skintone = models.CharField(max_length=30)
    siblings = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    expectation = models.CharField(max_length=70)
    meternal = models.CharField(max_length=30)
    native = models.CharField(max_length=30)

    def __str__(self):
        return self.lid

class savelist(models.Model):
    lid = models.ForeignKey(login, on_delete=models.CASCADE)
    bioid = models.ForeignKey(biodata,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  str(self.bioid)



class feedback(models.Model):
    lid = models.ForeignKey(login,on_delete=models.CASCADE)
    ratings = models.CharField(max_length=30)
    comment = models.TextField()



class contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    message = models.TextField()

    def __str__(self):
        return self.name


