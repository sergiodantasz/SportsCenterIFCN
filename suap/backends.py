from datetime import datetime

from django.utils.timezone import make_aware
from social_core.backends.oauth import BaseOAuth2

from sportscenterifcn.models import Usuario
from utils.usuario import formatar_url_foto


class SuapOAuth2(BaseOAuth2):
    name = 'suap'
    AUTHORIZATION_URL = 'https://suap.ifrn.edu.br/o/authorize/'
    ACCESS_TOKEN_URL = 'https://suap.ifrn.edu.br/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'
    ID_KEY = 'identificacao'
    RESPONSE_TYPE = 'code'
    REDIRECT_STATE = True
    STATE_PARAMETER = True
    USER_DATA_URL = 'https://suap.ifrn.edu.br/api/eu/'
    DEFAULT_SCOPE = [
        'identificacao', 'email', 'documentos_pessoais',
    ]

    def get_user_details(self, response):
        dados = {
            'matricula': response['identificacao'],
            'nome_social': response['nome_social'],
            'nome_registro': response['nome_registro'],
            'primeiro_nome': response['primeiro_nome'],
            'ultimo_nome': response['ultimo_nome'],
            'email_pessoal': response['email_secundario'],
            'email_escolar': response['email_google_classroom'],
            'email_academico': response['email_academico'],
            'campus': response['campus'],
            'foto': response['foto'],
            'tipo_usuario': response['tipo_usuario'],
            'cpf': response['cpf'],
            'data_nascimento': response['data_de_nascimento'],
            'sexo': response['sexo'],
        }
        if dados['nome_social']:
            primeiro_nome, *_, ultimo_nome = dados['nome_social'].split()
            dados['primeiro_nome'] = primeiro_nome
            dados['ultimo_nome'] = ultimo_nome
            dados['nome'] = f'{primeiro_nome} {ultimo_nome}'
        else:
            dados['nome'] = f'{response['primeiro_nome']} {response['ultimo_nome']}'
        dados['foto'] = formatar_url_foto(dados['foto'])
        data_nascimento = make_aware(datetime.strptime(dados['data_nascimento'], '%Y-%m-%d'))
        dados['data_nascimento'] = data_nascimento
        if len(Usuario.objects.filter(pk=response['identificacao'])) == 0:
            usuario = Usuario.objects.create(**dados)
            usuario.save()
        else:
            campos = (
                'matricula', 'nome_social', 'nome_registro', 'primeiro_nome',
                'ultimo_nome', 'email_pessoal', 'email_escolar', 'email_academico',
                'campus', 'foto', 'tipo_usuario', 'cpf', 'data_nascimento', 'sexo'
            )
            usuario = Usuario.objects.get(pk=response['identificacao'])
            for campo in campos:
                if getattr(usuario, campo) != dados[campo]:
                    setattr(usuario, campo, dados[campo])
        return {
            'username': response.get('identificacao'),
            'first_name': response.get('primeiro_nome'),
            'last_name': response.get('ultimo_nome'),
            'email': response.get('email_secundario'),
        }

    def user_data(self, access_token, *args, **kwargs):
        return self.request(
            url=self.USER_DATA_URL,
            method='GET',
            data={
                'scope': kwargs['response']['scope'],
            },
            headers={
                'Authorization': f'Bearer {access_token}',
            },
        ).json()
