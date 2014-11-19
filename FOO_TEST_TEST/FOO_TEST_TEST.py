# -*- coding: utf-8 -*-


__author__ = 'ipetrash'


# TODO: добавить
# def mils2mm(mils):
#     """Функция конвертирует mils (1/1000 дюйма) в mm (миллиметры)."""
# 
#     mm = (mils / 1000) * 25.4
#     return round(mm, 2)
#     # return mm
#     # return int(mm)
# 
# 
# def mm2mils(mm):
#     """Функция конвертирует mm (миллиметры) в mils (1/1000 дюйма)."""
# 
#     mils = (mm * 1000) / 25.4
#     return round(mils, 2)
#     # return mils
#     # return int(mils)
# 
# 
# print("Horizontal Offset Limits: {} mm - {} mm".format(mils2mm(280), mils2mm(3025)))
# print("Vertical Offset Limits: {} mm - {} mm".format(mils2mm(135), mils2mm(860)))
# print()
# print("Horizontal Offset Limits: {} mils - {} mils".format(mm2mils(7.11), mm2mils(76.83)))
# print("Vertical Offset Limits: {} mils - {} mils".format(mm2mils(3.43), mm2mils(21.84)))


# TODO: получение курса валют 1 USD -> ? RUB: http://news.yandex.ru/quotes/1.html


__author__ = 'ipetrash'

"""Модуль для возвращения информации о ранобе."""


# def get_ranobe_info_from_ruranobe(url):
#     """Функция возвращает словарь, содержащий информацию о ранобе."""
#
#     from grab import Grab
#
#     g = Grab()
#     g.setup(hammer_mode=True)
#     g.go(url)
#
#     # Если не удачно, выходим
#     if g.response.code != 200:
#         print("Не найден {}.".format(url))
#         return
#
#     # Получение основного контекста, содержащий аннотацию и ссылки на тома
#     content_text = g.doc.select('//div[@id="mw-content-text"]')
#
#     # Получение названия ранобе
#     name_ranobe = g.doc.select('//h1[@id="firstHeading"]').text()
#
#     # Получение и объединение параграфов в единый текст
#     annotation = '\n'.join(r.text() for r in content_text.select('p/i'))
#
#     # Получение списка томов
#     list_volumes = content_text.select('ul/li/a')
#
#     info = {
#         "name": name_ranobe,
#         "annotation": annotation,
#         "list_volumes": list_volumes,
#         "url": url,
#     }
#     return info
#
# ranobe_info = get_ranobe_info_from_ruranobe('http://ruranobe.ru/r/sao')
# print(ranobe_info['annotation'])
# for i, volume in enumerate(ranobe_info['list_volumes'], 1):
#     print('{}. "{}"'.format(i, volume.text()))


# TODO: pretty xml
# from xml.dom.minidom import parseString
#
# def pretty_xml(xml, ind=' ' * 2):
#     """Функция принимает строку xml и выводит xml с отступами."""
#
#     return parseString(xml).toprettyxml(indent=ind)
#
#
# from lxml import etree
#
# def pretty_xml(xml_str):
#     """Функция принимает строку xml и выводит xml с отступами."""
#
#     root = etree.fromstring(xml_str)
#     return etree.tostring(root, pretty_print=True)



# def split_words_in_capitalize(text):
#     """Функция разделяем слитные слова, на пересечении разных регистров или при встрече с цифрой и оформляет строку
#        в виде предложения: первый символ заглавный, остальные строчные.
#        Пример: CardsPickedSinceCleaningCard -> Cards picked since cleaning card
#                TotalPickedInputHopper6      -> Total picked input hopper 6
#     """
#     if not text:
#         return text
# 
#     res = ''
#     for c in text:
#         res += " " + c if c.isupper() or c.isdigit() else c
# 
#     # Удаление пробелов с краев
#     res = res.strip()
# 
#     # Первый символ в верхний регистр, остальные в нижний
#     return res.capitalize()


