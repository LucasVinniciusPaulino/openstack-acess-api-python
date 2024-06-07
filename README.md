# Acesso à API OpenStack para listar instâncias usando python:

## Descrição
O projeto foi desenvolvido para interagir com a API do OpenStack utilizando Python, realiza a autenticação na API e acessa os serviços de computação para listar todas as máquinas instâncias. Este projeto é uma demonstração de como integrar e consumir serviços oferecidos pelo OpenStack focando principalmente na autenticação e na listagem de recursos computacionais.

## Objetivo
O projeto tem como objetivo fornecer um exemplo funcional de como autenticar-se na API do OpenStack e acessar a API de computação para listar as máquinas virtuais, também serve como base para outros desenvolvimentos que necessitem interagir com a infraestrutura de nuvem do OpenStack permitindo a automação e gestão de recursos.

## Funcionalidades
- Autenticação na API do OpenStack: Utiliza credenciais de aplicação para obter um token de autenticação.
- Listagem de Máquinas Virtuais: Acessa a API de computação e lista todas as instâncias disponíveis, exibindo as informações de forma estruturada.

## Como usar
- Configuração: Crie um arquivo .env no projeto com variáveis de ambiente contendo suas credenciais para mão deixa-las expostas no código

- Instalação de Dependências: Certifique-se de ter o Python e as bibliotecas requests e python-dotenv instaladas.

- Certifique-se de utilizar a api da sua openstack
