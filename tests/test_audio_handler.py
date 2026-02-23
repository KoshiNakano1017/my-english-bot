import utils.audio_handler as audio_handler


def test_audio_handler_exports():
    assert hasattr(audio_handler, "download_voice")
    assert hasattr(audio_handler, "cleanup_voice")
