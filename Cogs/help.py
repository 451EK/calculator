import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,Bot):
        self.Bot = Bot

    @commands.command()
    async def help(self,ctx,command = None):
        if command == None:
            embed=discord.Embed(title="**Commands (8)**",description="➜ **Moderation**\n`setprefix`\n➜ **Info**\n`help`,`info`,`ping`\n ➜**Calculation**\n `add`,`sub`,`mul`,`div`,`sqrt`,`factorial`",colour=discord.Color.blue())
            await ctx.send(embed=embed)
        elif command == "setprefix".lower():
            SETPREFIXembed=discord.Embed(title="**Command 'setprefix'**",description="\n• **Usage** : `-setprefix <prefix>`\n• **Description** : Changes the prefix in server.\n• **Note** : Administrator permission is required to use this command.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SETPREFIXembed)
        elif command == "setprefix".upper():
            SETPREFIXembed=discord.Embed(title="**Command 'setprefix'**",description="\n• **Usage** : `-setprefix <prefix>`\n• **Description** : Changes the prefix in server.\n• **Note** : Administrator permission is required to use this command.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SETPREFIXembed)
        elif command == "help".lower():
            HELPembed=discord.Embed(title="**Command 'help'**",description="\n• **Usage** : `-help`\n• **Description** : Shows the help message.",colour=discord.Color.dark_theme())           
            await ctx.send(embed=HELPembed)
        elif command == "help".upper():
            HELPembed=discord.Embed(title="**Command 'help'**",description="\n• **Usage** : `-help`\n• **Description** : Shows the help message.",colour=discord.Color.dark_theme())           
            await ctx.send(embed=HELPembed)
        elif command == "info".lower():
            CREDITSembed=discord.Embed(title="**Command 'info'**",description="\n• **Usage** : `-info`\n• **Description** : Shows informations about the bot.",colour=discord.Color.dark_theme())
            await ctx.send(embed=CREDITSembed)
        elif command == "info".upper():
            CREDITSembed=discord.Embed(title="**Command 'info'**",description="\n• **Usage** : `-info`\n• **Description** : Shows informations about the bot.",colour=discord.Color.dark_theme())
            await ctx.send(embed=CREDITSembed)
        elif command == "ping".lower():
            PINGembed=discord.Embed(title="**Command 'ping'**",description="\n• **Usage** : `-ping`\n• **Description** : Shows bot's latency.",colour=discord.Color.dark_theme())
            await ctx.send(embed=PINGembed)
        elif command == "ping".upper():
            PINGembed=discord.Embed(title="**Command 'ping'**",description="\n• **Usage** : `-ping`\n• **Description** : Shows bot's latency.",colour=discord.Color.dark_theme())
            await ctx.send(embed=PINGembed)
        elif command == "add".upper():
            ADDembed=discord.Embed(title="**Command 'add'**",description="\n• **Usage** : `-add <number1> <number2>`\n• **Description** : Adds up entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=ADDembed)
        elif command == "add".lower():
            ADDembed=discord.Embed(title="**Command 'add'**",description="\n• **Usage** : `-add <number1> <number2>`\n• **Description** : Adds up entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=ADDembed)
        elif command == "sub".lower():
            SUBembed=discord.Embed(title="**Command 'sub'**",description="\n• **Usage** : `-sub <number1> <number2>`\n• **Description** : Subtracts entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SUBembed)
        elif command == "sub".upper():
            SUBembed=discord.Embed(title="**Command 'sub'**",description="\n• **Usage** : `-sub <number1> <number2>`\n• **Description** : Subtracts entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SUBembed)
        elif command == "mul".lower():
            MULembed=discord.Embed(title="**Command 'mul'**",description="\n• **Usage** : `-mul <number1> <number2>`\n• **Description** : Multiplies entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=MULembed)
        elif command == "mul".upper():
            MULembed=discord.Embed(title="**Command 'mul'**",description="\n• **Usage** : `-mul <number1> <number2>`\n• **Description** : Multiplies entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=MULembed)
        elif command == "div".lower():
            DIVembed=discord.Embed(title="**Command 'div'**",description="\n• **Usage** : `-div <number1> <number2>`\n• **Description** : Divides entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=DIVembed)
        elif command == "div".upper():
            DIVembed=discord.Embed(title="**Command 'div'**",description="\n• **Usage** : `-div <number1> <number2>`\n• **Description** : Divides entered numbers.",colour=discord.Color.dark_theme())
            await ctx.send(embed=DIVembed)
        elif command == "sqrt".lower():
            SQRTembed=discord.Embed(title="**Command 'sqrt'**",description="\n• **Usage** : `-sqrt <number>`\n• **Description** : Takes the square root of entered number.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SQRTembed)
        elif command == "sqrt".upper():
            SQRTembed=discord.Embed(title="**Command 'sqrt'**",description="\n• **Usage** : `-sqrt <number>`\n• **Description** : Takes the square root of the entered number.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SQRTembed)
        elif command == "factorial".lower():
            SQRTembed=discord.Embed(title="**Command 'factorial'**",description="\n• **Usage** : `-factorial <number>`\n• **Description** : Shows the factorial of the entered number.\n• **Note** : Entered number must be integer.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SQRTembed)
        elif command == "factorial".upper():
            SQRTembed=discord.Embed(title="**Command 'factorial'**",description="\n• **Usage** : `-factorial <number>`\n• **Description** : Shows the factorial of the entered number.\n• **Note** : Entered number must be integer.",colour=discord.Color.dark_theme())
            await ctx.send(embed=SQRTembed)
        else:
            UNKNOWNembed=discord.Embed(title="**Unknown Command**",description="Use the `-help` command to see all commands.",colour=discord.Color.red())
            reaction = "❌"
            await ctx.message.add_reaction(reaction)
            await ctx.send(embed=UNKNOWNembed)

def setup(Bot):
    Bot.add_cog(Help(Bot))

