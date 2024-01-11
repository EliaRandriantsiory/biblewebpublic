from django.db import models

class lesona(models.Model):
    Titre=models.CharField(max_length=1000)
    def __str__(self) :
        return self.Titre
class sousTitre(models.Model):
    sousTitre = models.CharField(max_length=1000,blank=True,null=True)
    titre = models.ForeignKey(lesona, on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self) :
        if self.sousTitre == None:
            return "-"
        else:
            return self.sousTitre
class fanazavana(models.Model):
    fanazavana = models.CharField(max_length=10000,blank=True,null=True)
    tokoSyAndininy = models.CharField(max_length=10000,blank=True,null=True)
    sousTitre= models.ForeignKey(sousTitre, on_delete=models.CASCADE,blank=True,null=True)
    def __str__(self) :
        return self.fanazavana 
