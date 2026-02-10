from google import genai
import os
import subprocess

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

# 差分の取得（極限まで絞る：500文字）
diff = subprocess.getoutput("git diff HEAD~1 HEAD")
diff_limited = diff[:500] + "..." if len(diff) > 500 else diff

# 試行するモデルの優先順位（2026年現在の有効なID）
models_to_try = ['gemini-2.0-flash-exp', 'gemini-2.0-flash', 'gemini-1.5-flash-8b']

success = False
for model_id in models_to_try:
    try:
        response = client.models.generate_content(
            model=model_id,
            contents=f"Review this code briefly: {diff_limited}"
        )
        print(f"=== AI Review ({model_id}) ===\n{response.text}")
        success = True
        break
    except Exception as e:
        print(f"Skipping {model_id}: Quota or error.")

if not success:
    print("All models failed. Quota might be reset tomorrow.")