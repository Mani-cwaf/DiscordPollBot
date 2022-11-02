from discord import app_commands
import discord
import inflect
import json

guild = discord.Object(id = 992451336383770734)
intents = discord.Intents.default()
intents.guild_reactions = True
intents.guild_messages = True

class discord_client(discord.Client):
    def __init__(self):
        super().__init__(intents = intents)
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await tree.sync(guild = guild)
            self.synced = True
        print(f'we have logged in as {self.user}.')

client = discord_client()
tree = app_commands.CommandTree(client)

@tree.command(name = 'poll', description = 'poll command', guild = guild)
async def self(interaction: discord.Interaction, option1: str=None, option2: str=None, option3: str=None, option4: str=None, option5: str=None):
    description = ""
    options = [option1, option2, option3, option4, option5]
    for i in range(len(options)):
        description += f'Option :{inflect.engine().number_to_words(i + 1)}: : {options[i]} \n '
    await interaction.response.send_message(embed=discord.Embed(title="Poll", description=description))
    message = await interaction.original_response()
    await message.add_reaction('1\N{variation selector-16}\N{combining enclosing keycap}')
    await message.add_reaction('2\N{variation selector-16}\N{combining enclosing keycap}')
    await message.add_reaction('3\N{variation selector-16}\N{combining enclosing keycap}')
    await message.add_reaction('4\N{variation selector-16}\N{combining enclosing keycap}')
    await message.add_reaction('5\N{variation selector-16}\N{combining enclosing keycap}')

client.run(json.load(open('PrivateData.json'))["AuthKey"])