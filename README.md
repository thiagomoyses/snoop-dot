# Projeto Python

Este é um projeto Python que realiza a detecção de ips ativos na rede, dado um range.

## Pré-requisitos

Antes de começar a trabalhar com o projeto, você precisa configurar um ambiente de desenvolvimento Python. Siga os passos abaixo para configurar o ambiente virtual e instalar as dependências necessárias.

## Configuração do Ambiente

1. **Crie um Ambiente Virtual**

   Primeiro, crie um ambiente virtual para isolar as dependências do projeto. No terminal, navegue até o diretório do projeto e execute:

   python3 -m venv venv

   Isso criará um novo diretório chamado venv que conterá o ambiente virtual.

2. **Ative o Ambiente Virtual**

    * no Win:
        venv\Scripts\activate
    
    * No macOS e Linux:
        source venv/bin/activate

    
    Após a ativação do ambiente virtual, você verá (venv) no início da linha de comando, indicando que o ambiente está ativo.

3. **Instale as dependencias**

    Com o ambiente virtual ativado, instale as dependências do projeto utilizando o pip. Execute o seguinte comando para instalar todas as dependências listadas no arquivo requirements.txt:

    pip install -r requirements.txt
