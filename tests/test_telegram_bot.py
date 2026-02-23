import services.telegram_bot as telegram_bot


def test_parse_settings_parses_both_fields():
    sit, keywords = telegram_bot.parse_settings("Situation: Cafe\nKeywords: a, b, c")
    assert sit == "Cafe"
    assert keywords == ["a", "b", "c"]