# import re
# import os
# # file_name = input("File name: ")
# file_name = "D:\hosts.txt"
# if os.path.exists(file_name):
#     with open(file_name) as file:
#         for row in file:
#             m = re.search(r"(\d{1,3}).(\d{1,3}).(\d{1,3}).(\d{1,3})(/(\d{1,3}))?", row)
#             if m:
#                 ip = m.group(0)
#                 ip_1 = m.group(1)
#                 ip_2 = m.group(2)
#                 ip_3 = m.group(3)
#                 ip_4 = m.group(4)
#                 ip_5 = m.group(6)  # m.group(5) -- this (/([0-9]{1,3})), m.group(6) -- ([0-9]{1,3})
#                 if ip_5:
#                     print("ip: '{}':\n    1:'{}' 2:'{}' 3:'{}' 4:'{}' 5:'{}'".format(ip, ip_1, ip_2, ip_3, ip_4, ip_5))
#                 else:
#                     print("ip: '{}':\n    1:'{}' 2:'{}' 3:'{}' 4:'{}'".format(ip, ip_1, ip_2, ip_3, ip_4))
#                 print()


# # Overlay "watermark" image / Наложение "водяного знака" на изображение
# import os
# from PIL import Image, ImageDraw, ImageFont
#
# # from PIL import Image, ImageDraw
# # text = "Hello, PIL!!!"
# # color = (0, 0, 120)
# # img = Image.new('RGB', (100, 50), color)
# # imgDrawer = ImageDraw.Draw(img)
# # imgDrawer.text((10, 20), text)
# # img.save("pil_example-basic-example.png")
#
# path = r"C:\Users\ipetrash\Desktop\pic.png"
# # path = input("Input path: ")
# path = os.path.normpath(path)
# if os.path.exists(path):
#     print("File: %s" % path)
#
#     image = Image.open(path)
#     width, height = image.size
#     # image.show()
#
#     drawer = ImageDraw.Draw(image)
#     font = ImageFont.truetype("arial.ttf", 25)
#     text = "Hello World!"
#     width_text, height_text = font.getsize(text)
#     for i in range(0, width, width_text * 2):
#         for j in range(0, height, height_text * 2):
#             drawer.text((i, j), text, font=font, fill=(0x00, 0xff, 0x00))
#
#     image.show()
#     input("")
#     # image.save(path)


# import sqlite3
# # https://docs.python.org/3.4/library/sqlite3.html
# path = r"C:\Users\ipetrash\Desktop\teller\kmaksimov_NDC.sdb"
# conn = sqlite3.connect(path)
# # result = tuple(row for row in conn .cursor().execute("SELECT * FROM BNA_Demoninations"))
# # for s in result:
# #     print(s)
#
# # cursor = conn .cursor()
# # for row in cursor.execute("SELECT * FROM BNA_Demoninations"):
# #     print(row)
#
# c = conn.cursor()
# result = tuple(row for row in c.execute("SELECT * FROM BNA_Demoninations"))
# print(result)
# print(sorted(result, key=lambda x: x[1]))  # sorting by the second value
#
# # Way to get a list of column names
# print()
# # 1
# print("Column names: {0}".format(c.description))
#
# # 2
# result = tuple(row for row in c.execute("PRAGMA table_info('BNA_Demoninations')"))
# print("Column names: {0}".format(result))
#
# # 3
# conn.row_factory = sqlite3.Row
# c = conn.execute('select * from BNA_Demoninations')
# row = c.fetchone()  # instead of cursor.description
# names = row.keys()
# print("Column names: {0}".format(names))


