**TestContact**

Esse é um exemplo de Chatter Bot criado em Python e que utiliza a plataforma [BLiP.ai] (https://blip.ai) como plataforma de integração. Esse bot foi construído para praticar e testar funções básicas de desenvolvimento de bots com WebHook utilizado Python,Flask, e as principais interfaces do BLiP e apenas envia uma resposta padrão para quem se comunicar com ele. É possível ainda definir uma mensagem customizada para ser enviada para contatos específicos.

Hoje você pode ver o funcionamento dele no [Telegram] (https://telegram.me/testcontactbot) e no [Facebook] (https://www.facebook.com/testcontactbot/).

Para utilizar pode ser executado com o Gunicorn, Apache + mod_wsgi, ou qualquer outro servidor compativel com WSGI. Esse bot já contém o que é necessário para ser publicado no Heroku também.

Para utilizar esse bot siga os seguintes passos:

* Crie uma conta na plataforma [BLiP.ai] (https://blip.ai)
* Clone o código e publique uma aplicação do Heroku com ele
* Crie uma variável, ou coloque no arquivo **config.py**, com o nome de *BLIP_KEY* que contenha sua chave da plataforma BLiP
* Siga as instruções da plataforma BLiP par apublicar os canais que deseja.

*Opcional* : Caso queira, pode configurar uma variável com o nome *CUSTOM_USR* contendo os usuários que você queira que receba uma mensagem customizada. Cada usuário deve ser separado por ';'. Esses usuários devem ser os IDs enviados por cada canal, usuários do Telegram, por exemplo, é no formato **ID_UNICO@telegram.gw.msging.net**.
A mensagem customizada é definida na variável *CUSTOM_MSG*.
