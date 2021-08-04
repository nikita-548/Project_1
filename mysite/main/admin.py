from django.contrib import admin

# Register your models here.
from .models import UploadFiles, ZipFileName

admin.site.register(UploadFiles)
admin.site.register(ZipFileName)