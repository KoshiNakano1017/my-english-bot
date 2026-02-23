from __future__ import annotations

from unittest.mock import AsyncMock, Mock

from fastapi.testclient import TestClient

import main


def test_webhook_text_saves_settings(monkeypatch):
    # Avoid real Telegram API call.
    send_message = AsyncMock()
    monkeypatch.setattr(main.telegram_bot, "send_message", send_message)

    main.state_manager.user_states.clear()
    client = TestClient(main.app)

    payload = {
        "message": {
            "from": {"id": 123},
            "text": "Situation: At a coffee shop\nKeywords: latte, to-go, receipt",
        }
    }
    res = client.post("/webhook", json=payload)
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

    state = main.state_manager.get_user_state(123)
    assert state["situation"] == "At a coffee shop"
    assert state["target_vocab"] == ["latte", "to-go", "receipt"]

    send_message.assert_awaited()
    args, _kwargs = send_message.await_args
    assert args[0] == 123
    assert "Settings Saved" in args[1]
    assert "At a coffee shop" in args[1]


def test_webhook_voice_flow(monkeypatch):
    download_voice = AsyncMock(return_value="temp_123.ogg")
    cleanup_voice = Mock()
    chat_with_gemini = AsyncMock(return_value="Hello from Gemini")
    send_message = AsyncMock()

    monkeypatch.setattr(main.audio_handler, "download_voice", download_voice)
    monkeypatch.setattr(main.audio_handler, "cleanup_voice", cleanup_voice)
    monkeypatch.setattr(main.gemini_api, "chat_with_gemini", chat_with_gemini)
    monkeypatch.setattr(main.telegram_bot, "send_message", send_message)

    main.state_manager.user_states.clear()
    client = TestClient(main.app)

    payload = {"message": {"from": {"id": 123}, "voice": {"file_id": "FILE_ID"}}}
    res = client.post("/webhook", json=payload)
    assert res.status_code == 200
    assert res.json() == {"status": "ok"}

    download_voice.assert_awaited_once_with("FILE_ID", 123)
    chat_with_gemini.assert_awaited()
    send_message.assert_awaited_once_with(123, "Hello from Gemini")
    cleanup_voice.assert_called_once_with("temp_123.ogg")

    state = main.state_manager.get_user_state(123)
    assert state["turn_count"] == 1

