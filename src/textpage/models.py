from django.db import models

class SnsModel(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  author = models.CharField(max_length=100)
  # 画像をアップロード時にはpillowライブラリが使われるので、pipでインストールする必要あり
  # 前提としてブランクの時にはデフォルトでどこに保存するかの設定をsettings.pyに書き込む必要あり
  images = models.ImageField(upload_to='') # upload_toはどこのディレクトリに画像をアップロードするかの設定
  good = models.IntegerField()
  read = models.IntegerField()
  readtext = models.CharField(max_length=200)