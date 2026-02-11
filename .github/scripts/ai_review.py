import os
import subprocess
import sys

# インストール直後のライブラリを確実に読み込むためのインポート
try:
    from google import genai
except ImportError:
    print("Error: google-genai not found. Check installation.")
    sys.exit(1)

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 差分の取得（極限まで絞る：500文字）
diff = subprocess.getoutput("git diff HEAD~1 HEAD")
diff = subprocess.getoutput("git diff HEAD~1 HEAD")
if not diff:
    print("No changes to review.")
    sys.exit(0)

diff_limited = diff[:500] + "\n...(truncated)" if len(diff) > 500 else diff

prompt = f"""
Briefly review this code for PEP8 and logic bugs:
{diff_limited}
"""

try:
    # 2.0-flash-lite は現在最も制限が緩いモデルです
    response = client.models.generate_content(
        model='gemini-3-flash',
        contents=prompt
    )
    print("=== AI Review ===\n" + response.text)
except Exception as e:
    # 制限（429）やエラーが出てもCIを失敗させな
    print(f"Skipped review: {e}")
