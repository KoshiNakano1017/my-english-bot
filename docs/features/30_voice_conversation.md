## 音声会話（Telegram Voice → Gemini → テキスト返信）

### 目的
- ユーザーの英語音声に対して、状況（Situation）に沿った自然な返答を返す。

### 入口（トリガー）
- Telegram の **voice メッセージ**（`message.voice`）

### 入力
- Telegram voice: `file_id`
- ユーザー状態: `situation / target_vocab / turn_count`

### 処理フロー（現状）
1) **音声ファイル取得**
- `utils/audio_handler.download_voice(file_id, user_id)` が Telegram API から `.ogg` をダウンロード

2) **ターン更新**
- `services/state_manager.increment_turn(user_id)` で `turn_count` を進める

3) **Geminiへ送信**
- `services/gemini_api.chat_with_gemini(audio_path, state)` で
  - 状況・キーワード・進捗（turn_count）を含むプロンプトを作成
  - 音声ファイルをアップロードして生成
  - 10ターン目は `--- ADVICE ---` を末尾に付ける指示を追加

4) **返信**
- `services/telegram_bot.send_message(chat_id, text)` でテキスト返信

5) **後片付け**
- `utils/audio_handler.cleanup_voice(audio_path)` でローカルファイル削除

### 出力
- Telegram へ **テキスト**で返信（音声返信は未実装）

### 状態（永続化）
- なし（ターン数などはメモリ上）

### 制約・注意
- Geminiへの入力として「音声を直接渡す」前提（モデル/SDK仕様によってはSTTが必要）
- 外部API失敗時の例外処理・再試行は未整備
- 返信の音声化（TTS）/ `sendVoice` は未実装

### 関連ファイル
- `main.py`
- `utils/audio_handler.py`
- `services/gemini_api.py`
- `services/state_manager.py`
- `services/telegram_bot.py`

