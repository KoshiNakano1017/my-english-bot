from fastapi import FastAPI, Request
from services import telegram_bot, gemini_api, state_manager
from utils import audio_handler

app = FastAPI()

@app.post("/webhook")
async def handle_webhook(request: Request):
    data = await request.json()
    if "message" not in data: return {"status": "ok"}
    
    msg = data["message"]
    user_id = msg["from"]["id"]

    # 設定変更 (Text)
    if "text" in msg:
        sit, voc = telegram_bot.parse_settings(msg["text"])
        if sit or voc:
            state_manager.update_user_setting(user_id, sit, voc)
            await telegram_bot.send_message(user_id, f"✅ Settings Saved!\nNow in: {sit}")
        return {"status": "ok"}

    # 英会話 (Voice)
    if "voice" in msg:
        # 1. 準備
        audio_path = await audio_handler.download_voice(msg["voice"]["file_id"], user_id)
        state_manager.increment_turn(user_id)
        state = state_manager.get_user_state(user_id)

        # 2. AI解析
        response = await gemini_api.chat_with_gemini(audio_path, state)

        # 3. 返信・掃除
        await telegram_bot.send_message(user_id, response)
        audio_handler.cleanup_voice(audio_path)

    return {"status": "ok"}