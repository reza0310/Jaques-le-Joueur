# coding=utf-8
__author__ = "reza0310"

import discord
from random import *
import asyncio
import os


def read_token():  # Permet d'utiliser le fichier texte "token" dans le même dossier pour se connecter à discord
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


def check(m):
    users_blacklist = ["Jaques le joueur#2605", "Laura du Pôle Emploi#8164", "Claire la Secrétaire#5331",
                       "Roger le Banquier#7558"]
    n = m.author not in users_blacklist
    return n


token = read_token()

client = discord.Client()

mute = False


@client.event
async def on_message(message):
    users_blacklist = ["Jaques le joueur#2605", "Laura du Pôle Emploi#8164", "Claire la Secrétaire#5331",
                       "Roger le Banquier#7558"]

    if str(message.author) not in users_blacklist:

        if message.content.find("<@628662847983058944>") != -1:  # Commande @mention
            print("Commande mention exécutée")
            await message.channel.send("Oui?\nTape J= aide  pour obtenir la liste des commandes disponibles.")

        elif message.content.find("J= aide") != -1:  # Commande aide
            print("Commande aide exécutée")
            await message.channel.send("Les commandes actuellement disponibles sont: \n-|J= bonjour| pour se saluer. \n-|J= merci| pour me remercier. \n-|J= jet [potentiel max] [potentiel max auquel cas le précédent deviens le min] [nombre de lancés]| pour faire un ou plusieurs jet(s) de min à max (0 à 20 de base) les 2 inclus. \n-|J= tables [potentiel niveau]| pour se taper 10 tables d'affilé et avoir un score. Le niveau va de 0 à l'infini (enfin 9223372036854775807 pour être exact). \n-|J= dvc [potentiel max] [potentiel max auquel cas le précédent deviens min]| pour un petit devine-chiffre les 2 inclus (de 0 à 100 de base).\n-|J= pp+ [titre: |[titre]|] [texte]| pour créer un presse papier et potentiellement lui rajouter un titre.\n-|J= pp+s [titre: |[titre]|] [texte]| pour créer un presse papier et potentiellement lui rajouter un titre. secret: votre message est effacé et vous êtes le seul à y avoir accès MAIS le titre reste publique et je garde l'accès aux fichiers depuis mon PC.\n-|J= ppl [numéro]| pour lire un presse papier si vous en avez le droit.\n-|J= pps [numéro]| pour supprimer un presse papier. \n-|J= ppn| pour avoir la liste des presse papiers. \n-|J= recherche randompokemon/pokemon/image [arguments]| pour faire des recherches sur internet. \nPS: Evitez l'abus de presse papier parce que ça créé des fichiers sur mon ordi... et aussi on peux supprimer les presse papiers des autres donc ne le faites pas. Je changerai ça à l'avenir.")

        elif message.content.find("J= bonjour") != -1:  # Commande bonjour
            print("Commande bonjour exécutée")
            await message.channel.send("Bonjour à toi!")

        elif message.content.find("J= merci") != -1:  # Commande merci
            print("Commande merci exécutée")
            await message.channel.send("De rien.")

        elif message.content.find("J= jet") != -1 or message.content.find("j= jet") != -1 or message.content.find("J=jet") != -1 or message.content.find("j=jet") != -1 or message.content.find("jet") != -1 or message.content.find("Jet") != -1:
            print("Commande jet exécutée par", message.author.name)
            zone = message.content
            chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            resul = []
            tours = 1
            min = 1
            max = 20
            end = False
            for i in range(len(zone)):
                if zone[i] in chiffres and zone[i-1] not in chiffres:
                    y = i
                    aappend = ""
                    while y < len(zone) and zone[y] in chiffres:
                        aappend += zone[y]
                        y += 1
                    resul.append(aappend)
                if zone[i] == "D" or zone[i] == "d":
                    end = True
            if end:
                if len(resul) == 2:
                    resul.insert(1, 1)
                resul.append(resul[0])
                del resul[0]
            print(resul)
            if len(resul) == 3:
                min = int(resul[0])
                max = int(resul[1])
                tours = int(resul[2])
            elif len(resul) == 2:
                min = int(resul[0])
                max = int(resul[1])
            elif len(resul) == 1:
                max = int(resul[0])
            if tours == 1:
                nombre = randint(min, max)
                a = "> ---------- " + message.author.mention + " ton jet de " + str(min) + " à " + str(max) + " est **" + str(nombre) + "** ----------"
            else:
                resultats = []
                total = 0
                for i in range(0, tours):
                    nombre = randint(min, max)
                    resultats.append(nombre)
                    total += nombre
                a = "> ---------- " + message.author.mention + " tes " + str(tours) + " jets de " + str(min) + " à " + str(max) + " sont **" + str(resultats) + "** ce qui fait un total de **" + str(total) + "** ----------"
            await message.channel.send(a)

        elif message.content.find("J= get") != -1 or message.content.find("j= get") != -1 or message.content.find("J=get") != -1 or message.content.find("j=get") != -1 or message.content.find("get") != -1 or message.content.find("Get") != -1:
            print("Commande jet exécutée par", message.author.name)
            zone = message.content
            chiffres = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            resul = []
            tours = 1
            min = 1
            max = 100
            end = False
            for i in range(len(zone)):
                if zone[i] in chiffres and zone[i-1] not in chiffres:
                    y = i
                    aappend = ""
                    while y < len(zone) and zone[y] in chiffres:
                        aappend += zone[y]
                        y += 1
                    resul.append(aappend)
                if zone[i] == "D" or zone[i] == "d":
                    end = True
            if end:
                if len(resul) == 2:
                    resul.insert(1, 1)
                resul.append(resul[0])
                del resul[0]
            print(resul)
            if len(resul) == 3:
                min = int(resul[0])
                max = int(resul[1])
                tours = int(resul[2])
            elif len(resul) == 2:
                min = int(resul[0])
                max = int(resul[1])
            elif len(resul) == 1:
                max = int(resul[0])
            if tours == 1:
                nombre = randint(min, max)
                a = "> ---------- " + message.author.mention + " ton jet de " + str(min) + " à " + str(max) + " est **" + str(nombre) + "** ----------"
            else:
                resultats = []
                total = 0
                for i in range(0, tours):
                    nombre = randint(min, max)
                    resultats.append(nombre)
                    total += nombre
                a = "> ---------- " + message.author.mention + " tes " + str(tours) + " jets de " + str(min) + " à " + str(max) + " sont **" + str(resultats) + "** ce qui fait un total de **" + str(total) + "** ----------"
            await message.channel.send(a)

        elif message.content.find("J= tables") != -1:
            print("Commande tables exécutée")
            niveau = 1
            results = []
            if len(message.content) >= 11:
                niveau = int(message.content.split(" ")[2])
            count = 0
            score = 0
            while count != 10:
                t1 = randint(niveau, niveau * 10)
                t2 = randint(niveau, niveau * 10)
                t3 = t1 * t2
                t4 = str(t1) + " x " + str(t2) + " = ?"
                await message.channel.send(t4)
                try:
                    humain = True
                    while humain:
                        msg = await client.wait_for('message', timeout=60.0, check=check)
                        try:
                            g = msg.content
                            g = int(g)
                            humain = False
                        except:
                            humain = True
                except asyncio.TimeoutError:
                    await message.channel.send('Désole mais t\'es vraiment trop long...')
                    g = "time out"
                if g == t3:
                    score += 1
                    results.append(str(t1) + " x " + str(t2) + " = " + str(g) + "     :white_check_mark:")
                else:
                    results.append(str(t1) + " x " + str(t2) + " = ~~" + str(g) + "~~ " + str(t3) + "     :x:")
                count += 1
            t5 = "Votre score est de: " + str(score)
            for calcul in range(len(results)):
                t5 += "\n-" + str(results[calcul])
            await message.channel.send(t5)

        elif message.content.find("J= dvc") != -1:
            print("Commande devine chiffre exécutée")
            zone = message.content.split(" ")
            if len(zone) >= 4:
                min = int(zone[2])
                max = int(zone[3])
            elif len(zone) == 3:
                min = 0
                max = int(zone[2])
            else:
                min = 0
                max = 100
            gagne = False
            chiffre_a_deviner = randint(min, max)
            essais = 0
            while not gagne:
                a = str(min) + " < ... < " + str(max)
                await message.channel.send(a)
                try:
                    humain = True
                    while humain:
                        msg = await client.wait_for('message', timeout=60.0, check=check)
                        try:
                            chiffre = int(msg.content)
                            humain = False
                        except:
                            humain = True
                except asyncio.TimeoutError:
                    await message.channel.send('Désole mais t\'es vraiment trop long...')
                if chiffre < min:
                    a = str("Moins que le minimum...")
                    await message.channel.send(a)
                elif chiffre > max:
                    a = str("Plus que le maximum...")
                    await message.channel.send(a)
                elif chiffre > chiffre_a_deviner:
                    a = str("C'est moins!")
                    await message.channel.send(a)
                    max = chiffre
                    essais += 1
                elif chiffre < chiffre_a_deviner:
                    a = str("C'est plus!")
                    await message.channel.send(a)
                    min = chiffre
                    essais += 1
                elif chiffre_a_deviner == chiffre:
                    essais += 1
                    a = "VOUS AVEZ GAGNE EN " + str(essais) + " ESSAIS!!! BIEN JOUE!!!"
                    await message.channel.send(a)
                    gagne = True

        elif message.content.find("J= pp+") != -1:
            print("Commande pp+ executée")
            a = message.content
            i = 7
            if a[6] == "s":
                await message.delete()
                i += 1
            a = a[i:]
            if a[0:6] == "titre:":
                a = a.split("|")
                a = a[1] + "\n" + a[2][1:] + "\n" + message.author.name
            else:
                a = "Sans titre\n" + a + "\n" + message.author.name
            if i == 7:
                a += "\nnon"
            else:
                a += "\noui"
            with open("n.txt", "r") as f:
                lines = f.readlines()
                N = lines[0].strip()
                N = int(N)
            Nom = "pp" + str(N) + ".txt"
            f = open("n.txt", "w")
            N += 1
            f.write(str(N))
            f.close()
            with open(Nom, "w", encoding="utf-8") as f:
                f.write(a)
            await message.channel.send("presse papier enregistré")

        elif message.content.find("J= parler") != -1:
            await message.delete()
            # msg = input("Message?")
            await message.channel.send("Nope")

        elif message.content.find("J= dire") != -1:
            msg = message.content[8:]
            await message.channel.send(msg)

        elif message.content.find("J= ppl") != -1:
            print("Commande ppl executée")
            a = message.content
            a = int(a[7:])
            N1 = "pp" + str(a) + ".txt"
            with open(N1, "r", encoding="utf-8") as f:
                lignes = f.readlines()
            if lignes[-1] == "oui" and message.author.name != lignes[-2][:-1]:
                await message.channel.send("Accès refusé")
                print("L'utilisateur", message.author.name, "a essayé d'ouvrir le presse papier secret de",
                      lignes[-2][:-1])
            else:
                texte = ''
                for line in lignes:
                    texte += line
                await message.channel.send(texte)

        elif message.content.find("J= ppn") != -1:
            print("Commande ppn executée")
            with open("n.txt", "r") as f:
                lines = f.readlines()
                N = lines[0].strip()
                N = int(N) - 1
            a = "Il y a " + str(N) + " fichiers:"
            poids = 0
            for i in range(1, N + 1):
                nom = "pp" + str(i) + ".txt"
                poids += os.path.getsize(nom)
                with open(nom, "r", encoding="utf-8") as f:
                    lignes = f.readlines()
                    titre = lignes[0]
                    auteur = lignes[-2]
                    secret = lignes[-1]
                if secret == "oui":
                    secr = " qui est secret"
                else:
                    secr = " qui n'est pas secret"
                a += "\n-Fichier n°" + str(i) + ": " + titre[:-1] + " par " + auteur[:-1] + secr
            a += "\nSoit un total de " + str(poids) + " octets sur le PC de reza0310"
            await message.channel.send(a)

        elif message.content.find("J= pps") != -1:
            print("Commande pps executée")
            a = message.content
            a = int(a[7:])
            N1 = "pp" + str(a) + ".txt"
            os.remove(N1)
            with open("n.txt", "r") as f:
                lines = f.readlines()
                N = lines[0].strip()
                N = int(N) - 1
            try:
                N2 = "pp" + str(N) + ".txt"
                os.rename(N2, N1)
            except:
                print('c\'était le dernier')
            f = open("n.txt", "w")
            f.write(str(N))
            f.close()
            await message.channel.send("Presse papier supprimé")

        elif message.content.find("J= clear") != -1 and message.author.name == "﴾ reza0310 ﴿":
            print("Commande clear exécutée par", message.author.name)
            x = int(message.content.split(" ")[2])
            async for msg in message.channel.history(limit=x):
                if msg.author.name.split(" ")[0] == message.content.split(" ")[3]:
                    await msg.delete()
                else:
                    x += 1

        elif message.content.find("J= among_us speak") != -1:
            global mute
            channel = client.get_channel(758035318858448897)
            members = channel.members
            for member in members:
                if mute == False:
                    await member.edit(mute=True)
                    await member.edit(deafen=True)
                else:
                    await member.edit(mute=False)
                    await member.edit(deafen=False)
            mute = not mute

        elif message.content.find("J=") != -1 and message.channel != client.get_channel(633656647264370689) or message.content.find("j=") != -1 or message.content.find("J =") != -1 or message.content.find("j =") != -1:
            print("Commande erreur exécutée")
            await message.channel.send("Mauvaise commande. Essayez J= aide.")

client.run(token)  # Démarre le bot