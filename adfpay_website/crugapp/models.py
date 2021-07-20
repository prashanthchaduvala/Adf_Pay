# from django.db import models
# from django.contrib.auth.models import User
#
#
# class BecomeMember(models.Model):
#     id = models.AutoField(primary_key = True)
#     become_user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='become_users')
#     full_name = models.CharField(max_length=50)
#     mobile = models.IntegerField()
#     email = models.EmailField(max_length=150)
#     password = models.CharField(max_length=20)
#     residential_address = models.CharField(max_length=100)
#     residential_address2 = models.CharField(max_length=100)
#     residential_address3 = models.CharField(max_length=100)
#     country = models.CharField(max_length=50)
#     state = models.CharField(max_length=50)
#     city = models.CharField(max_length=70)
#     zipcode = models.IntegerField()
#     pancard = models.CharField(max_length=20)
#     aadharcard = models.IntegerField()
#     photo = models.FileField(upload_to='become_member/')
#
#     class Meta:
#         verbose_name_plural = 'Become_member'
#
#     def __str__(self):
#         return self.full_name
#
