## 設定保存（Situation / Keywords）

### これは何？
Telegram に「設定用テキスト」を送ることで、ユーザーごとの会話設定を保存する機能です。保存した内容は、音声会話時に Gemini へ渡すプロンプトの一部になります。

### 目的
- 会話の「状況（Situation）」と「使いたい単語（Keywords）」をユーザー単位で保持し、会話をパーソナライズする。

### 入口（トリガー）
- Telegram の **テキストメッセージ**（`message.text`）

### 入力フォーマット（現状のパース仕様）
以下のように `Situation:` と `Keywords:` を含むテキストを送ると反映されます。

例:

```
Situation: At a coffee shop
Keywords: latte, to-go, receipt
```

### 保存されるデータ
`services/state_manager.py` のメモリ辞書に、user_id ごとに保存されます。

- `situation`: 文字列
- `target_vocab`: 文字列リスト（`Keywords` をカンマ区切りで分割）

### 処理フロー（現状）
- `services/telegram_bot.parse_settings(text)` で `situation / keywords` を抽出
- `services/state_manager.update_user_setting(user_id, situation, target_vocab)` で更新
- `sendMessage` で「保存した」旨の確認メッセージを返す

### 出力（ユーザーへの返信）
- Telegramへテキスト返信（保存完了メッセージ）

### 状態（永続化）
- なし（プロセス再起動で消える）

### 制約・注意
- パースは単純な文字列 split なので、フォーマットが崩れると反映されない
- `Keywords` は現状「保存はされるが、会話で使わせる強制力」はプロンプト依存

### 関連ファイル
- `main.py`
- `services/telegram_bot.py`
- `services/state_manager.py`

