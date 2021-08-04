from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UploadFiles, ZipFileName, CrontabFileText
from .forms import FileModelForm
import zipfile
import boto3
import os
# Create your views here.

def index(request):

    


    if request.method == 'POST':
        data = request.POST
        #music_file = request.FILES.get('music_file')
        music_files = request.FILES.getlist('music_file')
        counter = 0
        for music_file in music_files:
            music_file = UploadFiles.objects.create(
                music_file=music_file,
            )

        zip_file_name = ZipFileName.objects.create(
            zip_file_name=data['zip_file_name'],
        )
        crontab_text = CrontabFileText.objects.create(
            crontab_text=data['crontab_text']
        )

        file = open(r'../mysite/static/files/'+str(zip_file_name)+'.txt', "w")
        file.write(str(crontab_text))
        file.close()

        print(zip_file_name)
        for music_file in music_files:
            while not(os.path.exists(f'../mysite/static/files/{music_file}')):
                counter += 1

        zipfile_ob = zipfile.ZipFile(r'../mysite/static/files/'+str(zip_file_name)+'.zip', "w")
        for music_file in music_files:
            zipfile_ob.write(f'../mysite/static/files/{music_file}', os.path.basename(f'../mysite/static/files/{music_file}'), compress_type=zipfile.ZIP_DEFLATED)
        zipfile_ob.write(f'../mysite/static/files/{zip_file_name}.txt', os.path.basename(f'../mysite/static/files/{zip_file_name}.txt'), compress_type=zipfile.ZIP_DEFLATED)
        zipfile_ob.close()

        ACCESS_KEY = 'AKIA5ZNX4T4CMTDRSHFW'
        SECRET_KEY = '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'

        
        local_file = '../mysite/static/files/'+str(zip_file_name)+'.zip'
        bucket = 'nikita-dev1-bucket'
        s3_file = str(zip_file_name)+'.zip'

        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                          aws_secret_access_key=SECRET_KEY)
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")

        return redirect('index')
    else:
        file = open('../mysite/staticfiles/directory_for_crontab_pattern/crontab_pattern.txt', "r")
        crontab_pattern_text = file.read()
        file.close()
        uploaded_zip_files = ZipFileName.objects.all()
        music_file_form = FileModelForm()
        context = {'uploaded_zip_files': uploaded_zip_files, 'crontab_pattern_text': crontab_pattern_text,
                   'music_file_form': music_file_form}

        return render(request, 'mysite/index.html', context)


def user(request, slug):
    return HttpResponse(f'Пользователь {slug}')