## Conway's Game of Life (1970).
# Место действия этой игры — «вселенная» — это размеченная на клетки поверхность или плоскость — безграничная,
# ограниченная, или замкнутая (в пределе — бесконечная плоскость).
# Каждая клетка на этой поверхности может находиться в двух состояниях: быть «живой» или быть «мёртвой» (пустой).
# Клетка имеет восемь соседей (окружающих клеток).
# Распределение живых клеток в начале игры называется первым поколением. Каждое следующее поколение рассчитывается
# на основе предыдущего по таким правилам:
# в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
# если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; в противном случае
# (если соседей меньше двух или больше трёх) клетка умирает («от одиночества» или «от перенаселённости»).
# Игра прекращается, если на поле не останется ни одной «живой» клетки, если при очередном шаге ни одна из клеток
# не меняет своего состояния (складывается стабильная конфигурация) или если конфигурация на очередном шаге в
# точности (без сдвигов и поворотов) повторит себя же на одном из более ранних шагов (складывается
# периодическая конфигурация).
#
# Эти простые правила приводят к огромному разнообразию форм, которые могут возникнуть в игре.
#
# Игрок не принимает прямого участия в игре, а лишь расставляет или генерирует начальную конфигурацию «живых»
# клеток, которые затем взаимодействуют согласно правилам уже без его участия (он является наблюдателем).
#
# https://github.com/yangit/Life
# http://habrahabr.ru/post/151832/
# https://ru.wikipedia.org/wiki/%D0%96%D0%B8%D0%B7%D0%BD%D1%8C_%28%D0%B8%D0%B3%D1%80%D0%B0%29#.D0.9F.D1.80.D0.B0.D0.B2.D0.B8.D0.BB.D0.B0
# http://habrahabr.ru/post/140581/
# http://habrahabr.ru/company/mailru/blog/228379/


# TODO: добавить пример работы с модулем json
# https://docs.python.org/3.4/library/json.html
# import json


# TODO: больше примеров по модулю psutil_example.
# Ссылки:
#   http://pythonhosted.org/psutil_example/
#   https://github.com/giampaolo/psutil_example


# # TODO: добавление примеров:
# http://jenyay.net/Matplotlib/Date
# http://jenyay.net/Matplotlib/Text
# http://jenyay.net/Matplotlib/Xkcd
# http://jenyay.net/Matplotlib/Locators
# http://jenyay.net/Matplotlib/LogAxes


# ## Quality Control
# # doctest
# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
#
# import doctest
# doctest.testmod()   # automatically validate the embedded tests
#
# # unittest
# import unittest
#
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
#
# unittest.main() # Calling from the command line invokes all tests


# TODO: https://docs.python.org/3/tutorial/stdlib2.html


# TODO: придумать простое приложение и реализовтаь его с помощью TDD (используя unit-тесты)


# TODO: https://gist.github.com/gil9red/021dee2d0be2d15cc04b


# TODO: получение списка доступных кодировок


# TODO: Flask
# "Мега-Учебник Flask, Часть 1: Привет, Мир!": http://habrahabr.ru/post/193242/
# http://ru.wikibooks.org/wiki/Flask


# TODO: Excel
# "Интеграция MS Excel и Python": http://habrahabr.ru/post/232291/


# TODO: tornado
# "Современный Торнадо: распределённый хостинг картинок в 30 строк кода":
# http://habrahabr.ru/post/230607/


# TODO: визуализация связей в вк и linkedin:
# http://habrahabr.ru/post/221251/
# https://github.com/stleon/vk_friends


# TODO: Webmoney API
# http://habrahabr.ru/post/222411/


# TODO: Основы создания 2D персонажа в Godot
# https://github.com/okamstudio/godot/
# "Игровой движок Godot отдали в общественное пользование": http://habrahabr.ru/post/212109/
#
# "Часть 1: компилирование игрового движка, создание проекта и анимация покоя героя":
# http://habrahabr.ru/post/212583/
#
# "Часть 2: компилирование шаблонов, немного о GDScript, движение и анимация героя":
# http://habrahabr.ru/post/212837/


# TODO: "Экспорт Избранного на Хабре в PDF": http://habrahabr.ru/post/208802/
# Оригинал: https://github.com/vrtx64/fav2pdf
# Форк: https://github.com/icoz/fav2pdf


# TODO: Работа с буфером обмена: pyperclip
# http://stackoverflow.com/questions/11063458/python-script-to-copy-text-to-clipboard


# TODO: brutforce Instagram
# http://habrahabr.ru/post/215829/
