from django.db import models

class cls_baibl(models.Model):
    bible=models.CharField(max_length=30)
    type_bible=models.CharField(max_length=30)
    nbr_chapitre=models.IntegerField(default=1)
    def __str__(self) :
        return self.type_bible

class vrs_baibl(models.Model):
    bible_vrs = models.CharField(max_length=30)
    chptr=models.IntegerField()
    nbr_vrs=models.IntegerField()
    def __str__(self) :
        return self.bible_vrs

class trad(models.Model):
    bbl_m=models.CharField(max_length=20)
    bbl_fr=models.CharField(max_length=20)
    chpt=models.CharField(max_length=5)
    def __str__(self):
        return self.bbl_m


class baiboly(models.Model):
    bible=models.CharField(max_length=100, blank=True, null=True)
    content_bible=models.CharField(max_length=50000, blank=True, null=True)
    def __str__(self) :
        return f"{self.bible} ({self.content_bible})"

