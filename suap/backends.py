from social_core.backends.oauth import BaseOAuth2


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

    def get_user_details(self, response):
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
