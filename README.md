# Messenger Bot with Heroku
### Configurando ambiente

Criar diretório para a aplicação e o ambiente virtual
```bash
mkdir botmessenger
cd botmessenger
pyenv virtualenv 3.5.0 botmessenger
pyenv activate botmessenger
```
Instalar flask, requests e gunicorn
```bash
pip install Flask
pip install requests
pip install gunicorn
```

### Heroku
Instalar o heroku toolbelt
https://devcenter.heroku.com/articles/heroku-cli

Realizar o login no heroku
```bash
heroku login
```
Criar o arquivo requirements.txt com os módulos instalados:
```bash
pip freeze > requirements.txt
```
Criar o arquivo runtime.txt e adiciona a versao mais proxima do heroku:
```bash
echo python-3.5.2 > runtime.txt
```
Criar o arquivo Procfile com o conteúdo:
```bash
echo "web: gunicorn index:app" > Procfile
```
### Facebook
* crie uma nova página no Facebook
* crie um novo app para Messenger e vincule à página criada.

Crie o arquivo .env com o conteúdo:
FB_ACCESS_TOKEN=<token gerado após vincular o app à página>
FB_VERIFY_TOKEN=<digite aqui uma frase de seguranca>

### Deploy in Heroku

Criar um repositório git
```bash
git init
```

Criar o arquivo .gitignore com o conteúdo:
.env
*pyc
__pycache__

Adicionar tudo ao git
```bash
git add .
```
Fazer o commit:
```bash
git commit -m "project my bot"
```
Criar uma app no Heroku:
```bash
heroku apps:create nome_da_sua_app
```
Fazer o heroku ler as informações do .env:
```bash
heroku config:push
```
Realizar o deploy:
```bash
git push heroku master --force
```
(agora já é possível acessar via browser pelo endereço gerado e também no dashboard do heroku)

### Webhooks
Nas configurações do app no Facebook:
  * Seu aplicativo precisa ter o campo Ícone do aplicativo (1024 x 1024) definido. 
  * Seu aplicativo precisa ter o campo URL da Política de Privacidade definido. (nome_do_seu_app.heroku.com/privacy)
  * Seu aplicativo precisa ter o campo Categoria definido.
  * Em URL de retorno de chamada, coloque a url do heroku
  * Em Verificar Token, coloque a frase que vc digitou na opção FB_VERIFY_TOKEN, do arquivo .env
  * Marque a opção "messages" e clique em salvar
  * Agora, em webhooks, selecione a página que você criou e clique em inscrever

Em avaliação de aplicativo do messenger:
 * Clique em adicionar ao envio na opção pages_messaging
 * Clique em editar notas
 * Selecione a página para vincular o bot e marque a opção: "Sua experiência do Messenger inclui respostas automatizadas (por exemplo: bots)"
 * Insira o seguinte exemplo de comando:<br>
   Comando: oi<br>
   Resposta: olá, tudo bem?

  **Clique em salvar e aguarde ser liberado :)**
