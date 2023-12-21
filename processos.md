<!--
title: 'processos.md'
author: 'Elias Albuquerque'
created: '2023-12-20'
update: '2023-12-20'
-->


# Procedimentos para desenvolvimento de bots para automação

1. Entenda a necessidade do projeto e a solução final
2. Descreva em detalhes os requisitos e os procedimentos a serem seguidos
3. Dividir o projeto em etapas e transcreva a solução em código
4. Teste a aplicação
5. Implantação do projeto




## Permissão para rodar scripts no Windows

Usando o terminal com privilégios de administrador, digite o seguinte comando:

```powershell
Set-ExecutionPolicy RemoteSigned
```

Esta política permite que scripts que você escreveu em seu computador local 
sejam executados sem assinatura, enquanto quaisquer scripts baixados da 
Internet devem ser assinados por um editor confiável.

> O objetivo principal da política `RemoteSigned` é impedir que scripts 
> potencialmente maliciosos baixados da Internet sejam executados em seu 
> sistema, a menos que sejam assinados por um editor confiável. Isso 
> adiciona uma camada de segurança ao garantir que scripts de fontes 
> desconhecidas ou não confiáveis não possam ser executados sem sua 
> permissão explícita. Para checar a configuração atual use o comando: 
> `Get-ExecutionPolicy` no terminal.




## Venv - Ambientes virtuais

Crei um ambiente virtual para instalar os módulos (dependências) do seu projeto. 
    
> As *dependências* do projeto são os módulos externos que foram utilizados no 
> desenvolvimento da aplicação, adicionando funcionalidades específicas no 
> projeto.

Os comandos a seguir atendem ao **SO** **Windows** e terminal **Powershell**:

1. Vá até a pasta do projeto e crie um novo ambiente com o comando:

    ```powershell
    python -m venv <nome_do_ambiente>
    ```

    Substitua `<nome_do_ambiente>` com um nome que tenha ligação com o projeto 
    em desenvolvimento para que tenha uma coerência no seu desenvolvimento.

    Para confirmar se o ambiente foi criado, use o comando `dir` no terminal e 
    vai aparecer uma mensagem com detalhes do ambiente e o nome.

2. Ativando o ambiente virtual:
   
    Ainda no diretório do projeto onde estamos criando um ambiente virtual, use 
    o seguinte comando:

    ```powershell
    .\<nome_do_ambiente>\Scripts\activate
    ```

    > NOTA:
    > É importante que o `ExecutionPolicy` tenha permissão para rodar scripts
    > criados na sua própria máquina. Caso não tenha certeza, use o camando 
    > `Get-ExecutionPolicy` e verifique se a resposta no terminal foi 
    > `RemoteSigned`. Se não, use o comando `Set-ExecutionPolicy RemoteSigned`.

    Nesse momento já temos um ambiente virtual criado e ativado, podendo ser 
    verificado com o comando `pip list`, que irá retornar somente os módulos 
    `pip` e `setuptools`.

3. Criando uma lista de requisitos (dependências):

    Para gerar uma lista das dependências do projeto:

    ```powershell
    pip freeze > requirements.txt
    ```

    Esse comando irá criar um arquivo `.txt` com os módulos instalados no 
    ambiente em que estiver desenvolvendo, nesse caso, ao criar um ambiente 
    virtual para o projeto e instalar os módulos nesse ambiente, `pip freeze` 
    irá listar esses módulos no arquivo `requirements`. Caso esteja no ambiente 
    global, irá listar os módulos instalados no ambiente global.




## Alternativa à listagem de dependências

Outra maneira de criar o arquivo `requirements.txt` e listar todas as 
dependências do projeto é usar o módulo `pipreqs`:


1. Para instalar o módulo `pipreqs`:

    ```powershell
    pip install pipreqs
    ```

2. Execute `pipreqs` no diretório do projeto:

    ```powershell
    pipreqs /diretorio/projeto/
    ```
    <!-- pipreqs /path/to/your/project/ -->

    ou, se já estiver no diretorio:

    ```powershell
    pipreqs .
    ```

    E, caso já exista o arquivo `requirements.txt`:

    ```powershell
    pipreqs . --force
    ```

Este módulo percorre o diretório do projeto e lista todos os módulos utilizados 
na aplicação, sem a necessidade de criar ambientes virtuais. Assim, pode-se 
utilizar o ambiente global para a instalação de módulos externos.