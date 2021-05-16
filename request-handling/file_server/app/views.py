from datetime import datetime
import os
from app.settings import FILES_PATH

from django.shortcuts import render


def file_list(request, date=None):
    template_name = 'index.html'
    files = []
    listdir = os.listdir(path=f"{FILES_PATH}")
    for filename in listdir:
        file_stat = os.stat(f"{FILES_PATH}\\{filename}")
        ctime = datetime.fromtimestamp(file_stat.st_ctime)
        mtime = datetime.fromtimestamp(file_stat.st_mtime)
        if date is None or date == ctime.date():
            files.append({'name': filename,
                          'ctime': ctime,
                          'mtime': mtime
                          })
    context = {'files': files, 'date': date}
    return render(request, template_name, context)


def file_content(request, name):
    with open(f"{FILES_PATH}\\{name}") as f:
        file_content = f.read()
    return render(
        request,
        'file_content.html',
        context={'file_name': name, 'file_content': file_content}
    )
