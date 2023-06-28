import discord  
from discord.ext import commands
from discord import app_commands

class help(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="help", description="Helps with the bot!")
    async def help(self, interaction):
        await interaction.response.send_message("No help for you yet")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(help(bot))