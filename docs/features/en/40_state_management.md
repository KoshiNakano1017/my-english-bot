## State management (per-user state / turn counter)

### Purpose
- Keep conversation settings and progress (turn count) per `user_id` and reuse them across messages.

### State data (current)
Stored in `services/state_manager.py` as an in-memory dict `user_states`.

- `situation`: conversation context (e.g. "Casual conversation")
- `target_vocab`: list of target words to try to use
- `turn_count`: conversation turn number (cycles 1..10)

### Main APIs (current)
- `get_state(user_id)` / `update_state(user_id, **kwargs)`
- `increment_turn(user_id)`

### Compatibility APIs (used by `main.py`)
To match call sites that use different names, the following wrappers exist:

- `get_user_state(user_id)` → `get_state(user_id)`
- `update_user_setting(user_id, situation=None, target_vocab=None)` → `update_state(...)`

### Turn behavior
- `increment_turn` increments `turn_count`
- When it exceeds 10, it resets to 1 (to support "advice every 10 turns")

### Persistence
- None (lost on process restart)

### Constraints / notes
- In-memory state breaks when scaling to multiple processes/instances
- Consider moving to DB/Redis later

### Related files
- `services/state_manager.py`
- `main.py`

