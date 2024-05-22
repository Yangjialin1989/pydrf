from django.db import models

# Create your models here.
class FilesModel(models.Model):
    """ 文件上传 """
    file = models.FileField(upload_to='uploads/')

    class Meta:
        db_table = 'files'
        ordering = ['-id']