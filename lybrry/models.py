from django.db import models

# Create your models here.
"""Normal method"""
# class Book(models.Model):
#     title=models.CharField(max_length=200)
#     price=models.IntegerField()

#     def __str__(self):
#         return '{}'.format(self.title)

"""Form method  Foreignkey method"""
class AUTHOR(models.Model):
    name=models.CharField(max_length=200,null=True)

    def __str__(self):
        return '{}'.format(self.name)



class Book(models.Model):
    title=models.CharField(max_length=200)
    price=models.IntegerField(null=True)
    image=models.ImageField(upload_to='book_media')
    quantity=models.IntegerField()

    author=models.ForeignKey(AUTHOR, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return '{}'.format(self.title)