import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

FEEDBACK_CHANNEL_ID = 1440021011092344873  # غيرها لـ ID الشنل

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == FEEDBACK_CHANNEL_ID:
        embed = discord.Embed()  # ممكن تضيف title/description إذا تحب
        embed.set_image(url="https://cdn.discordapp.com/attachments/1304166672873029723/1440091225297391778/flamingtext_com-3265350159.gif")
        # النص اللي عايز تكتبه
        text = f" \n**Thanks For Giving {message.author.mention} Feedback 💖**"
        await message.channel.send(content=text, embed=embed)

    await bot.process_commands(message)

bot.run("MTQ0ODM2NjA3NTY5MDQ4Mzc2Mw.G0tsaF.ZgLXxhGqu-njL5uf8ANpkbuh6kbS-oj_8SEFZ0")
