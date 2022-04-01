import lightbulb as lb
import config
import Secrets


#Declare Bot

bot = lb.BotApp(
        #Bot Token
        token=Secrets.token,
        #The default guilds that application commands will be enabled in.
        default_enabled_guilds=(config.serverid)
        )