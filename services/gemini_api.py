import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

async def chat_with_gemini(audio_path, state):
    model = genai.GenerativeModel('gemini-1.5-flash-8b')
    
    turn_count = state["turn_count"]
    # 10回に1回のアドバイスフラグ
    give_advice = (turn_count % 10 == 0)

    # 命令文の構築
    prompt = f"""
    # Role
    You are an English conversation partner.
    
    # Context
    - Situation: {state['situation']}
    - Target Vocabulary: {', '.join(state['target_vocab'])}
    - Current Progress: {turn_count}/10 messages.

    # Instructions
    1. Listen to the user's audio and respond naturally in the given situation.
    2. Try to use the target vocabulary in your response to encourage the user.
    """
    
    if give_advice:
        prompt += """
        3. SPECIAL: Since this is the 10th turn, add a section '--- ADVICE ---' at the end.
        Provide feedback on grammar mistakes and suggest more natural idioms used in this conversation.
        """

    audio_file = genai.upload_file(path=audio_path)
    response = model.generate_content([prompt, audio_file])
    return response.text