import services.gemini_api as gemini_api


def test_gemini_api_exports():
    assert hasattr(gemini_api, "chat_with_gemini")
