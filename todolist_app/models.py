from django.db import models
from django.contrib.auth.models import User

class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=300)
    tanggal = models.DateField(default='2022-09-01')
    pelajaran = models.CharField(max_length=25, default='Matematika')
    waktu = models.CharField(max_length=10, default='Malam')
    cara = models.CharField(max_length=25, default='Duduk')
    jam = models.TimeField(default='20:30:30')
    durasi = models.IntegerField(default=30)
    nilai = models.IntegerField(default=90)
    positif = models.TextField(max_length=255, default='None')
    negatif = models.TextField(max_length=255, default='None')
    done = models.BooleanField(default=True)

    # def __str__(self):
    #     return self.task + " -----------    " + str(self.done) + "--------------->      " + str(self.owner)
    
    def __str_(self):
        return self.task
    
    class Meta:
        verbose_name_plural = "Tasks"

