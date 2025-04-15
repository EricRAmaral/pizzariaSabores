from django import forms # Importa o módulo de forms do django
from .models import Paciente
from .models import Medico

# Criando o form baseado no model Paciente(ModelForm)
class PacienteForm(forms.ModelForm):
    class Meta: # A classe meta serve para configurar o form
        model = Paciente # Define qual é model que o form representa
        fields = ['nome','sobrenome','email','telefone','mensagem',] # São os campos que serão exibidos no form (HTML).

class MedicoForm(forms.ModelForm):
    class Meta: 
        model = Medico
        fields = ['nome','sobrenome','crm','email','telefone','mensagem','especialidade_id',]