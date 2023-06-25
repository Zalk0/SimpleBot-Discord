import discord
from discord import app_commands


@app_commands.context_menu(name="Pin/Unpin")
async def pin(interaction: discord.Interaction, message: discord.Message):
    if message.pinned:
        await message.unpin()
        await interaction.response.send_message("The message has been unpinned!", ephemeral=True)
    else:
        await message.pin()
        await interaction.response.send_message("The message has been pinned!", ephemeral=True)


@app_commands.command(name="cheh", description="Cheh somebody")
async def cheh(interaction: discord.Interaction, user: discord.Member):
    # Check if the user to cheh is the bot or the user sending the command
    if user == interaction.client.user:
        await interaction.response.send_message("You can't **Cheh** me!")
    elif user == interaction.user:
        await interaction.response.send_message("**FEUR**")
    else:
        cheh_gif = "https://tenor.com/view/cheh-true-cheh-gif-19162969"
        await interaction.response.send_message(f"**Cheh** {user.mention}")
        await interaction.channel.send(cheh_gif)
