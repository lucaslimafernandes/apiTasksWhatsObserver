sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 5000 -j ACCEPT
sudo netfilter-persistent save

sudo apt update
sudo apt install -y python3-pip
sudo apt install -y python3-venv

git clone https://github.com/lucaslimafernandes/apiTasksWhatsObserver.git
cd apiTasksWhatsObserver

# python
python3 -m venv ambiente
source ambiente/bin/activate

python -m pip install --upgrade pip
pip install -r requirements

# executar o comando abaixo e fechar a janela
#nohup uvicorn main:app --host 0.0.0.0 --port 5000