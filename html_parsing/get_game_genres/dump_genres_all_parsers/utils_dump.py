#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from glob import glob
import importlib.util
import os
import sys
from typing import Dict, Callable

# For import common.py
sys.path.append('..')


def module_from_file(file_path: str):
    module_name = os.path.splitext(os.path.basename(file_path))[0]
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if module_name not in sys.modules:
        sys.modules[module_name] = module

    return module


def get_funcs_parsers() -> Dict[str, Callable]:
    data = dict()

    for file_name in glob('../*.py'):
        module = module_from_file(file_name)
        if 'get_game_genres' not in dir(module):
            continue

        data[module.__name__.replace('_', '.')] = module.get_game_genres

    return data


def get_parsers() -> list:
    items = []

    for file_name in glob('../*.py'):
        module = module_from_file(file_name)
        for attr in dir(module):
            if not attr.endswith('_Parser'):
                continue

            cls = getattr(module, attr)
            items.append(
                cls.instance()
            )

    return items


if __name__ == "__main__":
    for parser in get_parsers():
        print(f"{parser.get_site_name():<25}: {parser.__class__}")

    # ag_ru                    : <class 'ag_ru.AgRu_Parser'>
    # gamebomb_ru              : <class 'gamebomb_ru.GamebombRu_Parser'>
    # gamefaqs_gamespot_com    : <class 'gamefaqs_gamespot_com.GamefaqsGamespotCom_Parser'>
    # gameguru_ru              : <class 'gameguru_ru.GameguruRu_Parser'>
    # gamer_info_com           : <class 'gamer_info_com.GamerInfoCom_Parser'>
    # gamespot_com             : <class 'gamespot_com.GamespotCom_Parser'>
    # igromania_ru             : <class 'igromania_ru.IgromaniaRu_Parser'>
    # iwantgames_ru            : <class 'iwantgames_ru.IwantgamesRu_Parser'>
    # metacritic_com           : <class 'metacritic_com.MetacriticCom_Parser'>
    # mobygames_com            : <class 'mobygames_com.MobygamesCom_Parser'>
    # playground_ru            : <class 'playground_ru.PlaygroundRu_Parser'>
    # spong_com                : <class 'spong_com.SpongCom_Parser'>
    # stopgame_ru              : <class 'stopgame_ru.StopgameRu_Parser'>
    # store_steampowered_com   : <class 'store_steampowered_com.StoreSteampoweredCom_Parser'>
