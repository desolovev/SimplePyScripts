#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


import datetime as DT
import json
import time
from typing import Optional

from bs4 import BeautifulSoup
import requests
from peewee import *


def wait(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    from datetime import timedelta, datetime
    from itertools import cycle
    import sys
    import time

    try:
        progress_bar = cycle('|/-\\|/-\\')

        today = datetime.today()
        timeout_date = today + timedelta(
            days=days, seconds=seconds, microseconds=microseconds,
            milliseconds=milliseconds, minutes=minutes, hours=hours, weeks=weeks
        )

        def str_timedelta(td: timedelta) -> str:
            td = str(td)

            # Remove ms
            # 0:01:40.123000 -> 0:01:40
            if '.' in td:
                td = td[:td.rindex('.')]

            # 0:01:40 -> 00:01:40
            if td.startswith('0:'):
                td = '00:' + td[2:]

            return td

        while today <= timeout_date:
            left = timeout_date - today
            left = str_timedelta(left)

            print('\r' + ' ' * 100 + '\r', end='')
            print('[{}] Time left to wait: {}'.format(next(progress_bar), left), end='')
            sys.stdout.flush()

            # Delay 1 seconds
            time.sleep(1)

            today = datetime.today()

        print('\r' + ' ' * 100 + '\r', end='')

    except KeyboardInterrupt:
        print()
        print('Waiting canceled')


def get_price(url: str) -> Optional[int]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
    }

    rs = requests.get(url, headers=headers)

    root = BeautifulSoup(rs.content, 'html.parser')
    price_value = root.select_one('.current-price-value')
    if not price_value:
        return

    return int(price_value['data-price-value'])


# Ensure foreign-key constraints are enforced.
db = SqliteDatabase('tracked_products.sqlite', pragmas={'foreign_keys': 1})


class BaseModel(Model):
    class Meta:
        database = db


class Product(BaseModel):
    title = TextField()
    url = TextField(unique=True)

    def get_last_price(self):
        last_price = self.prices.order_by(Price.date.desc()).first()
        if not last_price:
            return

        return last_price.value


class Price(BaseModel):
    value = DecimalField(null=True)
    date = DateField(default=DT.datetime.now)
    product = ForeignKeyField(Product, backref='prices')

    class Meta:
        indexes = (
            (("product_id", "date"), True),
        )


db.connect()
db.create_tables([Product, Price])

while True:
    try:
        for product_data in json.load(open('tracked_products.json', encoding='utf-8')):
            product, _ = Product.get_or_create(title=product_data['title'], url=product_data['url'])
            last_price = product.get_last_price()

            print(f'Product<title={repr(product.title)} last_price={repr(last_price)} url={repr(product.url)}>')

            current_price = get_price(product.url)
            print('Current price:', current_price)

            # Цена отличается или у продукта еще нет цен
            if current_price != last_price or not product.prices.count():
                print('Append price:', current_price)
                Price.get_or_create(product=product, value=current_price)

            print()

            time.sleep(5)  # 5 seconds

        wait(days=1)

    except Exception as e:
        # Выводим ошибку в консоль
        import traceback
        tb = traceback.format_exc()
        print(tb)

        print('Wait 15 minutes')
        time.sleep(15 * 60)  # 15 minutes