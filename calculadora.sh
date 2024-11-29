#!/bin/bash

echo 'Verificando os recursos necessários.'

sudo apt update
sudo apt install python3

echo 'Inicializando a calculadora.'

python3 calculadora.py
