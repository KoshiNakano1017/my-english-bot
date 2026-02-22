## 状態管理（ユーザー別 State / ターン管理）

### 目的
- user_id ごとに会話設定と進捗（ターン数）を保持し、会話体験を継続させる。

### 管理している状態（現状）
`services/state_manager.py` のメモリ辞書 `user_states` に保持します。

- `situation`: 会話の状況（例: "Casual conversation"）
- `target_vocab`: 使わせたい単語リスト
- `turn_count`: 会話ターン数（1〜10 を循環）

### 主なAPI（現状）
- `get_state(user_id)` / `update_state(user_id, **kwargs)`
- `increment_turn(user_id)`

### 互換API（main.py から利用）
過去/別実装の呼び出し名に合わせるため、以下を提供します。

- `get_user_state(user_id)` → `get_state(user_id)`
- `update_user_setting(user_id, situation=None, target_vocab=None)` → `update_state(...)`

### 仕様（ターン）
- `increment_turn` で `turn_count` を +1
- 10 を超えたら 1 に戻す（「10回に1回アドバイス」のため）

### 永続化
- なし（プロセス再起動で消える）

### 制約・注意
- 並列処理/スケールアウト（複数プロセス）すると状態が分散して破綻する
- 将来的にDB/Redisなどへの移行が必要

### 関連ファイル
- `services/state_manager.py`
- `main.py`

