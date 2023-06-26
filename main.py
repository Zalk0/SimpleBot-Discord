from dotenv import dotenv_values

from bot import SimpleBot


def main():
    # Import config from dotenv
    config = dotenv_values()
    print(config)

    # Create an instance of the SimpleBot
    client = SimpleBot()

    # Run the client with the token
    client.run(config['BOT_TOKEN'], reconnect=True)


if __name__ == '__main__':
    main()
