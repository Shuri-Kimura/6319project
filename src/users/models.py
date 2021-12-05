
from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, RegexValidator
from django.utils import timezone
from django.urls import reverse
import uuid

# Create your models here.

#Users作らなきゃいけない
class MyUserManager(BaseUserManager):
    def create_user(self, username, student_number, password):
        if not username:
            raise ValueError('Users must have an username')
        if not student_number:
            raise ValueError('Users must have an student_number address')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            username=username,
            student_number=student_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, student_number, password):
        if not username:
            raise ValueError('Users must have an username')
        if not student_number:
            raise ValueError('Users must have an student_number address')
        if not password:
            raise ValueError('Users must have a password')
        user = self.model(
            username=username,
            student_number=student_number,
        )
        user.set_password(password)
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(verbose_name='username', max_length=10, unique=True, validators=[MinLengthValidator(5,), RegexValidator(r'^[a-zA-Z0-9]*$',)])
    student_number = models.CharField(verbose_name='学籍番号', unique=True, max_length=7, validators=[MinLengthValidator(7,), RegexValidator(r'^[A-Z0-9]*$',)])
    email = models.EmailField(verbose_name='Email', max_length=50)
    image = models.ImageField(verbose_name='プロフィール画像', upload_to="src/users/static/users/image/", blank=True, null=True)
    user_comment = models.TextField(verbose_name='自己紹介', max_length=300, blank=True, null=True) #文字数？

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    #AbstractBaseUserにはMyUserManagerが必要
    objects = MyUserManager()
    #一意の識別子として使用されます
    USERNAME_FIELD = 'username'
    #ユーザーを作成するときにプロンプ​​トに表示されるフィールド名のリストです。
    REQUIRED_FIELDS = ['student_number']

    def __str__(self):
        return self.username
    
    def get_absolute_url(self):
        return reverse('mypage:mypage', kwargs={'pk': self.pk})


class Classes(models.Model):
    class_id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=50) #文字数？
    teacher = models.TextField(max_length=20) #文字数？
    faculty = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(7)]) #数字は？
    department = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(35)]) #数字は？
    method_eval = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？
    classform = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) #数字は？
    contents = models.TextField()

class Texts(models.Model):
    text_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) #外部キー
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー
    title = models.TextField(max_length=50) #文字数？商品名
    info = models.TextField(max_length=300) #文字数？　商品情報
    sold_flag = models.BooleanField()
    category = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)]) #数字は？カテゴリ
    state =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)]) #数字は?商品状態
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存
    days = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)]) #数字は？お渡しまでの日数
    image1 = models.ImageField(verbose_name='商品画像１', upload_to="src/textpage/static/textpage/image1/", blank=False, null=False)
    #image1 = models.ImageField(verbose_name='商品画像１', upload_to="src/textpage/static/textpage/image1/", blank=True, null=True)
    image2 = models.ImageField(verbose_name='商品画像２', upload_to="src/textpage/static/textpage/image2/", blank=True, null=True)
    image3 = models.ImageField(verbose_name='商品画像３', upload_to="src/textpage/static/textpage/image3/", blank=True, null=True)
    

class Tcom(models.Model):
    tcom_id = models.AutoField(primary_key=True)
    text_id = models.ForeignKey(Texts, on_delete=models.CASCADE) #外部キー
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) #外部キー
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存
    comments = models.TextField(max_length=100) #文字数？

class Ccom(models.Model):
    ccom_id = models.IntegerField(primary_key=True)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) #外部キー
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存
    comments = models.TextField(max_length=100) #文字数？

class Cevals(models.Model):
    ceval_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) #外部キー
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー
    rikai = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) 
    raku = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Uevals(models.Model):
    ueval_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) #評価先
    eval = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Tfavos(models.Model):
    tfavo_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    text_id = models.ForeignKey(Texts, on_delete=models.CASCADE) #外部キー

class Cfavos(models.Model):
    cfavo_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー

class Messages(models.Model):
    message_id = models.IntegerField(primary_key=True)
    title = models.TextField(max_length=30)
    messages = models.TextField()
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存