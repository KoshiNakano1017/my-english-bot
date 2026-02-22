## Feature list (current implementation)

This folder documents **what is implemented today**, using a consistent template (purpose / input / processing / output / state / constraints / related files). Ideas for future features live in `docs/new_features.md`.

## 1) Webhook intake (FastAPI)
- **Purpose**: Receive Telegram webhook updates and route between text/voice flows
- **Entry point**: `POST /webhook`
- **Related**: `main.py`

## 2) Settings persistence (Situation / Keywords)
- **Purpose**: Keep per-user "conversation situation" and "target vocabulary" and reuse them in prompts
- **Input**: Telegram text in a `Situation:` / `Keywords:` format
- **Related**: `services/telegram_bot.py`, `services/state_manager.py`, `main.py`

## 3) Voice conversation (Voice → Gemini → text reply)
- **Purpose**: Fetch Telegram voice, send it to Gemini, and reply with text
- **Input**: Telegram voice message
- **Related**: `utils/audio_handler.py`, `services/gemini_api.py`, `services/telegram_bot.py`, `main.py`

## 4) State management (per-user + turn counter)
- **Purpose**: Keep `situation / target_vocab / turn_count` in memory per `user_id`
- **Related**: `services/state_manager.py`

## 5) Telegram API I/O (minimum)
- **Send**: text replies via `sendMessage`
- **Receive voice**: `getFile` → download from file URL
- **Related**: `services/telegram_bot.py`, `utils/audio_handler.py`

## 6) GitHub Actions (AI Review)
- **Purpose**: Run a lightweight Gemini-based review on pushes (designed not to fail the whole workflow on API errors)
- **Related**: `.github/workflows/ai_review.yml`, `.github/scripts/ai_review.py`

