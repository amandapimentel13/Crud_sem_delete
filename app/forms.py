from django.forms import ModelForm
from app.models import Empresa
from app.models import Produto

# Create the form class.
class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = ['Nome', 'Contato', 'Telefone']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['NomeProd', 'Marca', 'Preco', 'empresa']