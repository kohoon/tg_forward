from telethon import TelegramClient

api_id = '2493046'
api_hash = '598884197cbbb951c7020125cb4b62e7'
session_name = 'my_session'

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    dialogs = await client.get_dialogs()
    for dialog in dialogs:
        print(f"Name: {dialog.name}, ID: {dialog.id}")

with client:
    client.loop.run_until_complete(main())
