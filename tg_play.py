from pyrogram import Client, filters

# Замените на ваш API ID
api_id = "api_id"
# Замените на ваш API Hash
api_hash = "api_hash"
# Username бота GPT
gpt_bot = "Your_GPT_Bot"
# Username бота для преобразования текста в речь
ms_speech_bot = "msspeechbot"

# Создание клиента Pyrogram
app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Словарь для хранения ID сообщений и соответствующих чатов
message_ids = {}

# Обработчик сообщений от GPT бота
@app.on_message(filters.chat(gpt_bot) & filters.text & filters.regex("GPT4"))
async def forward_message_to_bot(client, message):
    # Извлекаем текст сообщения, удаляя все до "End of message"
    cleaned_text = message.text.split("End of message")[0].strip()
    
    # Отправляем очищенное сообщение в @msspeechbot
    sent_message = await client.send_message(ms_speech_bot, cleaned_text)
    # Сохраняем информацию о сообщении
    message_ids[sent_message.id] = message.chat.id

# Обработчик ответов от @msspeechbot
@app.on_message(filters.chat(ms_speech_bot) & filters.audio)
async def handle_bot_response(client, message):
    # Получаем исходный chat_id из словаря
    if message.reply_to_message_id in message_ids:
        original_chat_id = message_ids[message.reply_to_message_id]
        # Пересылаем аудиофайл обратно в исходный чат
        await client.send_audio(original_chat_id, message.audio.file_id)
        # Удаляем запись из словаря
        del message_ids[message.reply_to_message_id]

# Отключение запроса подтверждения при авторизации
async def authorize_no_confirm(self):
    from pyrogram.raw.functions import Ping
    await self.send(Ping(ping_id=0))

app.authorize = authorize_no_confirm.__get__(app, Client)

# Запуск клиента
app.run()