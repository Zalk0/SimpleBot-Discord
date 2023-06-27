import discord
from discord import app_commands


# Define command group based on the Group class
class Roles(app_commands.Group):
    # Set command group name and description
    def __init__(self):
        super().__init__(name="roles", description="Manages roles")

    # Set error handler for permissions for the command group
    async def on_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.MissingPermissions):
            for perm in error.missing_permissions:
                if perm == "administrator":
                    await interaction.response.send_message("You must be an admin to use the command!")
                    return
            await interaction.response.send_message("You don't have the permissions to use the command!")

    # Define number command
    @app_commands.command(name="number", description="Get the number of users in a role")
    @app_commands.checks.has_permissions(administrator=True)
    async def number(self, interaction: discord.Interaction, role: discord.Role):
        nb_users = len(role.members)
        if nb_users == 0:
            await interaction.response.send_message(f"There is no user in the role **{role.name}**")
        elif nb_users == 1:
            await interaction.response.send_message(f"There is 1 user in the role **{role.name}**")
        else:
            await interaction.response.send_message(f"There are {nb_users} users in the role **{role.name}**")

    # Define set command
    @app_commands.command(name="set", description="Set the roles of a user")
    @app_commands.rename(member="user")
    @app_commands.checks.has_permissions(administrator=True)
    async def set(self, interaction: discord.Interaction, member: discord.Member, roles: str):
        roles_list = []
        roles_string = ""
        for role in roles.split(" "):
            role = "".join(filter(str.isdigit, role))
            # Check if string is of the correct length
            if not len(role) == 18:
                await interaction.response.send_message("At least one role is not correct!")
                return
            role = member.guild.get_role(int(role))
            # Check if role is found
            if role is None:
                await interaction.response.send_message("At least one role is not correct!")
                return
            roles_list.append(role)
            roles_string += f" **{role.name}**,"
        await member.edit(roles=roles_list)
        roles_string = roles_string[:-1]
        await interaction.response.send_message(f"The roles{roles_string} were given to {member.name}")

    # Define check_duplicate command
    @app_commands.command(name="check_duplicate", description="Displays the roles with the same name")
    @app_commands.checks.has_permissions(administrator=True)
    async def check_dupli(self, interaction: discord.Interaction):
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
