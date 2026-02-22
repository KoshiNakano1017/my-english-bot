## Voice conversation (Telegram Voice → Gemini → text reply)

### Purpose
- Respond naturally to the user's English voice message, following the saved "Situation" context.

### Entry point (trigger)
- Telegram **voice message** (`message.voice`)

### Input
- Telegram voice: `file_id`
- User state: `situation / target_vocab / turn_count`

### Processing (current)
1) **Fetch the voice file**
- `utils/audio_handler.download_voice(file_id, user_id)` downloads an `.ogg` from Telegram via Bot API

2) **Advance the turn**
- `services/state_manager.increment_turn(user_id)` increments `turn_count`

3) **Send to Gemini**
- `services/gemini_api.chat_with_gemini(audio_path, state)`:
  - Builds a prompt including situation, target vocab, and progress (`turn_count`)
  - Uploads the audio and generates a response
  - Every 10th turn, instructs the model to append an `--- ADVICE ---` section

4) **Reply**
- `services/telegram_bot.send_message(chat_id, text)` sends a text reply

5) **Cleanup**
- `utils/audio_handler.cleanup_voice(audio_path)` removes the downloaded file

### Output
- Telegram **text** reply (voice reply is not implemented yet)

### State (persistence)
- None (turn count and settings are in-memory)

### Constraints / notes
- Assumes the model/SDK can accept audio directly; otherwise STT would be required
- Error handling / retry for external APIs is not fully implemented
- TTS + `sendVoice` is not implemented yet

### Related files
- `main.py`
- `utils/audio_handler.py`
- `services/gemini_api.py`
- `services/state_manager.py`
- `services/telegram_bot.py`

