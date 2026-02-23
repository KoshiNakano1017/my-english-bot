from __future__ import annotations

from typing import TypedDict


class UserState(TypedDict):
    situation: str
    target_vocab: list[str]
    turn_count: int

