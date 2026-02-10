import httpx
import os
from config import TELEGRAM_BOT_TOKEN

async def download_voice(file_id: str, user_id: int):
    dest_path = f"temp_{user_id}.ogg"
    
    # 1. TelegramからURLを取得
    async with httpx.AsyncClient() as client:
        file_info = await client.get(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getFile?file_id={file_id}")
        file_path = file_info.json()["result"]["file_path"]
        
        # 2. ダウンロード
        download_url = f"https://api.telegram.org/file/bot{TELEGRAM_BOT_TOKEN}/{file_path}"
        voice_data = await client.get(download_url)
        
        with open(dest_path, "wb") as f:
            f.write(voice_data.content)
            
    return dest_path

def cleanup_voice(path: str):
    if os.path.exists(path):
        os.remove(path)