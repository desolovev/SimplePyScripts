#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from common import get_client, sizeof_fmt


qb = get_client()
torrents = qb.torrents()
total_size = 0

for i, torrent in enumerate(torrents, 1):
    torrent_size = torrent['total_size']
    total_size += torrent_size

    print('{:<3} {} ({})'.format(i, torrent['name'], sizeof_fmt(torrent_size)))

print()
print('Total torrents: {}, total size: {} ({} bytes)'.format(len(torrents), sizeof_fmt(total_size), total_size))
