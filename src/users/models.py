from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, RegexValidator
from django.utils import timezone

# Create your models here.

#Users作らなきゃいけない
class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('Users must have an username')
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(verbose_name='username', max_length=10, unique=True, validators=[MinLengthValidator(5,), RegexValidator(r'^[a-zA-Z0-9]*$',)])
    student_number = models.CharField(verbose_name='学籍番号', max_length=7, unique=True, validators=[MinLengthValidator(7,), RegexValidator(r'^[A-Z0-9]*$',)])
    email = models.EmailField(verbose_name='Email', max_length=50, unique=True)
    image = models.ImageField(verbose_name='プロフィール画像', upload_to="image/", blank=True, null=True)
    user_comment = models.TextField(verbose_name='自己紹介', max_length=300, blank=True, null=True) #文字数？

    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    #AbstractBaseUserにはMyUserManagerが必要
    objects = MyUserManager()
    #一意の識別子として使用されます
    USERNAME_FIELD = 'student_number'
    #ユーザーを作成するときにプロンプ​​トに表示されるフィールド名のリストです。
    REQUIRED_FIELDS = ['username', 'student_number']

    def __str__(self):
        return self.username


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
    text_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE) #外部キー
    class_id = models.ForeignKey(Classes, on_delete=models.CASCADE) #外部キー
    info = models.TextField(max_length=300) #文字数？
    sold_flag = models.BooleanField()
    category = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)]) #数字は？
    state =  models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)]) #数字は?
    date = models.DateTimeField(default=timezone.now) #レコード登録時の日本時間が保存
    days = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)]) #数字は？

class Tcom(models.Model):
    tcom_id = models.IntegerField(primary_key=True)
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