
#Importera bibliotek
import discord
from discord.ext import commands
import googletrans
from discord import FFmpegPCMAudio
import time


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= "!", intents=intents) #Väljer en prefix för kommandon: '!'

messageCount = {} #Här sparas hur många gånger en användare har skrivit ett meddelande i en dictionary där ett namn och ett värde finns.


@client.event   #Bot lyssnar efter specefiktt event
async def on_ready():   #I detta går programmet in i denna funktion när det lyckas med uppstart
    print("The bot is ready")   
    print("----------------")


# @client.command() #Bot lyssnar efter ett specifikt kommando
# async def levels(ctx): #När kommandot "!hello" skickas så kommer bot att skicka tillbaka medellande i discord
#     print(messageCount)

@client.command(aliases = ['tr'])   #Lyssna efter kommando, kommando kan också kallas med 'tr' istället för 'translate'
async def translate(ctx, lang_to, *args): # !translate, tar argumenten: Vilken kanal som kommando skrevs i, vilket språk som ska översättas till, och text som ska översättas
    lang_to = lang_to.lower()             #gör gör text till gemener
    if lang_to not in googletrans.LANGUAGES and lang_to not in googletrans.LANGCODE:  #kontrollera att givet språk stöds av översättaren
        raise commands.BadArgument("Påhittat språk")    #felmeddelande

    text = ' '.join(args)   #Anslut text med mellanrum och deklarerar den som en variabel "text"
    translator = googletrans.Translator()   #Deklarera översättaren som "translator"
    translated_text = translator.translate(text, dest=lang_to).text #Deklarera variabel med den översatta texten
    await ctx.send(translated_text)     #Skicka meddelande med översatt text
    
@client.command(pass_context=True)#Deklarera ett kommando
async def join(ctx):    #Skapar funktion som körs när kommandot "!join" hittas i en kanal.
    if (ctx.author.voice):  #Kontrollerar att användaren är i en röstkanal, så att botten kan gå med i den.
        channel = ctx.message.author.voice.channel  #Skapar variabelnamn för användarens röstkanal
        voice = await channel.connect()     #Skapar instans för att bot går med i röstkanal
        voice.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source="C:/Users/william.modig/Desktop/DiscordBot/DiscordBot2/superidol.wav"))
        #Använder 'voice' som variabel för bot i röstkanal, och använder vårt importerade bibliotek FFmpegAudio för att spela ljud från en specifik source.

        while voice.is_playing():   #While kontroll som säkerställer att boten inte lämnar innan ljudfilen spelat klart.
            time.sleep(.1)
        await voice.disconnect()    #Bot disconnect
    else:
        await ctx.send('You are not in a voice channel')   #Skickar felmeddelande i context chat att användaren måste ansluta till röstkanal


@client.event #Event
async def on_member_join(member):   #När det inbyggda eventet 'on_member_join' händer körs funktionen.
    #Skickar ett välkomstmeddelande när ny medlem finns i server.
    channel = client.get_channel(940151258503872515) # #general
    await channel.send('How did the chicken cross the road')

@client.event
#Samma som event ovan men för när någon lämnar
async def on_member_remove(member):
    channel = client.get_channel(940151258503872515)
    await channel.send('Goodbye')

# @client.event #Här lyssnar botten återigen efter ett specifikt event. 
# async def on_message(ctx):
#     author = str(ctx.author) #Här tar den reda på information om vilken användare som skriver och sparar det i en variabel
#     if author in messageCount: #If-sats som kontrollerar om användaren redan finns i vårt dictionary 'messageCount'
#         messageCount[author] += 1 #Operatorn adderar personlig räknare med ett.
#     else:
#         messageCount[author] = 1 #Ger den nya användaren ett startvärde på 1
#         await client.process_commands(ctx)




    
client.run("OTQ1MjMzNTg2NzIwNzU1NzQy.YhNLYA.rVhZjAUthdoPdgOFldcWPv_6T3Y")
 
