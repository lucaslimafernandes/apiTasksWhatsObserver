#!/bin/bash

source /home/ubuntu/apiTasksWhatsObserver/ambiente/bin/activate
cd /home/ubuntu/apiTasksWhatsObserver/
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
