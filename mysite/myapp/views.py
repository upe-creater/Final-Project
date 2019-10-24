# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import os

# Create your views here.
def index(request):
	return render_to_response('index.html')

def network(request):
	return render_to_response('network.html')

def configure(request):
    return render_to_response('graph.html')

def compile(request):
	
    return render(request, 'compile.html', {'what':'Django File Upload'})
 
def upload(request):
    if request.method == 'POST':
        handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        return HttpResponse("Successful")
 
    return HttpResponse("Failed")
 
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')
 
    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)


# def folder(request):
# 	spath = r"/home"

# def folder(path):
#     # subprocess.check_call(['xdg-open', '--', path])
# 	file = open("/home")
# 	# file="/"
#     path=os.getcwd()+file
#     fp=open(path,'r+')


# from tkinter import filedialog
# from tkinter import *

# def browse_button():
#     # Allow user to select a directory and store it in global var
#     # called folder_path
#     global folder_path
#     filename = filedialog.askdirectory()
#     folder_path.set(filename)
#     print(filename)


# root = Tk()
# folder_path = StringVar()
# lbl1 = Label(master=root,textvariable=folder_path)
# lbl1.grid(row=0, column=1)
# button2 = Button(text="Browse", command=browse_button)
# button2.grid(row=0, column=3)

# mainloop() 
# from tkinter import filedialog
# from tkinter import *

# def browse_button():
#     # Allow user to select a directory and store it in global var
#     # called folder_path
#     global folder_path
#     filename = filedialog.askdirectory()
#     folder_path.set(filename)
#     print(filename)


# root = Tk()
# folder_path = StringVar()
# lbl1 = Label(master=root,textvariable=folder_path)
# lbl1.grid(row=0, column=1)
# button2 = Button(text="Browse", command=browse_button)
# button2.grid(row=0, column=3)

# mainloop()
