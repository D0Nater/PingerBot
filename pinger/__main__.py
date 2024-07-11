"""Main entry point."""

import asyncio

from pinger.bot import TgBot


def main() -> None:
    """Call the CLI."""
    bot = TgBot.from_env()
    asyncio.run(bot.run())


if __name__ == "__main__":
    main()
