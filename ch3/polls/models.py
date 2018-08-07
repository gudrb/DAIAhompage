from django.db import models
# Create your models here.

class Question(models.Model): # 회원가입 신청목록 ,회원목록 텍스트
    question_text=models.CharField(max_length=200)
    def __str__(self):
        return self.question_text
class Choice(models.Model): # 승인대기 회원들
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    git = models.CharField(max_length=200)
    sns = models.CharField(max_length=200)
    student_id = models.IntegerField(default=0)
    phone_num = models.IntegerField(default=0)
    #image = models.FileField(upload_to=None, max_length=100)
    def __str__(self):
        return self.name
class Newmember(models.Model): #승인받은 회원들
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    git = models.CharField(max_length=200)
    sns = models.CharField(max_length=200)
    student_id = models.IntegerField(default=0)
    phone_num = models.IntegerField(default=0)
    #image = models.FileField(upload_to=None, max_length=100)
    def __str__(self):
        return self.name