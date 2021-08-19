import discord
from discord.ext import commands
from discord.utils import get
from random import randint

bot = commands.Bot(description='Um bot feito para um trabalho universitário', command_prefix='.')


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Digite .ajuda"))
    print("""
    ----------------------------------
                Bot Online!
       Feito por: Bruno Durão Silva
        Projeto AV3 de programação:
             Bot para discord
                build v1.1
    ----------------------------------
    versão da API discord.py:""", discord.__version__, """
    ----------------------------------
Registro de ações no console:""")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Este comando não existe.")

    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Faltam Argumentos. Digite .ajuda para saber como utilizar o comando corretamente!")

    if isinstance(error, commands.BadArgument):
        await ctx.send("Argumento inválido. Digite .ajuda para saber como utilizar o comando corretamente!")


@bot.command()
async def teste(ctx):
    await ctx.message.add_reaction("✅")
    await ctx.send("Teste concluido!")
    print("Teste concluido!")


@bot.command()
async def somar(ctx, a: int, b: int):
    await ctx.send(a + b)
    print("Somar: O resultado é {}".format(a + b))


@bot.command()
async def multiplicar(ctx, a: int, b: int):
    await ctx.send(a * b)
    print("Multiplicar: O resultado é {}".format(a * b))


@bot.command()
async def dividir(ctx, a: int, b: int):
    await ctx.send(a / b)
    print("Dividir: O resultado é {}".format(a / b))


@bot.command()
async def ajuda(ctx):
    embed = discord.Embed(title="Aqui estão todos os comandos do bot atualmente:", color=0x000080)
    embed.add_field(name="**ajuda**", value="Mostra estes comandos", inline=False)
    embed.add_field(name="**teste**", value="Um comando de teste, verifica se o bot está funcional.", inline=False)
    embed.add_field(name="**desmotivar**", value="Mostra uma imagem desmotivadora aleatória.", inline=False)
    embed.add_field(name="**cargos**", value="Escolha um cargo usando reações.", inline=False)
    embed.add_field(name="**somar**", value="Soma dois números inteiros. Uso correto: **.somar 1 1**", inline=False)
    embed.add_field(name="**multiplicar**", value="Multiplica dois números inteiros. Uso correto: **.multiplicar 1 1**",
                    inline=False)
    embed.add_field(name="**dividir**", value="Divide dois números inteiros. Uso correto: **.dividar 1 1**",
                    inline=False)
    embed.add_field(name="**expulsar**", value="Expulsa um usuário do servidor. Uso correto: **.expulsar @usuario**",
                    inline=False)
    embed.add_field(name="**banir**", value="Bane um usuário do servidor. Uso correto: **.banir @usuario**",
                    inline=False)
    embed.add_field(name="**desbanir**",
                    value="Tira o banimento de um usuário banido do servidor. Uso correto: **.desbanir usuario#0000**",
                    inline=False)
    embed.add_field(name="**admin**",
                    value="Verifica se o usuário é um administrador do servidor. Uso correto: **.admin @usuario**",
                    inline=False)
    embed.add_field(name="**sugestao**", value="E-mail para contato de sugestões para o bot.", inline=False)
    embed.add_field(name="**fale**",
                    value="O bot vira seu papagaio pessoal. Uso correto: **.fale** (**o que o bot falará**).",
                    inline=False)
    embed.add_field(name="**limpar**",
                    value="Limpe o chat. Uso correto: **.limpar** (**quantidade**) [sem quantidade informada, serão apagadas 100 mensagens].",
                    inline=False)
    embed.add_field(name="**Autoria**", value="Bot feito por Bruno Durão Silva", inline=False)
    await ctx.send(embed=embed)


@bot.command()
async def cargos(ctx):
    embed1 = discord.Embed(
        title="Adicione uma das seguintes reações para ober um cargo abaixo:", color=0x000080)
    embed1.add_field(name="> **Cobaia**       =  🐁", value="Seja testado!", inline=False)
    embed1.add_field(name="> **Novato**       =  😵", value="Seja bem vindo, novato!", inline=False)
    embed1.add_field(name="> **Veterano**     =  😎", value="Mostre pros novatos quem é que manda!", inline=False)
    embed1.add_field(name="> **Inteligente**  =  🤓", value="Demonstre inteligência e ajude os outros!", inline=False)
    embed1.add_field(name="> **Preguiçoso**   =  😴", value="Muito sono pra fazer qualquer coisa...", inline=False)
    embed1.add_field(name="> **Coronavairus** =  😷", value="Pegaste corona. Ficará isolado do servidor.", inline=False)
    mensagemBot = await ctx.send(embed=embed1)
    global idMensagem
    idMensagem = mensagemBot.id

    await mensagemBot.add_reaction("🐁")
    await mensagemBot.add_reaction("😵")
    await mensagemBot.add_reaction("😎")
    await mensagemBot.add_reaction("🤓")
    await mensagemBot.add_reaction("😴")
    await mensagemBot.add_reaction("😷")


