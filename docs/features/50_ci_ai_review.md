## CI（現状: AI Review workflow）

### 目的
- push のたびに差分をGeminiでざっくりレビューして、スタイル/ロジックの粗を早期に見つける。

### トリガー
- GitHub Actions: `on: [push]`

### 処理（現状）
- Python 3.12 をセットアップ
- Gemini SDK（`google-genai`）をインストール
- `git diff HEAD~1 HEAD` を取得してプロンプト化（最大500文字）
- `gemini-2.0-flash-lite` へ投げてレビュー文を出力

### 出力
- Actions のログに `=== AI Review ===` として表示

### 失敗時の挙動（重要）
- 429などでGeminiが失敗しても、例外を握りつぶして「スキップ扱い」で落としにくい設計

### 制約・注意
- `git diff HEAD~1 HEAD` のため、複数コミットが積まれるとレビュー対象が意図とズレる可能性がある
- Secrets の `GEMINI_API_KEY` が必要

### 関連ファイル
- `.github/workflows/ai_review.yml`
- `.github/scripts/ai_review.py`

