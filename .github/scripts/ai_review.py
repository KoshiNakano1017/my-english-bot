import google.generativeai as genai
import os
import subprocess

genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# 今回のPushでの変更点(Diff)を取得
diff = subprocess.getoutput("git diff HEAD~1 HEAD")

prompt = f"""
あなたはシニアエンジニアです。以下のコードの差分をレビューしてください。
1. PEP8などのコーディング規約に則っているか
2. ロジックのバグや、音声処理の不備がないか
3. より良い書き方（自然なPythonの書き方）があれば提案

Diff:
{diff}
"""

if diff:
    response = model.generate_content(prompt)
    print("=== Gemini AI Review Results ===")
    print(response.text)
else:
    print("No changes to review.")