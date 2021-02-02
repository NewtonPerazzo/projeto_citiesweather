# Projeto Cities Weather 🚀

<h4>Este projeto tem como objetivo pôr em prática alguns conhecimentos de Python, tais como:</h3>

* Desenvolvimento Web 💻
* Manipulação de API ⚙
* Manipulação do ORM do Django 🐍
* Manipulação de Banco de Dados 🏢
* Utilização de bibliotecas 📚
* Desenvolvimento Frontend 🎨


<h3>Linguagem, Frameworks, Bibliotecas e Frontend utilizados 💼</h3>

```
* Linguagem: Python 3;
* Framework Web: Django;
* Bibliotecas:
    - requests;
    - pycountry_convert;
    - googletrans.
* Bootstrap, HTML e CSS.

````


<h3>Como rodar o projeto em sua máquina 🛠</h3> 

<h5>
Você pode baixar o repositório pelo próprio GitHub ou cloná-lo através do Git + sua chave SSH, utilizando o comando
 
`git clone {chave SSH}` 
    
Após baixar o repositório em sua máquina e abri-lo com uma IDE de sua preferência, é necessário ativar 
a máquina virtual (VirtualEnv). 
<p>No terminal, execute os seguintes comandos: </p> 

    cd .venv\Scripts  # Para abrir o .exe ativador da VirtualEnv
    activate  # Executando o .exe
    cd {caminho do diretório onde encontra-se o projeto}  # Voltando ao diretório principal para executar o servidor
Ativada a VirtualEnv, basta passar o comando, também no terminal, `python manage.py runserver` para o servidor ser startado. Será informado o link 
`http://127.0.0.1:8000/` e basta acessá-lo para ver o site funcionando.
</h5>

<h3>Explicando a funcionalidade do sistema ⛅</h3>

<h5>
<p>O projeto Cities Weather funciona basicamente para informar o clima de várias cidades do mundo. Utilizei a API Open 
Weather para realizar as pesquisas. Na página inicial tem o menu, com a logo do sistema e meus contatos principais, 
e a apresentação do site.</p> 
<p>Como rodapé, tem as referências principais do conteúdo.
Para ver o clima, basta clicar no botão de "Adicionar cidade" e inserir o nome do município e seu respectivo país
que o programa redirecionará para as informações de clima daquela cidade no momento.
Clicando em voltar, é possível ir para a página inicial.</p>

Ao adicionar a cidade e o país, os dados vão para o Banco de Dados SQLite padrão e, posteriormente, são passados como
argumento de pesquisa na API. Caso sejam encontradas informações, as informações são tratadas na ```view```,
renderizada no template e exibido. Ao voltar para o início, os dados inseridos no banco são automaticamente excluídos
para evitar dados desnecessários no banco e consumir memória. Caso não sejam encontradas, é renderizado um
template padrão de "não encontrado", possibilitando uma nova busca.

</h5>

<h3>Conclusão ✅</h3>
<h5>
<p>O projeto foi bastante proveitoso, visto que foi necessário entender primeiro a API para depois fazer o código, 
servindo de lição para projetos futuros. A utilização de libs também foi bastante útil, pois ajudou a resolver alguns
problemas da API que encontrei, tais como: </p>
    
    * A API não tem em seu arquivo JSON o nome do país e sim a sigla. Como inseri o campo de país no formulário para evitar cidades 
    de nomes iguais em países diferentes, tive que utilizar a lib `pycountry_convert` para transformar o nome do país em sigla;
    * O usuário escreverá o nome dos países em português, porém a lib pycountry_convert só aceita nomes em inglês, por isso foi
    necessária a utilização da lib googletrans;
   
<p>Foi possível mais uma vez trabalhar e reforçar os conceitos de desenvolvimento web, como parte do CRUD e a manipulação de dados 
no banco, bem como os conceitos lógicos e básicos de programação para que o sistema funcionasse (exemplos: listas, index,
funções de string e formatação).</p>
<p>Por fim, pude praticar e melhorar também a programação frontend, que não é necessariamente minha melhor skill (visto
que sou mais adepto ao backend), mas que é crucial entender, tanto a parte de exibição em templates, quando a de
estilização com CSS, para facilitar o entendimento geral de um sistema.</p>
</h5>
