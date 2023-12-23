from django import forms

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
