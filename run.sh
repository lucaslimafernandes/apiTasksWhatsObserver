#!/bin/bash

source /home/username/apiTasksWhatsObserver/ambiente/bin/activate
cd /home/username/apiTasksWhatsObserver/
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
