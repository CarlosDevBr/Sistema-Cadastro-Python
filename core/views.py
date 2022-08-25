from django.shortcuts import render
from random import randint

def home(request):
    cadastro = []
    if request.POST:
        if request.POST['name']:
            cadastro.append(request.POST['name'])
        if request.POST['street']:
            cadastro.append(request.POST['street'])
        if request.POST['complemention']:
            cadastro.append(request.POST['complemention'])
        if request.POST['district']:
            cadastro.append(request.POST['district'])
        if request.POST['city']:
            cadastro.append(request.POST['city'])
        if request.POST['state']:
            cadastro.append(request.POST['state'])
        if request.POST['cep']:
            cadastro.append(request.POST['cep'])
        if request.POST['email']:
            cadastro.append(request.POST['email'])
        print(cadastro)

    arquivo = open('bancodados.txt','a')
    for linha in cadastro:
        arquivo.writelines(linha+'\n')
    arquivo.close()

    return render(request, 'index.html')