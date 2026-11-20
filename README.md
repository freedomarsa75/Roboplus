# Telegram news assistant

**Bilingual (Persian/English) open-source Telegram news assistant.**

Telegram news assistant is a modular Python project for collecting news from permitted sources, filtering duplicates, preparing AI-assisted summaries, and publishing reviewed updates to Telegram.

> **Current status:** Phase 1 foundation. The Telegram bot skeleton and project tooling are included. News ingestion, AI summarization, persistence, and publishing workflows will be implemented in later phases.

## Features planned

- Telegram bot interface (commands and admin controls)
- Pluggable news-source adapters
- Duplicate detection and source attribution
- Persian/English summaries and translation
- Optional OpenAI integration
- Review-before-publish workflow
- Automated tests and GitHub Actions

## Quick start

### 1. Requirements

- Python 3.11+
- A Telegram bot token from [@BotFather](https://t.me/BotFather)
- Optional OpenAI API key for later AI features

### 2. Clone and install

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/OpenPulse-AI.git
cd OpenPulse-AI

python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

python -m pip install --upgrade pip
pip install -e ".[dev]"
```

### 3. Configure environment

```bash
cp .env.example .env
```

On Windows PowerShell use `Copy-Item .env.example .env`.

Set `TELEGRAM_BOT_TOKEN` in `.env`. Never commit `.env` or real credentials.

### 4. Run

```bash
python -m openpulse
```

Then open your bot in Telegram and send `/start`.

## Configuration

| Variable | Required | Description |
|---|---:|---|
| `TELEGRAM_BOT_TOKEN` | Yes | Token from BotFather |
| `OPENAI_API_KEY` | No | Reserved for optional AI features |
| `OPENAI_MODEL` | No | Model name used by the future AI adapter |
| `LOG_LEVEL` | No | `DEBUG`, `INFO`, `WARNING`, or `ERROR` |

## Development

```bash
pytest
ruff check .
ruff format --check .
```

## Project structure

```text
src/openpulse/
├── bot/                 # Telegram handlers
├── core/                # Domain logic and pipeline
├── integrations/        # External service adapters
├── config.py            # Environment configuration
└── main.py              # Application entry point
tests/                   # Automated tests
```

## Responsible use

- Use public, authorized, or otherwise permitted news sources.
- Respect Telegram terms, source terms, copyright, and rate limits.
- Keep the original source link with every news item.
- Do not present AI-generated summaries as verified reporting.
- Require human review before publishing until moderation and quality controls are proven.
- Store secrets in environment variables or a secrets manager, never in source code.


## زبان فارسی

**Telegram news assistant** یک پروژه متن‌باز و دوزبانه برای ساخت دستیار خبری تلگرام است. هدف پروژه جمع‌آوری خبر از منابع مجاز، حذف موارد تکراری، خلاصه‌سازی فارسی و انگلیسی با کمک هوش مصنوعی و انتشار کنترل‌شده در تلگرام است.

**وضعیت فعلی:** مرحله اول؛ زیرساخت مخزن، اسکلت ربات تلگرام، تنظیمات و تست خودکار آماده شده‌اند. قابلیت دریافت خبر، اتصال کامل هوش مصنوعی، پایگاه داده و انتشار اخبار در مراحل بعدی اضافه می‌شوند.

### راه‌اندازی سریع

1. Python نسخه 3.11 یا بالاتر نصب کنید.
2. مخزن را دریافت و محیط مجازی بسازید.
3. وابستگی‌ها را نصب کنید: `pip install -e ".[dev]"`
4. فایل `.env.example` را به `.env` کپی کنید.
5. مقدار `TELEGRAM_BOT_TOKEN` را در `.env` قرار دهید.
6. دستور `python -m openpulse` را اجرا کنید.

**نکته امنیتی:** فایل `.env`، توکن ربات و کلید API را هرگز در GitHub بارگذاری نکنید.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
