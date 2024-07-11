"""This module contains the router for the bot's handlers."""

from aiogram import Router

from . import ping


router = Router()
router.include_routers(ping.router)
