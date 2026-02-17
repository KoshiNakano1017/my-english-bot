# ユーザーデータを保持辞書
# { user_id: {"situation": str, "target_vocab": list, "turn_count": int} }
user_states = {}

def get_state(user_id):
    if user_id not in user_states:
        user_states[user_id] = {
            "situation": "Casual conversation",
            "target_vocab": [],
            "turn_count": 0
        }
    return user_states[user_id]

def update_state(user_id, **kwargs):
    state = get_state(user_id)
    state.update(kwargs)

def increment_turn(user_id):
    state = get_state(user_id)
    state["turn_count"] += 1
    if state["turn_count"] > 10:
        state["turn_count"] = 1 # アドバイス後は1にリセット
    return state["turn_count"]