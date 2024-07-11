"""Bot."""

from typing import Self

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from pinger.core.config import AppConfig
from pinger.handlers import router


class TgBot:
    """Telegram bot class.

    This class initializes the Telegram bot and
    sets up the dispatcher with the necessary configurations and handlers.
    """

    def __init__(self, config: AppConfig):
        """Initialize the Telegram bot with the given configuration.

        Args:
            config (AppConfig): Application configuration containing the bot token and other settings.
        """
        self.bot = Bot(
            token=config.tgbot.token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )
        self.dispatcher = Dispatcher()
        self.dispatcher.include_router(router)

    @classmethod
    def from_env(cls) -> Self:
        """Create a bot instance from environment variables.

        Returns:
            TgBot: An instance of the TgBot class.
        """
        return cls(AppConfig.from_env())

    async def run(self) -> None:
        """Run the bot.

        This method starts polling for updates and handles incoming messages.
        """
        await self.dispatcher.start_polling(self.bot)
