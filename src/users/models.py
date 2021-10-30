from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.

#Users作らなきゃいけない

class Classes(models.Model):
    class_id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=50) #文字数？
    teacher = models.TextField(max_length=50) #文字数？
    faculty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？
    department = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？
    method_eval = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？
    classform = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？
    contents = models.TextField(max_length=50) #文字数？

class Texts(models.Model):
    text_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #外部キー
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー
    info = models.TextField(max_length=50) #文字数？
    sold_flag = models.BooleanField()
    category = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？
    state =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は?
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存
    days = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？

class Tcom(models.Model):
    tcom_id = models.IntegerField(primary_key=True)
    text_id = models.ForeignKey(Texts, on_delete=models.CASCADE) #外部キー
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #外部キー
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存
    comments = models.TextField(max_length=50) #文字数？

class Ccom(models.Model):
    ccom_id = models.IntegerField(primary_key=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #外部キー
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存
    comments = models.TextField(max_length=50) #文字数？

class Cevals(models.Model):
    ceval_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #外部キー
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー
    rikai = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？
    raku = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？

class Uevals(models.Model):
    ueval_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #評価先
    eval = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？

class Tfavos(models.Model):
    tfavo_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text_id = models.ForeignKey(Texts, on_delete=models.CASCADE) #外部キー

class Cfavos(models.Model):
    cfavo_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー

class Messages(models.Model):
    message_id = models.IntegerField(primary_key=True)
    messages = models.TextField(max_length=50) #文字数？
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存