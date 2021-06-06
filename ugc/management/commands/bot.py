import logging
from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram.ext import Filters
from telegram.ext import MessageHandler, CommandHandler
from telegram.ext import Updater
from telegram.utils.request import Request
from .handler import *
from json import dumps, loads

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()


class Command(BaseCommand):
    help = 'Telegram-bot'

    def handle(self, *args, **options):
        fp = open("settings.json", "r")
        d = loads(fp.read())
        for key, value in d.items():
            if hasattr(settings, key):
                setattr(settings, key, value)
            else:
                setattr(logging, key, value)
        fp.close()

        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
        )

        bot = Bot(
            request=request,
            token=settings.TOKEN,
            base_url=settings.PROXY_URL,
        )

        updater = Updater(
            bot=bot,
            use_context=True,
        )

        print(bot.get_me())

        dp = updater.dispatcher
        dp.add_handler(CommandHandler(
            'start', start_bot_callback))
        dp.add_handler(CommandHandler(
            'show', show_item_callback))

        dp.add_handler(
            CommandHandler
            (
                'create',
                create_item_callback,
                filters=Filters.user(username=settings.ADMIN_USER)
            )
        )
        dp.add_handler(CommandHandler('update', update_item_callback,
                       filters=Filters.user(username=settings.ADMIN_USER)))
        dp.add_handler(CommandHandler('delete', delete_item_callback,
                       filters=Filters.user(username=settings.ADMIN_USER)))
        dp.add_handler(MessageHandler(
            Filters.command, unknown_command_callback))

        updater.start_polling()
        updater.idle()
