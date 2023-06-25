import discord
from discord import app_commands


# Define command group based on the Group class
class Roles(app_commands.Group):
    # Set command group name and description
    def __init__(self):
        super().__init__(name="roles", description="Manages roles")

    # Define number command
    @app_commands.command(name="number", description="Get the number of users in a role")
    async def number(self, interaction: discord.Interaction, role: discord.Role):
        nb_users = len(role.members)
        if nb_users == 0:
            await interaction.response.send_message(f"There is no user in the role **{role.name}**")
        elif nb_users == 1:
            await interaction.response.send_message(f"There is 1 user in the role **{role.name}**")
        else:
            await interaction.response.send_message(f"There are {nb_users} users in the role **{role.name}**")

    # Define set command
    @app_commands.command(name="set", description="Give a role to a user")
    async def set(self, interaction: discord.Interaction, user: discord.Member, role: discord.Role):
        if interaction.user.guild_permissions.administrator:
            await user.add_roles(role)
            await interaction.response.send_message(f"The role **{role.name}** was given to {user.name}")
        else:
            await interaction.response.send_message("You must be administrator to use this command!")

    # Define same_roles command
    @app_commands.command(name="same_roles", description="Displays the roles with the same name")
    async def same(self, interaction: discord.Interaction):
        # Defer response to slash command (default only allows the bot 3s to respond)
        await interaction.response.defer(thinking=True)
        roles = interaction.guild.roles
        seen_roles = []
        duplicate_roles = []
        duplicate_string = ""
        for role in roles:
            if role.name.upper() in duplicate_roles:
                continue
            elif role.name.upper() in seen_roles:
                duplicate_roles.append(role.name.upper())
                duplicate_string += f"**{role.name.upper()}**\n"
            else:
                seen_roles.append(role.name.upper())
        await interaction.followup.send(f"Duplicated roles found:\n{duplicate_string}")