@bot.event
async def on_reaction_add(reaction, member):
    msg = reaction.message
    if reaction.emoji == "🐁" and msg.id == idMensagem:
        cargo = get(member.guild.roles, name="Cobaia")
        await member.add_roles(cargo)
        if member.id == 715551579612119070:
            return
        if not member.id == 715551579612119070:
            print("{} agora está no cargo {}".format(member, cargo))

    if reaction.emoji == "😵" and msg.id == idMensagem:
        cargo = get(member.guild.roles, name="Novato")
        await member.add_roles(cargo)
        if member.id == 715551579612119070:
            return
        if not member.id == 715551579612119070:
            print("{} agora está no cargo {}".format(member, cargo))

    if reaction.emoji == "😎" and msg.id == idMensagem:
        cargo = get(member.guild.roles, name="Veterano")
        await member.add_roles(cargo)
        if member.id == 715551579612119070:
            return
        if not member.id == 715551579612119070:
            print("{} agora está no cargo {}".format(member, cargo))

    if reaction.emoji == "🤓" and msg.id == idMensagem:
        cargo = get(member.guild.roles, name="Inteligente")
        await member.add_roles(cargo)
        if member.id == 715551579612119070:
            return
        if not member.id == 715551579612119070:
            print("{} agora está no cargo {}".format(member, cargo))

    if reaction.emoji == "😴" and msg.id == idMensagem:
        cargo = get(member.guild.roles, name="Preguiçoso")
        await member.add_roles(cargo)
        if member.id == 715551579612119070:
            return
        if not member.id == 715551579612119070:
            print("{} agora está no cargo {}".format(member, cargo))

    if reaction.emoji == "😷" and msg.id == idMensagem:
        cargo = get(member.guild.roles, name="Coronavairus")
        await member.add_roles(cargo)
        if member.id == 715551579612119070:
            return
        if not member.id == 715551579612119070:
            print("{} agora está no cargo {}".format(member, cargo))


@bot.command()
async def desmotivar(ctx):
    img = randint(1, 6)
    if img == 1:
        await ctx.send(
            "Imagem por @coachdefracassos https://printerama.com.br/media/catalog/product/cache/b0c13a2ccecd8979554cfcb92112e614/_/c/_coach-de-fracassos_-o-n_o-estampa_1.png")
        print("{} Foi desmotivado!".format(ctx.author))
    if img == 2:
        await ctx.send(
            "Imagem por @coachdefracassos https://i.pinimg.com/originals/66/4a/09/664a0915289315cddf3d67c8e056df53.png")
        print("{} Foi desmotivado!".format(ctx.author))
    if img == 3:
        await ctx.send(
            "Imagem por @coachdefracassos https://i.pinimg.com/236x/de/20/33/de2033eca9de5862a20bbf4c2ca5fad6.jpg")
        print("{} Foi desmotivado!".format(ctx.author))
    if img == 4:
        await ctx.send(
            "Imagem por @coachdefracassos https://i.pinimg.com/236x/97/a3/0c/97a30c22f5290b330babe150d2e9d3be.jpg")
        print("{} Foi desmotivado!".format(ctx.author))
    if img == 5:
        await ctx.send(
            "Imagem por @coachdefracassos https://i.pinimg.com/originals/af/13/c9/af13c9415f8eaef383a90e087cc0e8e5.png")
        print("{} Foi desmotivado!".format(ctx.author))
    if img == 6:
        await ctx.send(
            "Imagem por @coachdefracassos https://i.pinimg.com/236x/7b/10/07/7b1007557e28c979d61cb8d03badc0c0.jpg")
        print("{} Foi desmotivado!".format(ctx.author))


@bot.command()
async def limpar(ctx, quantidade=100):
    await ctx.channel.purge(limit=quantidade + 1)
    print("O chat foi limpo por {}!".format(ctx.author))


@bot.command()
async def expulsar(ctx, membro: discord.Member, *, motivo=None):
    if ctx.author.guild_permissions.administrator:
        await membro.kick(reason=motivo)
        await ctx.send("O usuário {} foi expulso!".format(membro))
        print("O Usuário {} foi expulso.".format(membro))
    else:
        await ctx.send("Você não pode expulsar usuários sem ser um Administrador!")


@bot.command()
async def banir(ctx, membro: discord.Member, *, motivo=None):
    if ctx.author.guild_permissions.administrator:
        await membro.ban(reason=motivo)
        await ctx.send("O usuário {} foi banido!".format(membro))
        print("O Usuário {} foi banido.".format(membro))
    else:
        await ctx.send("Você não pode banir usuários sem ser um Administrador!")


@bot.command()
async def desbanir(ctx, *, member):
    MembrosBanidosLista = await ctx.guild.bans()
    membro_nome, membro_numero = member.split('#')
    if ctx.author.guild_permissions.administrator:
        for ban_entry in MembrosBanidosLista:
            banido = ban_entry.user

            if (banido.name, banido.discriminator) == (membro_nome, membro_numero):
                await ctx.guild.unban(banido)
                await ctx.send("O usuário {} foi desbanido!".format(banido))
                print("Usuário {} Desbanido.".format(banido))
                return
    else:
        await ctx.send("Você não pode desbanir membros sem ser Administrador!")


@bot.command()
async def admin(ctx, membro: discord.Member):
    if membro.guild_permissions.administrator:
        await ctx.send("O usuário {} é um administrador!".format(membro))
    else:
        await ctx.send("O usuário {} não é um administrador!".format(membro))


@bot.command()
async def sugestao(ctx):
    await ctx.send("Sugestões são bem vindas! E-mail do criador: contato.brunodurao@gmail.com")


@bot.command()
async def fale(ctx, *, arg):
    await ctx.channel.purge(limit=1)
    await ctx.send(arg)
    print("O bot disse '{}' no chat!".format(arg))


chave = int(input("""O bot pode iniciar?
1 = sim
0 = não
resposta: """))
if chave == 1:
    print("Bot iniciado")
    bot.run('bot-key')
