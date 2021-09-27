from django.shortcuts import render, redirect
from app.forms import EmpresaForm
from app.forms import ProdutoForm
from app.models import Empresa
from app.models import Produto


# Views

def home(request):
    data = {}
    data['db'] = Empresa.objects.all()
    return render(request, 'index.html', data)

def form(request):
    data = {}
    data['form'] = EmpresaForm()
    return render(request, 'form.html', data)

def create(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    data['form'] = EmpresaForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Empresa.objects.get(pk=pk)
    form = EmpresaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
    return redirect('home')

def delete(request, pk):
    db = Empresa.objects.get(pk=pk)
    db.delete()
    return redirect ('home')

def homepro(request, empresa_ip):
    data = {}
    data['db'] = Produto.objects.filter(empresa = empresa_ip)
    data['empresa_ip'] = empresa_ip
    return render(request, 'formprod.html', data)

def formprod(request):
    data = {}
    data['viewprod'] = ProdutoForm()
    return render(request, 'formprod.html', data)

def viewprod(request, fk):
    data = {}
    data['db'] = Produto.objects.get(fk=fk)
    return render(request, 'viewprod.html', data)

def novoproduto(request, empresa_id):
    data = {}
    data['empresa_id'] = empresa_id
    data['form'] = ProdutoForm()
    return render(request, 'form_novo_produto.html', data)









