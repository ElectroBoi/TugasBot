#Kuliah Support Discord Bot
from asyncio import events
import json
import lightbulb as lb
import hikari
import datetime
from linkkuliah import inputl, outl, Matkul_Link
from disbot import bot
import config


#Load data from json
f = open("linkmatkul.json", "r")
MatkulDict = json.load(f)
f.close()
MatkulL = list(MatkulDict.keys())



#Bot Startup
@bot.listen(hikari.StartingEvent)
async def bot_started(ctx : lb.context) -> None:
    await Matkul_Link(ctx)

#Bot Stopped
@bot.listen(hikari.StoppingEvent)
async def bot_stopped(ctx : lb.context) -> None:
    await print("Bot has Stopped!")


#User Inputed Link Kuliah
@bot.command
@lb.option("matkul","Nama Matkul untuk Link tersebut", choices=[MatkulL[6], MatkulL[7], MatkulL[8], MatkulL[10]],  type=str)
@lb.option("link","Masukan Link GMeet/Zoom", type=str)
@lb.command("inputlink", "masukan link kuliah")
@lb.implements(lb.SlashCommand)
async def inputlink(ctx):
    await inputl(ctx)


#Link Kuliah Request
@bot.command
@lb.option("matkul","Nama Matkul untuk Link tersebut", choices=MatkulL, type=str)
@lb.command("mintalink", "minta link kuliah")
@lb.implements(lb.SlashCommand)
async def hasil(ctx):
    await outl(ctx)


#Buka Jadwal
@bot.command
@lb.command("jadwal", "Buka Jadwal Kuliah Terbaru")
@lb.implements(lb.SlashCommand)
async def open_jadwal(ctx : lb.context) -> None:
    await ctx.respond("Jadwal terbaru telah dibuka", flags=hikari.MessageFlag.EPHEMERAL)
    tstamp = datetime.datetime.now().strftime("%d/%b/%Y - %H:%M:%S")
    print("["+ tstamp + "]" + str(ctx.author) + " requested Jadwal to be opened")
    await Matkul_Link(ctx)


#Input Tugas Baru
@bot.command
@lb.option("addtugas","Masukan tugas baru", choices=MatkulL, type=str)
@lb.command("matkul", "Nama Mata Kuliah tugas tersebut")
@lb.implements(lb.SlashCommand)
async def add_tugas(ctx : lb.context) -> None:
    await ctx.respond("test")


#hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]

#@bot.command
#@lb.option("jakhir","Jam akhir matkul tersebut", type=int)
#@lb.option("jawal","Jam awal matkul tersebut", type=int)
#@lb.option("hari","hari matkul tersebut", choices=hari, type=str)
#@lb.option("matkul","Nama Matkul tersebut")
#@lb.command("addmatkul", "Tambah Matkul Baru")
#@lb.implements(lb.SlashCommand)
#async def add_matkul(ctx):
#    await tambah_matkul(ctx)
    
bot.run()