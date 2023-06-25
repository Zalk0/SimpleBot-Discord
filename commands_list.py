from commands.roles import Roles
from commands.utils import pin, cheh


# List of commands to add to the command tree
def commands_list(tree):
    # Add the pin command
    tree.add_command(pin)
    # Add the pin command
    tree.add_command(cheh)
    # Add the roles command group
    tree.add_command(Roles())
