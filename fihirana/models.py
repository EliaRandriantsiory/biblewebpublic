from django.db import models

class fihirana1(models.Model):
    Titre=models.CharField(max_length=100)
    Content=models.TextField()
    ord_diff=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Titre
    
class fihirana2(models.Model):
    Titre=models.CharField(max_length=1000)
    Content=models.TextField()
    ord_diff=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.Titre

class list_fihirana1(models.Model):
    Range_file=models.IntegerField()
    Clés=models.CharField(max_length=10)
    Transpose = models.IntegerField()
    Titre=models.CharField(max_length=1000)
    etat=models.BooleanField(default=False)
    def __str__(self):
        return self.Titre

class list_fihirana2(models.Model):
    Range_file=models.IntegerField()
    Clés=models.CharField(max_length=10)
    Transpose = models.IntegerField()
    Titre=models.CharField(max_length=1000)
    etat=models.BooleanField(default=False)
    def __str__(self):
        return self.Titre

class fhrn_mod(models.Model):
    Titre=models.CharField(max_length=1000)
    fhrn_mod=models.TextField()
    ord_dif=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.Titre
    
class fhrn_ajout(models.Model):
    Titre=models.CharField(max_length=1000)
    content=models.TextField()
    ord_dif=models.CharField(max_length=1000)
    date=models.DateTimeField(auto_now_add=True)
    Clés=models.CharField(max_length=10,null=True,blank=True)
    Transpose = models.IntegerField(null=True,blank=True)
    Range_file=models.IntegerField(null=True,blank=True)
    def __str__(self) :
        return self.Titre
    
class list_fihirana_ajout(models.Model):
    Titre=models.CharField(max_length=1000)
    Clés=models.CharField(max_length=10,null=True,blank=True)
    Transpose = models.IntegerField(null=True,blank=True)
    Range_file=models.IntegerField(null=True,blank=True)
    etat=models.BooleanField(default=False)
    def __str__(self):
        return self.Titre.Titre
    
