from telethon import TelegramClient
import asyncio
import os

# قراءة البيانات من Environment Variables
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

bot_username = os.environ["BOT_USERNAME"]  # بدون @
message = "🎁 الهدية اليومية"

async def main():
    # إنشاء الجلسة وتشغيل العميل
    client = TelegramClient("session", api_id, api_hash)
    await client.start()

    # حلقة لا نهائية لإرسال الرسالة كل 30 دقيقة
    while True:
        await client.send_message(bot_username, message)
        await asyncio.sleep(1800)  # 1800 ثانية = 30 دقيقة

# تشغيل البرنامج
asyncio.run(main())
