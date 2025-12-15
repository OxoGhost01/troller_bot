import discord
import os
import random
import asyncio
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

load_dotenv()

print("Troller will troll soon..")

intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)
tree = bot.tree

ASK_REPONSES = [
    "C'est une excellente question. Malheureusement, ce n'est pas la bonne.",
    "Après analyse approfondie, la réponse dépend du contexte émotionnel.",
    "Oui. Enfin non. Mais peut-être.",
    "Techniquement possible. Pratiquement discutable.",
    "Je ne peux pas répondre à cela sans remettre en question l'univers.",
    "La documentation est claire à ce sujet. Elle n'existe pas.",
    "Je comprends ta question, mais est-ce vraiment une question ?",
]

BLAGUES_NULLES = [
    "Pourquoi les programmeurs confondent Noël et Halloween ? Parce que OCT 31 == DEC 25.",
    "J'ai essayé de coder sans bug. J'ai échoué.",
    "Pourquoi ça marche ? Personne ne sait.",
    "Blague annulée pour manque de motivation.",
    "Tu t'attendais à une blague. Moi aussi.",
]

REPONSES_AUTOMATIQUES = {
    "bug": "Intéressant. Mais as-tu essayé d'éteindre puis rallumer ?",
    "marche pas": "Chez moi ça marche.",
    "?": "Réponse pertinente.",
    "help": "Je suis désolé que tu te sentes ainsi.",
    "quoi": "feur",
    "feur": "me ta gueule",
    "hello": "Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
    "coucou": "Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
    "salut": "Heyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
    "français": "Moi aussi.",
}

ANNONCES = [
    "🔔 Annonce importante\n\nFinalement non.",
    "🔔 Information officielle\n\nRien à signaler.",
    "🔔 Mise à jour critique\n\nTout reste pareil.",
]

# ---------- EVENTS ----------

@bot.event
async def on_ready():
    print("Trolling now....")
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="avec votre patience"
        )
    )
    await bot.tree.sync()
    print("Slash commands synced.")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to hell x)"
    )

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()
    
    for trigger, response in REPONSES_AUTOMATIQUES.items():
        if trigger in content:
            if random.random() < 0.4:
                await message.channel.send(response)
            break

    if bot.user.name.lower() in content:
        await message.channel.send("Oui ?")
        await asyncio.sleep(5)
        await message.channel.send("Ta gueule.")

# ---------- SLASH COMMANDS ----------

