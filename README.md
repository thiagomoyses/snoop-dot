# Projeto Python | Python Project | Проект на Python | Projet Python

🇧🇷 - Este é um projeto Python que realiza a detecção de IPs ativos na rede, baseado em um Range de IP.

🇷🇺 - Это проект на Python, который выполняет обнаружение активных IP-адресов в сети на основе диапазона IP-адресов.

🇫🇷 - Il s'agit d'un projet Python qui détecte les IP actives dans un réseau, basé sur une plage d'adresses IP.

🇺🇸 - This is a Python project that detects active IPs in a network, based on an IP range.

## Pré-requisitos | Prerequisites | Предварительные условия | Prérequis

🇧🇷 - Antes de começar, você precisa configurar um ambiente de desenvolvimento Python. Siga os passos abaixo para configurar o ambiente virtual e instalar as dependências necessárias.

🇷🇺 - Прежде чем начать, необходимо настроить Python-среду разработки. Следуйте инструкциям ниже, чтобы настроить виртуальную среду и установить необходимые зависимости.

🇫🇷 - Avant de commencer, vous devez configurer un environnement de développement Python. Suivez les étapes ci-dessous pour configurer l'environnement virtuel et installer les dépendances nécessaires.

🇺🇸 - Before starting, you need to set up a Python development environment. Follow the steps below to configure the virtual environment and install the necessary dependencies.

## Configuração do Ambiente | Environment Setup | Настройка окружения | Configuration de l'environnement

1. **Crie um Ambiente Virtual | Create a Virtual Environment | Создайте виртуальную среду | Créer un environnement virtuel**

   🇧🇷 - Primeiro, crie um ambiente virtual para isolar as dependências do projeto. No terminal, navegue até o diretório do projeto e execute:

   🇷🇺 - Сначала создайте виртуальную среду, чтобы изолировать зависимости проекта. В терминале перейдите в каталог проекта и выполните следующую команду:

   🇫🇷 - Tout d'abord, créez un environnement virtuel pour isoler les dépendances du projet. Dans le terminal, accédez au répertoire du projet et exécutez la commande suivante :

   🇺🇸 - First, create a virtual environment to isolate the project dependencies. In the terminal, navigate to the project directory and run:

        python3 -m venv venv


    🇧🇷 - Isso criará um novo diretório chamado venv que conterá o ambiente virtual.

    🇷🇺 - Это создаст новый каталог под названием venv, который будет содержать виртуальную среду.

    🇫🇷 - Cela créera un nouveau répertoire appelé venv qui contiendra l'environnement virtuel.

    🇺🇸 - This will create a new directory named venv that will contain the virtual environment.

2. **Ative o Ambiente Virtual | Activate the Virtual Environment | Активируйте виртуальную среду | Activez l'environnement virtuel**

    Windows:
        venv\Scripts\activate

    macOS/Linux:
        source venv/bin/activate

    🇧🇷 - Após a ativação do ambiente virtual, você verá (venv) no início da linha de comando, indicando que o ambiente está ativo.

    🇷🇺 - После активации виртуальной среды вы увидите (venv) в начале строки команд, что указывает на активность среды.

    🇫🇷 - Après l'activation de l'environnement virtuel, vous verrez (venv) au début de la ligne de commande, indiquant que l'environnement est actif.

    🇺🇸 - After activating the virtual environment, you will see (venv) at the beginning of the command line, indicating that the environment is active.

3. **Instale as dependências | Install the Dependencies | Установите зависимости | Installez les dépendances**

    🇧🇷 - Com o ambiente virtual ativado, instale as dependências do projeto utilizando o pip. Execute o seguinte comando para instalar todas as dependências listadas no arquivo requirements.txt

    🇷🇺 - С активированной виртуальной средой установите зависимости проекта с помощью pip. Выполните следующую команду, чтобы установить все зависимости, указанные в файле requirements.txt

    🇫🇷 - Avec l'environnement virtuel activé, installez les dépendances du projet à l'aide de pip. Exécutez la commande suivante pour installer toutes les dépendances listées dans le fichier requirements.txt

    🇺🇸 - With the virtual environment activated, install the project dependencies using pip. Run the following command to install all dependencies listed in the requirements.txt file

    pip install -r requirements.txt