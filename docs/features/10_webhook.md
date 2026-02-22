## Webhook受信（FastAPI `POST /webhook`）

### 目的
- Telegram Webhook から送られてくる update を受け取り、text/voice を振り分けて処理する。

### 入口（トリガー）
- **HTTP**: `POST /webhook`
- **想定**: Telegram Bot の webhook 設定でこのURLに update が飛んでくる

### 入力
- Telegram update JSON（最低限 `message` を想定）

### 処理フロー（現状）
- update に `message` が無ければ `{"status": "ok"}` で終了
- `message.text` があれば「設定保存」扱い（`services/telegram_bot.parse_settings`）
- `message.voice` があれば「音声会話」扱い（voiceダウンロード→Gemini→テキスト返信）

### 出力
- Webhookの応答は常に `{"status": "ok"}`（Telegramへの返信は別API呼び出しで実施）

### 状態（永続化）
- なし（状態は `services/state_manager.py` のメモリ辞書）

### 依存（外部）
- Telegram Bot API（受信はWebhook、返信は `sendMessage` / 音声取得は `getFile`）
- Gemini API（音声会話時）

### 制約・注意
- エラーハンドリングが薄い（外部API失敗時の通知/再試行/ログ整備は未実装）
- 永続化が無いので、プロセス再起動でユーザー状態は消える

### 関連ファイル
- `main.py`
- `services/telegram_bot.py`
- `services/state_manager.py`
- `utils/audio_handler.py`
- `services/gemini_api.py`

