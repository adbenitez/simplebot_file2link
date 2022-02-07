"""Plugin's commands definition."""

import functools
import os

import requests
import simplebot
from deltachat import Message
from simplebot.bot import DeltaBot, Replies

session = requests.Session()
session.headers.update(
    {
        "user-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
    }
)
session.request = functools.partial(session.request, timeout=60 * 5)  # type: ignore


@simplebot.hookimpl
def deltabot_init(bot: DeltaBot) -> None:
    _getdefault(bot, "server", "https://0x0.st/")


@simplebot.filter
def file2link(bot: DeltaBot, message: Message, replies: Replies) -> None:
    """Send me any file in private and I will upload it and give you a download link that you can share with others."""
    if not message.chat.is_group() and message.filename:
        num = os.stat(message.filename).st_size
        if num > 1024**2:
            rep = Replies(message, bot.logger)
            rep.add(text="⬆️ Uploading...", quote=message)
            rep.send_reply_messages()
        url = _getdefault(bot, "server")
        try:
            with open(message.filename, "rb") as file:
                with session.post(url, files=dict(file=file)) as resp:
                    resp.raise_for_status()
                    name = os.path.basename(message.filename)
                    size = _sizeof_fmt(num)
                    replies.add(
                        text=f"Name: {name}\nSize: {size}\nLink: {resp.text.strip()}"
                    )
        except requests.RequestException as ex:
            bot.logger.exception(ex)
            replies.add(text="❌ Failed to upload file", quote=message)


def _getdefault(bot: DeltaBot, key: str, value: str = None) -> str:
    val = bot.get(key, scope=__name__)
    if val is None and value is not None:
        bot.set(key, value, scope=__name__)
        val = value
    return val


def _sizeof_fmt(num: float) -> str:
    suffix = "B"
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)  # noqa
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)  # noqa
