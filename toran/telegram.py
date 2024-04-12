#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2024-03-30 16:30

"""Telegram."""



__author__ = 'Toran Sahu <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the MIT license'

import logging
import argparse

from utils import setup_logging
from telegram.client import Telegram

"""
Sends a message to a chat
Usage:
    python examples/send_message.py api_id api_hash phone chat_id text
https://github.com/alexander-akhmetov/python-telegram
https://core.telegram.org/tdlib/getting-started
"""


if __name__ == '__main__':
    setup_logging(level=logging.INFO)

    parser = argparse.ArgumentParser()
    parser.add_argument('api_id', help='API id')  # https://my.telegram.org/apps
    parser.add_argument('api_hash', help='API hash')
    parser.add_argument('phone', help='Phone')
    parser.add_argument('chat_id', help='Chat id', type=int)
    parser.add_argument('text', help='Message text')
    args = parser.parse_args()

    tg = Telegram(
        api_id=args.api_id,
        api_hash=args.api_hash,
        phone=args.phone,
        database_encryption_key='changeme1234',
    )
    # you must call login method before others
    tg.login()

    # if this is the first run, library needs to preload all chats
    # otherwise the message will not be sent
    result = tg.get_chats()

    # `tdlib` is asynchronous, so `python-telegram` always returns you an `AsyncResult` object.
    # You can wait for a result with the blocking `wait` method.
    result.wait()

    if result.error:
        print(f'get chats error: {result.error_info}')
    else:
        print(f'chats: {result.update}')

    result = tg.send_message(
        chat_id=args.chat_id,
        text=args.text,
    )

    result.wait()
    if result.error:
        print(f'send message error: {result.error_info}')
    else:
        print(f'message has been sent: {result.update}')
