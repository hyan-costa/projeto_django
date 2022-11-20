from django.forms import ModelForm
from app_servicos.models import Servico, CategoriaManutencao

class FormServico(ModelForm):
    class Meta:
        model=Servico
        exclude = ['protocolo','finalizado']

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
            self.fields[field].widget.attrs.update({'placeholder':field})
        lista = list()
        for x, y in self.fields['categoria_manutencao'].choices:
            categoria = CategoriaManutencao.objects.get(titulo=y)
            lista.append((x.value, categoria.get_titulo_display()))
        self.fields['categoria_manutencao'].choices = lista