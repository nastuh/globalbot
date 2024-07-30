import disnake
from disnake.ext import commands

bot = commands.Bot(command_prefix=".", help_command=None, intents=disnake.Intents.all())

#command to turn on the bot, we can see message in terminal
@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")

@bot.event
async def on_member_join(member):
    role = await disnake.utils.get(guild_id=member.guild.id, role_id=)

bot.run('MTI2NTc1Nzg1Njg1OTE2MDU3Ng.G8v_fq.pQAoYV_bTDgiCB_sqUpQG77e_RFDdT34Y8YdH4')
