# Importar modulos

## Importar modulo requests

import requests
## Importar modulo urllib

import urllib3

## Desabilitar alertas de certificados não confiáveis
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

## Importar modulo json
import json


# Inicializacao de variaveis e dicionarios

## Inicialização do dicionário 'keys', utilizaremos ele para armazenar o resultado bruto recebido pelo firewall

keys = {}


## Inicialização do dicionário 'tunnel_info' que utilizaremos para armazenar apenas os dados que queremos (IP e PSK)

tunnel_info = {}


##  Inicialização da variável 'count_tunnel' é ela que usaremos para garantir que buscaremos a informação de todos os túneis, independente da quantidade
count_tunnel = 0


# Criação da funcao 'retrieve_keys', note que ela espera um valor para ser inicializada, no caso é o IP do firewall que buscaremos a informação


def retrieve_keys(ip):


## Definição da varíavel 'url', note que ela está juntando 'https://' com o IP que fornecemos a função
	url = 'https://' + ip

##  Definição da chamada que faremos ao firewall. Usuários que fazem uso de vdom, coloquem o VDOM no final, logo após o '='
	command = '//api/v2/cmdb/vpn.ipsec/phase1-interface?plain-text-password=1?vdom='

##  Definição de como nos autenticaremos com o destino, no nosso caso, estamos usando um Token API
	headers = {'Authorization': 'Bearer ' + 'SEU_TOKEN_VAI_AQUI'}

##  Busca dos dados no firewall utilizando os valores anteriores
	r = requests.get(url + command, headers=headers, verify=False)
##  Retornar os dados em formato de texto 

	return(r.text)
   

##  Chamada da função 'retrieve_keys) utilizando como destino o IP to firewall
keys = json.loads(retrieve_keys('IP_DO_FIREWALL'))


##  Contar a quantidade de túneis o firewall possui

number_of_tunnels = (len(keys['results']))


##  Manter em loop a execução da tarefa enquanto não navegarmos em todos os túneis

while count_tunnel < number_of_tunnels:

##  Adicionar as informações que estamos buscando (IP e PSK) ao dicionário que iniciamos anteriormente 'tunnel_info'
	tunnel_info[(keys['results'][count_tunnel]['remote-gw'])] = (keys['results'][count_tunnel]['psksecret'])

##  Adicionar '1' a variável 'count_tunnel'
	count_tunnel = count_tunnel + 1


# Printar no console o resultado


print(tunnel_info)
