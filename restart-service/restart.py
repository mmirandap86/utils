#!/usr/bin/env python

import os
import subprocess
import requests

#Recibir servicio como argumento
servicio = sys.argv[1]

# Checkear si servicio esta activo
res = subprocess.run(['systemctl', 'is-active', servicio], stdout=subprocess.PIPE)

if res.stdout.decode('utf-8').strip() != 'active':
    #Iniciar servicio
    subprocess.run(['systemctl', 'start', servicio])

    #Configurar bot telegram y enviar mensaje
    url = 'https://api.telegram.org/bot/sendMessage'
    data = {'chat_id': '-1001541076284', 'text': 'Servicio '+servicio+' reiniciado'}
    requests.post(url, data=data)