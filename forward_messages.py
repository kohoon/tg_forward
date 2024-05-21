from telethon import TelegramClient, events

# API ID와 Hash는 my.telegram.org에서 얻을 수 있습니다.
api_id = '2493046'
api_hash = '598884197cbbb951c7020125cb4b62e7'

# 세션 이름을 설정합니다. 임의의 문자열을 사용할 수 있습니다.
session_name = 'my_session'

# 메시지를 포워딩할 소스 채널과 대상 채널의 사용자 이름 또는 ID를 설정합니다.
source_channel_id = -1001333182061
destination_channel_id = -1002024089057

# Telegram 클라이언트를 초기화합니다.
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    
    # 채널 엔티티 가져오기
    source_channel = await client.get_entity(source_channel_id)
    destination_channel = await client.get_entity(destination_channel_id)

    @client.on(events.NewMessage(chats=source_channel))
    async def handler(event):
        await client.send_message(destination_channel, event.message)

    print(f'Listening for new messages in {source_channel_id}...')
    await client.run_until_disconnected()

with client:
    client.loop.run_until_complete(main())