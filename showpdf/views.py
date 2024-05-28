from django.shortcuts import render
from pdf2image import convert_from_path
import random, os


def home(request):
    return render(request, 'showpdf/index.html')


def convert_page_1():
    workdir = os.getcwd()
    docs_path = os.path.join(workdir, "media", "docs")
    dir_list = os.listdir(docs_path)
    print("Files and directories in '", docs_path, "' :")
    # prints all files
    print(dir_list)

    for i in range(len(dir_list)):
        converted_image_list = []
        images = convert_from_path(dir_list[i])
        no_extension = dir_list[i].split(".")[0]
        random_num = random.randrange(10, 900, 3)
        image_name = no_extension + random_num +'.jpg'
        converted_image_list.append(image_name)
        images[0].save("/media/tmp/" + image_name, 'JPEG')

    return converted_image_list