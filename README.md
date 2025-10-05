# Renomeador de arquivos

Este projeto é um script em Python desenvolvido para renomear arquivos automaticamente, adicionando uma numeração sequencial no início do nome de cada arquivo.

A contagem começa em 1 e não possui limite máximo.
Os arquivos são renomeados em ordem cronológica, ou seja, o arquivo mais antigo recebe o número 1, e o mais recente recebe o número mais alto da sequência.

O principal objetivo deste script é facilitar a organização de arquivos, especialmente quando é necessário realizar renomeações em massa para que fiquem ordenados corretamente por nome em gerenciadores de arquivos.

## Exemplo

### Antes da renomeação  

- Video blue.mp4  
- Video red.mp4  
- Video green.mp4  
- Video purple.mp4

### Após a renomeação  

- 1 Video blue.mp4  
- 2 Video red.mp4  
- 3 Video green.mp4  
- 4 Video purple.mp4

## Como executar

Siga os passos abaixo para executar o script:

1. Clone o repositório  
```https://github.com/igorferreira007/renomeador-de-arquivos.git```   
2. Abra o terminal (CMD, PowerShell ou outro de sua preferência)  
3. Navegue até a pasta onde o script foi salvo  
```cd caminho/para/a/pasta```  
4. Execute o script com o comando:  
```python nome_do_arquivo.py```
