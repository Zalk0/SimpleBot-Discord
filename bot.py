import discord

from commands_list import commands_list


# Create a class of the bot
class SimpleBot(discord.Client):
    # Initialization when class is called
    def __init__(self):
        # Set intents for the bot
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.synced = False

    # Wait until bot is ready
    async def on_ready(self):
        # Waits until internal cache is ready
        await self.wait_until_ready()

        # Import commands and sync
        command_tree = discord.app_commands.CommandTree(self)
        commands_list(command_tree)
        if not self.synced:
            await command_tree.sync()
            self.synced = True

        # Set activity of the bot
        activity = discord.Activity(type=discord.ActivityType.listening, name="me")
        await self.change_presence(activity=activity, status=discord.Status.online)

        # Set up logging
        discord.utils.setup_logging()

        # Check the number of servers the bot is a part of
        print(f"I'm in {len(self.guilds)} server(s)")

        # Prints in the console that the bot is ready
        print(f'{self.user} is now online and ready!')

    # To react to messages sent in channels bot has access to
    async def on_message(self, message: discord.Message):
        # Ignore messages from bots including self
        if message.author.bot:
            return
        # Do something

    # To react to users joining a guild the bot is in
    async def on_member_join(self, member: discord.Member):
        # Check if the member is a bot
        if member.bot:
            return
        # Do something


# Function to run the bot
def main():
    # Import token from file
    with open("bot_token", "r") as file:
        token = file.read().rstrip()

    # Create an instance of the SimpleBot
    client = SimpleBot()

    # Run the client with the token
    client.run(token, reconnect=True)
