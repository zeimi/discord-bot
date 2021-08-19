# Projeto de Bot para Discord - Python

Esse projeto foi criado utilizando a API para discord - Discord.py.

<[Welcome to discord.py (discordpy.readthedocs.io)](https://discordpy.readthedocs.io/en/stable/)>

Também foi utilizado como entrega de projeto (AV3) para o primeiro semestre do curso de engenharia da computação, para a minha universidade atual (UNIJORGE).





Obs:

Alguns comandos, como o (.cargos) devem ser manualmente editados para cada servidor, para 100% de funcionalidades.
Entre as linhas 261 à linha 267, deve trocar o 'bot-key' pela sua key para usuário-bot fornecida pelo discord.
```python
chave = int(input("""O bot pode iniciar?
1 = sim
0 = não
resposta: """))
if chave == 1:
    print("Bot iniciado")
    bot.run('bot-key') # <- Troque aqui sua key
```