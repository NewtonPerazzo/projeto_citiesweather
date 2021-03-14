import pycountry_convert
from django.shortcuts import render, redirect
import requests
from app.forms import CidadeForm
from app.models import Cidade
from googletrans import Translator


# Chave da minha conta na API
key = '70b0b23f44fef00dda39631a4583ef94'


# Função responsável somente por iniciar o sistema.
def home(request):
    return render(request, 'app/home.html')


"""
    Função da view que adiciona uma cidade ao banco para ser pesquisada posteriormente.
    Antes de adicionar a cidade ao banco, a função deleta todas as outras cidades para que a pesquisa seja feita somente
    pela cidade no índice 0 da lista de cidades do banco.
"""

def addcidade(request):
    Cidade.objects.all().delete()
    if request.method == 'POST':
        form = CidadeForm(request.POST)
        if form.is_valid():
            cidade = form.save(commit=False)
            cidade.save()
            form.message = "Preenchimento concluído!"
            return redirect('resultado')
    else:
        form = CidadeForm
    return render(request, 'app/addcidade.html', {'form': form})


# Função responsável por buscar o clima da cidade na API e exibir no template.
# A cidade procurada será sempre a primeira cidade na lista do banco (cidades[0]).

def resultado(request):
    cidade = Cidade.objects.all().order_by('-updated')

    """
        Utilizando a documentação da API, passo o nome da cidade procurada (cidade[0].nome), a unidade de medida - Celsius
        (uniq=metric, de acordo com a documentação) e a Key da minha conta.
        Utilizo o captalize() para que a API reconheça o nome do país e da cidade.
    """

    api = requests.get(
        f'http://api.openweathermap.org/data/2.5/weather?q={cidade[0].nome.capitalize()}&units=metric&appid={key}')

    # Passo o resultado para json para fazer a manipulação.
    cidade_infos = api.json()

    # Chamando o método de tradução da lib GoogleTrans para aplicar no nome do país.
    translator = Translator()

    """
        Utilizei esta função da lib pycountry_convert para pegar o nome do país inserido pelo usuário e transformar em sua
        sigla oficial, para poder pesquisar na API (que aceita somente siglas) a cidade de acordo com o país.
        Isso resolve o problema de ter cidades de nomes iguais em países diferentes.
        Outro problema é que a API só aceita nome de países em inglês e com a primeira letra de cada palavra em maiúsculo,
        portanto, utilizo a lib GoogleTrans para fazer a tradução do país e o método title() para formatar o nome.
    """

    pais_traduzido = translator.translate(cidade[0].pais, src='pt', dest='en')

    # Para utilizar a string na biblioteca googletrans, é necessário passar o parâmetro .text.
    sigla = pycountry_convert.country_name_to_country_alpha2(pais_traduzido.text.title())

    # Se a cidade existir na API, a chave "cod" tem o valor 200. Se não, 404. Desta forma renderizo um template padrão
    # para as cidades não encontradas.

    if cidade_infos["cod"] == 200:
        if cidade_infos["sys"]["country"] == sigla:

            # Na API, as informações metereológicas estão dentro de outro dicionário chamado "main". Por isso o clima
            # recebe o valor desta maneira.

            clima = cidade_infos["main"]["temp"]
            sensacao = cidade_infos["main"]["feels_like"]
            minima = cidade_infos["main"]["temp_min"]
            maxima = cidade_infos["main"]["temp_max"]
            umidade = cidade_infos["main"]["humidity"]
            pais = cidade_infos["sys"]["country"]

            context = {
                'cidade': cidade[0].nome.upper(),  # Passo o .upper() somente para questão de estética.
                'clima': clima,
                'sensacao': sensacao,
                'minima': minima,
                'maxima': maxima,
                'umidade': umidade,
                'pais': pais
            }
            return render(request, 'app/resultado.html', context)

        else:
            clima = cidade_infos["main"]["temp"]
            sensacao = cidade_infos["main"]["feels_like"]
            minima = cidade_infos["main"]["temp_min"]
            maxima = cidade_infos["main"]["temp_max"]
            umidade = cidade_infos["main"]["humidity"]
            pais_achado = cidade_infos["sys"]["country"].upper()

            # Como pais_achado vem como sigla, crio a variável pais_achado_nome para exibir o nome para o usuário
            pais_achado_nome = pycountry_convert.country_alpha2_to_country_name(pais_achado)

            # Utilizo a função title() somente por estética
            context = {
                'mensagem': mensagem,
                'cidade': cidade[0],
                'pais': pais_achado_nome,
                'clima': clima,
                'sensacao': sensacao,
                'minima': minima,
                'maxima': maxima,
                'umidade': umidade,
            }
            return render(request, 'app/resultado_diferente.html', context)
    else:
        context = {
            'cidade': cidade[0].nome.title(),
            'pais': cidade[0].pais.title()
        }
        return render(request, 'app/not_found.html', context)


def contatos(request):
    return render(request, 'app/contatos.html')

