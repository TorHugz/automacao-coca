# 🥤 Automação da Coca-Cola de Terça

Este projeto roda um script automatizado toda terça-feira usando **GitHub Actions** para enviar uma notificação no **Slack**, avisando quem é a pessoa responsável por pagar a Coca-Cola da equipe no dia.

## 🛠️ Passo a Passo para colocar no ar:

### 1. Criando o Webhook no Slack
Para o código conseguir mandar mensagem no seu Slack, ele precisa de uma "URL de Webhook". Para criar:
1. Vá no seu workspace do Slack no computador.
2. Acesse a página de criação de Apps: [https://api.slack.com/apps](https://api.slack.com/apps)
3. Clique em **Create New App** > **From scratch**.
4. Dê um nome (ex: `Aviso da Coca`) e escolha o seu Workspace. Clique em **Create App**.
5. No menu lateral esquerdo, clique em **Incoming Webhooks**.
6. Ative a chave no topo para **On**.
7. Desça a página e clique no botão **Add New Webhook to Workspace**.
8. Escolha em qual **canal** a mensagem deve ser enviada (ex: `#geral` ou um canal do seu time) e clique em permitir.
9. Na tela que carregar, você verá uma **Webhook URL** (parecida com `https://hooks.slack.com/services/T000...`). **Copie esse link!**

### 2. Subindo o código pro GitHub
1. Crie um novo repositório no seu GitHub.
2. Faça o push dessa pasta `automacao-coca` para o repositório.

### 3. Configurando a Secret (Senha) no GitHub Actions
Para não expor a sua URL do Slack publicamente, vamos colocá-la como uma variável secreta no GitHub.
1. No seu repositório no GitHub, vá na aba **Settings** (Configurações).
2. No menu lateral esquerdo, vá em **Secrets and variables** > **Actions**.
3. Clique no botão verde **New repository secret**.
4. No campo **Name**, digite exatamente assim: `SLACK_WEBHOOK_URL`
5. No campo **Secret**, cole a URL do Slack que você copiou no Passo 1.
6. Clique em **Add secret**.

### 4. Pronto! 🎉
O código já está configurado para rodar:
- **Automaticamente:** Toda terça-feira às 10h da manhã (Horário de Brasília).
- **Manualmente:** Você pode ir na aba **Actions** no seu GitHub, selecionar o workflow "Automação da Coca de Terça" na esquerda, e clicar no botão **Run workflow** para testar agora mesmo!

## 🧑‍💻 Como atualizar a lista de pessoas?
Se entrar ou sair alguém do time:
1. Abra o arquivo `execution/slack_webhook.py`.
2. Altere a variável `PEOPLE` com a nova lista.
3. Se quiser reiniciar a contagem, altere a data em `ANCHOR_DATE` para a terça-feira de quem for o primeiro da lista.
