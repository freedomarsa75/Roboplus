from openpulse.config import Settings


def test_settings_can_load_from_environment(monkeypatch):
    monkeypatch.setenv("TELEGRAM_BOT_TOKEN", "test-token")
    settings = Settings(_env_file=None)
    assert settings.telegram_bot_token.get_secret_value() == "test-token"
    assert settings.log_level == "INFO"
