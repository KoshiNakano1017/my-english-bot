## Webhook intake (FastAPI `POST /webhook`)

### Purpose
- Receive Telegram webhook updates and route them to either the text (settings) flow or the voice conversation flow.

### Entry point (trigger)
- **HTTP**: `POST /webhook`
- **Assumption**: Telegram Bot webhook is configured to send updates to this URL

### Input
- Telegram update JSON (currently assumes `message` exists for handling)

### Processing (current)
- If update has no `message`, return `{"status": "ok"}`
- If `message.text` exists, treat it as "settings save" (via `services/telegram_bot.parse_settings`)
- If `message.voice` exists, treat it as "voice conversation" (download voice → Gemini → text reply)

### Output
- Always returns `{"status": "ok"}` to Telegram (actual replies are sent via Telegram Bot API calls)

### State (persistence)
- None in the endpoint itself (state is stored in-memory in `services/state_manager.py`)

### External dependencies
- Telegram Bot API (webhook + `sendMessage`, and `getFile` for voice downloads)
- Gemini API (voice conversation flow)

### Constraints / notes
- Error handling is minimal (no robust logging/retry/reporting yet)
- No persistence; per-user state is lost on process restart

### Related files
- `main.py`
- `services/telegram_bot.py`
- `services/state_manager.py`
- `utils/audio_handler.py`
- `services/gemini_api.py`

