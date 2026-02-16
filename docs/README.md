# my-english-bot

このプロジェクトは、AI（大規模言語モデル, LLM）を活用した英語学習支援ボットです。

## ディレクトリ構成

- `config.py` : 設定ファイル
- `main.py` : エントリーポイント
- `requirements.txt` : 依存パッケージ
- `docs/` : ドキュメント
- `services/` : サービス層（API連携、状態管理、Telegramボット）
- `utils/` : ユーティリティ（音声処理など）

## 機能概要
- Gemini APIを利用したAI英語学習サポート
- Telegramボットによるユーザーインターフェース
- 音声入力・出力対応

## 開発・テスト方針
- AIによる自動実装・テストを推進
- ドキュメント・テストコードもAIで自動生成

## 実行方法
```bash
python main.py
```

## ライセンス
MIT License