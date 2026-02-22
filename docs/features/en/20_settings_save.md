## Settings save (Situation / Keywords)

### What is this?
When a user sends a "settings text" message on Telegram, the bot saves per-user conversation settings in memory. These settings are later included in the Gemini prompt used for voice conversations.

### Purpose
- Persist the conversation **situation** and **target vocabulary** per user to personalize the conversation.

### Entry point (trigger)
- Telegram **text message** (`message.text`)

### Input format (current parser behavior)
Send a text containing `Situation:` and/or `Keywords:` lines.

Example:

```
Situation: At a coffee shop
Keywords: latte, to-go, receipt
```

### What gets saved
Saved in `services/state_manager.py` in an in-memory dict keyed by `user_id`.

- `situation`: string
- `target_vocab`: list of strings (split by comma from `Keywords`)

### Processing (current)
- Parse `situation / keywords` via `services/telegram_bot.parse_settings(text)`
- Update state via `services/state_manager.update_user_setting(user_id, situation, target_vocab)`
- Reply back with a confirmation message via `sendMessage`

### Output
- Telegram text reply confirming settings were saved

### State (persistence)
- None (lost on process restart)

### Constraints / notes
- Parsing is simple string splitting; malformed format won't be recognized
- `Keywords` are stored, but whether they are actually used depends on the prompt and the model response

### Related files
- `main.py`
- `services/telegram_bot.py`
- `services/state_manager.py`

