from bot import SimpleBot


def main():
    # Create an instance of the SimpleBot
    client = SimpleBot()

    # Run the client with the token
    client.run(client.config['BOT_TOKEN'], reconnect=True)


if __name__ == '__main__':
    main()