@bot.tree.command(name="blague", description="Raconte une blague vraiment nulle")
async def blague(interaction: discord.Interaction):
    blague = random.choice(BLAGUES_NULLES)

    if random.random() < 0.2:
        await interaction.response.send_message(blague[:len(blague)//2] + "...")
        await asyncio.sleep(2)
        await interaction.followup.send("Non en fait laisse tomber.")
    else:
        await interaction.response.send_message(blague)

@bot.tree.command(name="compte-a-rebours", description="Lance un suspense totalement inutile")
async def comptearebours(interaction: discord.Interaction):
    await interaction.response.send_message("Prépare-toi.")
    for i in range(5, 0, -1):
        await asyncio.sleep(1)
        await interaction.followup.send(str(i))
    await interaction.followup.send("Rien ne se passe. Merci de votre attention.")

@bot.tree.command(name="annonce", description="Fait une annonce très importante")
async def annonce(interaction: discord.Interaction):
    await interaction.response.send_message(random.choice(ANNONCES))

@bot.tree.command(name="ping", description="Teste la latence approximative")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong (approximatif)")

@bot.tree.command(name="stats", description="Affiche des statistiques très utiles")
async def stats(interaction: discord.Interaction):
    embed = discord.Embed(
        title="📊 Statistiques du serveur",
        color=discord.Color.blurple()
    )

    embed.add_field(name="Messages analysés", value="Beaucoup", inline=False)
    embed.add_field(name="Messages utiles", value="0", inline=True)
    embed.add_field(name="Messages inutiles", value="Tous", inline=True)
    embed.add_field(name="Crédibilité du bot", value="Discutable", inline=False)

    embed.set_footer(text="Données certifiées fiables à 100 %")

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="ask", description="Pose une question à un faux assistant très compétent")
@app_commands.describe(question="La question existentielle que tu te poses")
async def ask(interaction: discord.Interaction, question: str):
    await interaction.response.send_message("Analyse en cours…")

    await asyncio.sleep(random.uniform(1.5, 3.0))

    mode = random.random()

    # Réponse totalement à côté
    if mode < 0.4:
        await interaction.followup.send(random.choice(ASK_REPONSES))

    # Réponse pseudo-technique
    elif mode < 0.8:
        await interaction.followup.send(
            f"Concernant « {question} », la réponse courte est non.\n"
            "La réponse longue est plus complexe, donc non."
        )

    # Philosophie inutile
    else:
        await interaction.followup.send(
            "Avant de répondre, demandons-nous pourquoi répondre."
        )

@bot.tree.command(name="profile", description="Analyse approfondie de ton profil")
async def profile(interaction: discord.Interaction):
    user = interaction.user

    embed = discord.Embed(
        title="🧠 Analyse du profil",
        color=discord.Color.green()
    )

    embed.set_thumbnail(url=user.display_avatar.url)
    embed.add_field(name="Nom", value=user.display_name, inline=True)
    embed.add_field(name="Statut", value="Présent mais pas concentré", inline=True)
    embed.add_field(name="Niveau", value="Inquantifiable", inline=False)
    embed.add_field(name="Potentiel", value="Sous-exploité", inline=False)

    embed.set_footer(text="Analyse générée sans aucune base scientifique")

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="troll", description="Lance une analyse critique très sérieuse sur quelqu'un")
@app_commands.describe(user="La personne à analyser avec beaucoup trop de sérieux")
async def troll(interaction: discord.Interaction, user: discord.User):

    # Étape 1 — ouverture du dossier
    embed_start = discord.Embed(
        title="🛠️ Démarrage du protocole TROLL",
        description=(
            f"Un signalement automatique a été détecté.\n\n"
            f"**Cible :** {user.mention}\n"
            f"**Initiateur :** {interaction.user.mention}\n\n"
            "Merci de patienter pendant l'analyse."
        ),
        color=discord.Color.orange()
    )
    embed_start.set_footer(text="Merci de ne pas prévenir la personne concernée.")
    embed_start.set_thumbnail(url=user.display_avatar.url)

    await interaction.response.send_message(embed=embed_start)
    msg = await interaction.original_response()

    await asyncio.sleep(4)

    # Étape 2 — scan ridicule
    embed_scan = discord.Embed(
        title="🔍 Analyse comportementale",
        color=discord.Color.gold()
    )
    embed_scan.add_field(name="Présence sur le serveur", value="Confirmée", inline=False)
    embed_scan.add_field(name="Utilité moyenne", value="Fluctuante", inline=True)
    embed_scan.add_field(name="Confiance en soi", value="Légèrement excessive", inline=True)
    embed_scan.add_field(name="Dangerosité", value="Nulle", inline=False)
    embed_scan.set_footer(text="Scan en cours… ne pas cligner des yeux.")

    await msg.edit(embed=embed_scan)

    await asyncio.sleep(4)

    # Étape 3 — résultats inquiétants
    embed_mid = discord.Embed(
        title="📉 Résultats préliminaires",
        description=(
            "Les premiers résultats indiquent :\n\n"
            "• Une tendance à écrire sans réfléchir\n"
            "• Une confiance injustifiée dans ses messages\n"
            "• Une présence remarquée mais pas expliquée"
        ),
        color=discord.Color.red()
    )
    embed_mid.set_footer(text="Ces données peuvent être sorties de leur contexte.")

    await msg.edit(embed=embed_mid)

    await asyncio.sleep(4)

    # Étape 4 — verdict final
    embed_final = discord.Embed(
        title="✅ Verdict officiel",
        description=(
            f"**Conclusion concernant {user.mention} :**\n\n"
            "➡️ Troll potentiel détecté\n\n"
            "Aucune sanction ne sera appliquée.\n"
            "Cette analyse n'avait aucun objectif réel."
        ),
        color=discord.Color.dark_green()
    )
    embed_final.set_thumbnail(url=user.display_avatar.url)
    embed_final.set_footer(text="Rapport classé sans suite. Merci de votre collaboration.")

    await msg.edit(embed=embed_final)

    # Bonus — réaction finale
    await msg.add_reaction("🤡")


bot.run(os.getenv("DISCORD_TOKEN"))
