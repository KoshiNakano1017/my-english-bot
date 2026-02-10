import httpx
from config import TELEGRAM_BOT_TOKEN

# メッセージを送信する共通関数
async def send_message(chat_id: int, text: str):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown" # 太字や改行を綺麗に見せるため
    }
    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload)

# テキストメッセージから設定を読み取るロジック
def parse_settings(text: str):
    situation = None
    keywords = []
    
    if "Situation:" in text:
        situation = text.split("Situation:")[1].split("\n")[0].strip()
    if "Keywords:" in text:
        raw_keywords = text.split("Keywords:")[1].strip()
        keywords = [k.strip() for k in raw_keywords.split(",")]
        
    return situation, keywords