from django.db import models
import os
import zipfile
# Create your models here.


class UploadFiles(models.Model):
    music_file = models.FileField()
    def __str__(self):
        return os.path.basename(self.music_file.name)

class ZipFileName(models.Model):
    zip_file_name = models.TextField(max_length=200, null=False, blank=False)
    def __str__(self):
        return self.zip_file_name

class CrontabFileText(models.Model):
    crontab_text = models.TextField(max_length=20000, null=False, blank=False)
    def __str__(self):
        return self.crontab_text
