# Telegram Botの使用方法と設定手順

## 1. Botの作成
1. Telegramアプリで「BotFather」を検索し、開始
2. `/newbot`と入力し、指示に従ってBot名・ユーザー名を設定
3. 発行された「Botトークン」を控える

## 2. Botの基本設定
- BotFatherでアイコンや説明文を設定可能
- `/setdescription`や`/setuserpic`などのコマンドを利用

## 3. Webhookの設定
1. サーバー（FastAPI等）で`/webhook`エンドポイントを用意し、起動
2. ngrok等でサーバーを外部公開し、URLを取得
3. 以下のURLでWebhookを登録（<YOUR_TOKEN>と<ngrokのURL>を置換）
   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/setWebhook?url=https://<ngrokのURL>/webhook
   ```
4. Webhook登録状況の確認
   ```
   https://api.telegram.org/bot<YOUR_TOKEN>/getWebhookInfo
   ```

## 4. Botの使い方
- TelegramアプリでBotのユーザー名を検索し、「開始」または「/start」
- メッセージや音声を送信すると、サーバー側で処理され自動応答
- Botの機能追加や応答内容はサーバー側の実装で拡張可能

## 5. 注意点
- トークンやWebhook URLは他人に知られないよう管理
- サーバーが停止するとBotも応答しなくなる

---

より詳細な実装例やカスタマイズ方法は、プロジェクトのREADMEやdocsを参照してください。