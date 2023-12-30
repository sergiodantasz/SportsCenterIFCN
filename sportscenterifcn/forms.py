from django import forms
from django_summernote.widgets import SummernoteWidget

from sportscenterifcn import models


class TreinoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['esporte'].widget.attrs['placeholder'] = 'Ex.: Basquetebol Masculino'
        self.fields['dia_horario'].widget.attrs['placeholder'] = 'Ex.: Sexta: 18h à 19h30'

    class Meta:
        model = models.Treino
        fields = [
            'esporte', 'dia_horario'
        ]

    esporte = forms.CharField(
        min_length=1,
        max_length=50,
        label='Esporte',
    )

    dia_horario = forms.CharField(
        min_length=1,
        max_length=50,
        label='Dia(s) e Horário(s)',
    )


class NoticiaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs['placeholder'] = 'Digite o título da notícia...'
        self.fields['excerto'].widget.attrs['placeholder'] = 'Digite o excerto (descrição rápida) da notícia...'

    class Meta:
        model = models.Noticia
        fields = [
            'capa', 'titulo', 'excerto', 'conteudo'
        ]

    capa = forms.ImageField(
        label='Capa'
    )

    titulo = forms.CharField(
        min_length=1,
        max_length=200,
        label='Título'
    )

    excerto = forms.CharField(
        min_length=1,
        max_length=200,
        label='Excerto'
    )

    conteudo = forms.CharField(
        widget=SummernoteWidget(),
        min_length=1,
        max_length=50000,
        label='Conteúdo'
    )


class ArquivoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titulo'].widget.attrs['placeholder'] = 'Digite o título do arquivo...'

    class Meta:
        model = models.Arquivo
        fields = [
            'titulo'
        ]

    titulo = forms.CharField(
        min_length=1,
        max_length=200,
        label='Título'
    )


class AnexoArquivoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['anexo'].widget.attrs['multiple'] = True

    class Meta(ArquivoForm.Meta):
        model = models.AnexoArquivo
        fields = [
            'anexo'
        ]
