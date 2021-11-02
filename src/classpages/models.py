from django.db import models


class Classes(models.Model):
    classes_id = models.IntegerField(max_length=200)
    title = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    faculty = models.CharField(max_length=10)
    department = models.CharField(max_length=20)
    method_eval = models.CharField(max_length=200)
    classform = models.CharField(max_length=200)
    contents = models.CharField(max_length=200)

class C_com(models.Model):
    c_com_id = models.IntegerField(max_length=200)
    classes = models.ForeignKey(Classes, on_delete=models.CASCODE)
    
    c_com_date = models.DateTimeField('date published')
    comments = models.CharField(max_length=200)

class C_evals(models.Model):
    c_evals_id = models.IntegerField(max_length=200)

    classes = models.ForeignKey(Classes, on_delete=models.CASCODE)
    c_rikaido = models.IntegerField(max_length=5)
    c_rakutan = models.IntegerField(max_length=5)