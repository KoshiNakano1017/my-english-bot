# フォルダ構成設計

本プロジェクトの最適なフォルダ構成案は以下の通りです。

```
my-english-bot/
├── config.py                # 設定ファイル
├── main.py                  # エントリーポイント
├── requirements.txt         # 依存パッケージ
├── docs/                    # ドキュメント・設計書・構成図
│   ├── README.md
│   ├── AI_implementation_policy.md
│   ├── architecture.md      # システム構成・設計書
│   └── architecture.mmd     # Mermaid構成図（テキスト形式）
├── services/                # サービス層
│   ├── gemini_api.py        # Gemini API連携
│   ├── state_manager.py     # 状態管理
│   └── telegram_bot.py      # Telegramボット
├── utils/                   # ユーティリティ
│   └── audio_handler.py     # 音声処理
├── tests/                   # テストコード
│   ├── test_gemini_api.py
│   ├── test_state_manager.py
│   ├── test_telegram_bot.py
│   └── test_audio_handler.py
└── data/                    # ユーザー英単語・音声データ等
    └── user_words.json
```

## 機能追加時のポイント
- 新機能ごとにサービス層やユーティリティ層へファイル追加
- テストコードはtests/配下に
- 設計書や構成図はdocs/配下に

## 構成図（Mermaid例）
構成図はarchitecture.mmdとして保存し、Mermaid記法で記述します。
