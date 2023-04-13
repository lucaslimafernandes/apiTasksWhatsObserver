# Configuração do nginx

1. Instalar o Nginx

> sudo apt-get update
> sudo apt-get install nginx

2. Criar um arquivo de serviço para o uvicorn
> sudo nano /etc/systemd/system/my_api.service

```
[Unit]
Description=My API

[Service]
User=username
Group=www-data
WorkingDirectory=/path/to/my/api
TasksMax=20
ExecStart=/usr/bin/env uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
Restart=always

[Install]
WantedBy=multi-user.target
```

3. Iniciar o serviço
> sudo systemctl start my_api

4. Configure o Nginx para encaminhar as solicitações para o Uvicorn:
> sudo nano /etc/nginx/sites-available/my_api

```
server {
    listen 80;
    server_name example.com;

    location / {
        proxy_pass http://localhost:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Substitua "example.com" pelo nome de domínio ou endereço IP do seu servidor.

5. Ative o arquivo de configurações do nginx
> sudo ln -s /etc/nginx/sites-available/my_api /etc/nginx/sites-enabled/
ou então 
> sudo nginx -s reload

6. Reinicie o nginx
> sudo systemctl restart nginx
