from rest_framework import serializers

from .models import FilesModel


class FilesSerializer(serializers.ModelSerializer):
    """ 文件上传专用 """
    class Meta:
        model = FilesModel
        fields = '__all__'