# Django Azure SQL MWE

## Introduction 
Minimal working example for testing Azure SQL connectivity in Django.

## Getting Started
1.	Install dependencies and set up

Install dependencies:

    sudo apt update
    sudo apt install python3 python3-venv python3-pip
    sudo python3 -m pip install virtualenv virtualenvwrapper

Install the MS SQL odbc driver:
(https://docs.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver15#ubuntu17)

    sudo bash -c "curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -"
    sudo bash -c "curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list > /etc/apt/sources.list.d/mssql-release.list"

    sudo apt-get update
    sudo ACCEPT_EULA=Y apt-get install msodbcsql17
    sudo apt-get install unixodbc-dev

Set up environment variables for virtualenv:

    echo 'export VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'' >> "${HOME}/.bashrc"
    echo "export WORKON_HOME=${HOME}/.virtualenvs" >> "${HOME}/.bashrc"
    echo "source /usr/local/bin/virtualenvwrapper.sh" >> "${HOME}/.bashrc"
    source "${HOME}/.bashrc"

Create the virtualenv, copy the .env file and install the python packages:

    cd python-azuresql-mwe
    mkvirtualenv azure-sql-mwe
    python3 -m pip install -r requirements.txt

Create a .env file with the configuration of your Azure SQL db:
    cp .env.example .env
    nano .env

In this file, update the variables to have the correct values:

    AZURE_AZURE_SQL_DATABASE="DBNAME"
    AZURE_SQL_USER="USERNAME"
    AZURE_SQL_PASSWORD="PASSWORD"
    AZURE_SQL_HOST="domain.com"
    AZURE_SQL_PORT="1433"
    AZURE_SQL_DRIVER="ODBC Driver 17 for SQL Server"

Initialize the database:

    python3 ./djangoazuresql/manage.py makemigrations
    python3 ./djangoazuresql/manage.py migrate

2. Run the application

Run the application using the following commands:

    workon azure-sql-mwe
    python3 ./djangoazuresql/manage.py runserver


Navigate to http://127.0.0.1:8000

3. Deploy to Azure

Install the Azure-cli tooling:

Add your proxy's certificate to Azure-cli's cacert bundle:

    sudo cp /opt/az/lib/python3.6/site-packages/certifi/cacert.pem /opt/az/lib/python3.6/site-packages/certifi/cacert.pem.original
    echo -e "# My Proxy Proxy Cert\n# Installed on $(date +'%Y-%m-%d')" > /tmp/my_proxy_cert.pem
    cat "${path_to_proxy_cert}" >> /tmp/my_proxy_cert.pem
    sudo bash -c "cat /tmp/my_proxy_cert.pem >> /opt/az/lib/python3.6/site-packages/certifi/cacert.pem"

Log in to Azure with az:
    az login
    az account set -s "NAME OF YOUR SUBSCRIPTION"

Publish the Web App:
    
    az webapp up --resource-group "NAME OF YOUR RESOURCE GROUP" --sku B1 --name "NAME OF YOUR APP SERVICE"
