# <img src="pages/img/logo.png" alt="Logo do Sports Center IFCN." width="40px" align="center"> Sports Center IFCN <img src="pages/img/logo.png" alt="Logo do Sports Center IFCN." width="40px" align="center">

O presente repositório é utilizado para armazenar o código do Sports Center IFCN. Este projeto está sendo desenvolvido como método de avaliação da disciplina de Projeto Integrador, requerida no 3º período do curso técnico integrado em Informática, do IFRN *Campus* Currais Novos.

## Sobre

O Sports Center IFCN é uma plataforma online que tem como objetivo principal manter toda a comunidade do IFRN currais-novense sempre atualizada a respeito dos esportes no *campus*, por meio da inserção de diversas funcionalidades no site, como notícias, fotografias, vídeos, história e muito mais.

## Uso

Abra o terminal na raiz do repositório e crie um ambiente virtual.

```bash
python -m venv venv
```

Agora, ative o ambiente virtual.

```bash
. venv/bin/activate
```

Em seguida, instale os pacotes necessários, como mostrado na seção de [Dependências](#dependências).

> Certifique-se de configurar corretamente o arquivo `.env`.

Feitos esses procedimentos, é só fazer as migrações e coletar os arquivos estáticos.

```bash
. scripts/all.sh
```

Pronto, agora o projeto já pode ser executado com o comando abaixo.

```bash
python manage.py runserver
```

Ou, se preferir...

```bash
. scripts/runserver.sh
```

## Ferramentas

As ferramentas utilizadas na aplicação são mostradas na seguinte tabela, juntamente com as suas respectivas versões vigentes.

| Tecnologia | Versão |
|------------|--------|
| Python     | 3.12.1 |
| HTML       | 5      |
| CSS        | 3      |

## Dependências

O projeto possui algumas dependências, as quais estão dispostas na tabela abaixo.

| Pacote                 | Versão             |
|------------------------|--------------------|
| Django                 | >= 4.2.7 e < 4.3   |
| python-dotenv          | >= 1.0.0 e < 1.1   |
| Pillow                 | >= 10.1.0 e < 10.2 |
| mysqlclient            | >= 2.2.0 e < 2.3   |
| mysql-connector-python | >= 8.2.0 e < 8.3   |
| social-auth-app-django | >= 5.4.0 e < 5.5   |
| social-auth-core       | >= 4.5.0 e < 4.6   |

Elas devem ser instaladas utilizando o gerenciador de pacotes do Python, o PyPI.

### Instalação

Com o ambiente virtual ativado, execute o comando abaixo no terminal.

```bash
pip install -r requirements.txt
```

## Padronização

> Os pontos citados abaixo são válidos para a equipe de desenvolvedores.

- As páginas HTML e as estilizações CSS devem ser armazenadas **somente** na pasta `pages`, e as imagens em `pages/img`. A criação de múltiplos arquivos ou diretórios é de livre escolha de cada desenvolvedor.
- A utilização de `class` em vez `id`, tanto para elementos da página HTML, quanto para seletores CSS (salvo casos específicos).
- A adoção de medidas inteiras, no lugar de números decimais, e as unidades `rem`, `%` e `px`. As demais unidades também podem ser utilizadas, mas não devem ser um padrão do projeto.

## Equipe

O time do projeto é composto por 7 pessoas, separadas pelos cargos listados abaixo.

| Nome              | Cargo              |
|-------------------|--------------------|
| Valdyson Henrique | Scrum Master       |
| Sérgio Dantas     | Programador Sênior |
| Gabriel Medeiros  | Programador Sênior |
| João Vitor        | Programador Pleno  |
| Maria Gabriela    | Programadora Plena |
| Jordan Cainã      | Programador Júnior |
| Pedro Samuel      | Programador Júnior |

## Afazeres

- [x] Desenvolver a página de perfil do usuário.
- [ ] Verificar se o usuário é do *campus* Currais Novos (CN).
- [ ] Verificar se algum campo foi alterado quando usuários já autenticados fizerem login.
- [ ] Implementar nos templates do projeto as páginas feitas externamente.
- [ ] Desenvolver a página de treinos para que esta fique dinâmica e personalizável.
