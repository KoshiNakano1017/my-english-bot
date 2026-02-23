from __future__ import annotations

from services.types import UserState

# ユーザーデータを保持する辞書
# { user_id: {"situation": str, "target_vocab": list, "turn_count": int} }
user_states: dict[int, UserState] = {}


def get_state(user_id: int) -> UserState:
    if user_id not in user_states:
        user_states[user_id] = {
            "situation": "Casual conversation",
            "target_vocab": [],
            "turn_count": 0
        }
    return user_states[user_id]

def update_state(
    user_id: int,
    *,
    situation: str | None = None,
    target_vocab: list[str] | None = None,
    turn_count: int | None = None,
) -> None:
    state = get_state(user_id)
    if situation is not None:
        state["situation"] = situation
    if target_vocab is not None:
        state["target_vocab"] = target_vocab
    if turn_count is not None:
        state["turn_count"] = turn_count


def increment_turn(user_id: int) -> int:
    state = get_state(user_id)
    state["turn_count"] += 1
    if state["turn_count"] > 10:
        state["turn_count"] = 1 # アドバイス後は1にリセット
    return state["turn_count"]

# --- Backward-compatible API (used by main.py) ---

def get_user_state(user_id: int) -> UserState:
    return get_state(user_id)


def update_user_setting(
    user_id: int,
    situation: str | None = None,
    target_vocab: list[str] | None = None,
) -> None:
    update_state(user_id, situation=situation, target_vocab=target_vocab)
