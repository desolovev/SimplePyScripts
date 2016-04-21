#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from urllib.parse import urlsplit
import base64


def get_today_RFC1123_date():
    from datetime import datetime
    from babel.dates import format_datetime

    now = datetime.utcnow()
    format = 'EEE, dd LLL yyyy hh:mm:ss'
    return format_datetime(now, format, locale='en') + ' GMT'


def hmac_sha256(key, msg):
    import hmac
    import hashlib
    signature = hmac.new(key, msg, hashlib.sha256).digest()
    return base64.b64encode(signature).decode()


def get_authorization_header(application_id, secret, today_date, url):
    url_parts = urlsplit(url)
    path_and_query = url_parts.path
    if url_parts.query:
        path_and_query += '?' + url_parts.query

    message = "GET\n\n" + today_date + "\n" + path_and_query
    secret = base64.b64decode(secret)
    signature = hmac_sha256(secret, message.encode())

    return "UNIHMAC {}:{}".format(application_id, signature)
