from django.shortcuts import render
from pdf2image import convert_from_path
import random, os


def home(request):
    return render(request, 'showpdf/index.html')


def convert_page_one(request):
    found_files = []
    workdir = os.getcwd()
    docs_path = os.path.join(workdir, "media", "docs")
    dir_list = os.listdir(docs_path)

    for i in range(len(dir_list)):
        found_files.append(os.path.join(docs_path, dir_list[i]))

    for i in range(len(dir_list)):
        converted_image_list = []
        images = convert_from_path(found_files[i])
        no_extension = dir_list[i].split(".")[0]
        random_num = random.randrange(10, 900, 3)
        image_name = no_extension + "_" + str(random_num) +'.jpg'
        converted_image_list.append(image_name)
        path_save = os.path.join(workdir, "media", "tmp", image_name)
        images[0].save(path_save, 'JPEG')

    print("Files and directories in '", docs_path, "' :")
    print(converted_image_list)

    context = {
        'data': converted_image_list
    }

    return render(request, 'showpdf/index.html', context)
    