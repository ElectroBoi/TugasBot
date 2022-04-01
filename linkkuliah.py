from distutils.command.config import config
from re import A
import lightbulb as lb
import hikari
import json
import datetime
from disbot import bot
import config


#Load data from json
f = open("linkmatkul.json", "r")
MatkulDict = json.load(f)
f.close()
MatkulL = list(MatkulDict.keys())
f = open("usercache.json", "r")
usercache = json.load(f)
f.close()



#Input Link Function
async def inputl(ctx):
    before = MatkulDict.get(ctx.options.matkul)
    MatkulDict.update({ctx.options.matkul:ctx.options.link})
    after = MatkulDict.get(ctx.options.matkul)
    f = open("linkmatkul.json", "w")
    json.dump(MatkulDict, f)
    f.close()
    await ctx.respond("Link Saved to " + ctx.options.matkul, flags=hikari.MessageFlag.EPHEMERAL)
    tstamp = datetime.datetime.now().strftime("%d/%b/%Y - %H:%M:%S")
    print("["+ tstamp + "]" + " Link Kuliah was Updated from '"+ before + "' to '" + after + "' By " + str(ctx.author))
    usercache["latest_link_author"] = str(ctx.author)
    usercache["latest_link_time"] = tstamp
    f = open("usercache.json", "w")
    json.dump(usercache, f)
    f.close()
    await Matkul_Link(ctx)


#Request an Matkul Link Function
async def outl(ctx):
    if MatkulDict.get(ctx.options.matkul) != "":
        await ctx.respond(MatkulDict.get(ctx.options.matkul), flags=hikari.MessageFlag.EPHEMERAL)
        tstamp = datetime.datetime.now().strftime("%d/%b/%Y - %H:%M:%S")
        print("["+ tstamp + "]" + str(ctx.author) + " requested a link to matkul '" + ctx.options.matkul + "'")
    else:
        await ctx.respond("```Matkul tersebut Tidak ada link nya!```")


#Open an embed with Jadwal and links Kuliah Function
async def Matkul_Link(ctx : lb.context) -> None:
    f = open("linkmatkul.json", "r")
    MatkulDict = json.load(f)
    f.close()

    embed = hikari.Embed(title="**Jadwal Kuliah KB01**", 
        description="Jadwal Kuliah dan Link Gmeet/Zoom [" + config.kelas + " Semester "+ config.semester + "]", 
        colour=0xA63EC5
        )

    for i in range(0,len(MatkulL)):
        embed.add_field(MatkulL[i],"- " + MatkulDict.get(MatkulL[i]))

    f = open("usercache.json", "r")
    usercache = json.load(f)
    f.close()

    embed.set_thumbnail("https://rekreartive.com/wp-content/uploads/2018/10/Logo-Gunadarma-Universitas-Gunadarma-Original-PNG.png")
    embed.set_footer("Updated on " + usercache["latest_link_time"] + " By "+ usercache["latest_link_author"] +"   -   TugasBot V. " + config.versi)
    await bot.rest.create_message(config.jadwal_channelid, embed)



#async def tambah_matkul(ctx):
#    jawal = ctx.options.jawal + 6
#    jakhir = ctx.options.jakhir + 7
#    MatkulDict[ctx.options.matkul + " | " + ctx.options.hari + ", " + str(jawal) +":30 - " + str(jakhir) + ":30"] = ""
#    f = open("linkmatkul.json", "w")
#    json.dump(MatkulDict, f)
#    f.close()
#    await ctx.respond("Matkul telah ditambah!", flags=hikari.MessageFlag.EPHEMERAL)