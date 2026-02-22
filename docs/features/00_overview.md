## 機能一覧（現状の実装）

このフォルダは「いま実装されている機能」を、日本語で同じ型（目的/入力/処理/出力/状態/制約/関連ファイル）で整理したものです。将来案は `docs/new_features.md` にあります。

## 1) Webhook受信（FastAPI）
- **目的**: Telegram Webhook から届く更新を受け取り、text/voice を振り分ける
- **入口**: `POST /webhook`
- **関連**: `main.py`

## 2) 設定保存（Situation / Keywords）
- **目的**: 会話の「状況」と「使いたい単語」をユーザーごとに保持し、以降のプロンプトに反映する
- **入力**: Telegram のテキスト（`Situation:` / `Keywords:` を含む形式）
- **関連**: `services/telegram_bot.py`, `services/state_manager.py`, `main.py`

## 3) 音声会話（Voice → Gemini → Text返信）
- **目的**: Telegram音声を取得し、Geminiに渡して返信テキストを返す
- **入力**: Telegram の voice メッセージ
- **関連**: `utils/audio_handler.py`, `services/gemini_api.py`, `services/telegram_bot.py`, `main.py`

## 4) 状態管理（ユーザー別・会話ターン管理）
- **目的**: user_id ごとに `situation / target_vocab / turn_count` をメモリ上に保持する
- **関連**: `services/state_manager.py`

## 5) Telegram API 送受信（最低限）
- **送信**: `sendMessage` でテキスト返信
- **受信**: voice の実体は `getFile` → file URL からダウンロード
- **関連**: `services/telegram_bot.py`, `utils/audio_handler.py`

## 6) GitHub Actions（AI Review）
- **目的**: push時に差分をGeminiで簡易レビュー（失敗してもCI全体を落とさない設計）
- **関連**: `.github/workflows/ai_review.yml`, `.github/scripts/ai_review.py`

