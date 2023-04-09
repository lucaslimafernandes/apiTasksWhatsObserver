# apiTasksWhatsObserver

author: Lucas Lima Fernandes
e-mail: lucas.lfernandes@live.com

## Sobre o Projeto

Estudo de uso do design pattern Observer

## Run
uvicorn main:app --reload


## Setting up OCI

update firewall settings
>> sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 5000 -j ACCEPT
sudo netfilter-persistent save

python
>>sudo apt update
>>sudo apt install -y python3-pip
>>pip3 install virtualenv
>>pip3 install virtualenvwrapper

venv wrapper
>> sudo nano .bashrc
# set up Python env
export WORKON_HOME=~/envs
export PATH=$PATH:/home/ubuntu/.local/bin
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
source /home/ubuntu/.local/bin/virtualenvwrapper.sh

>>source ~/.bashrc

and install project

https://docs.oracle.com/en-us/iaas/developer-tutorials/tutorials/flask-on-ubuntu/01oci-ubuntu-flask-summary.htm