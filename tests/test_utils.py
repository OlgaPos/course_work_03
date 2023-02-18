import pytest
from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def test_get_data(test_url):
    # Проверим, что длина списка больше нуля.
    assert len(get_data(test_url)[0]) > 0
    # Проверим, что функция отрабатывает при обращении к несуществующему адресу
    # (вообще невозможно соединиться).
    assert get_data("https://no.url.com")[0] is None
    # Проверим, что ссылка идёт на правильный адрес (используем мой существующий адрес).
    assert get_data("https://github.com/OlgaPos")[0] is None
    # Проверим, что возвращает ошибку на существующий сайт, но неправильный адрес.
    assert get_data("https://github.com/OlgaPos/3")[0] is None


def test_get_filtered_data(test_transactions_base):
    # Проверяем, что со словом EXECUTED всего 4 строки.
    assert len(get_filtered_data(test_transactions_base)) == 4
    # Проверяем, что со словом from всего 2 строки.
    assert len(get_filtered_data(test_transactions_base, filtered_empty_from=True)) == 2


def test_get_last_values(test_transactions_base):
    data = get_last_values(test_transactions_base, 4)
    # Проверяем, что на первое место выходит транзакция от 2020 года.
    assert data[0]["date"] == "2020-07-03T18:35:29.512364"
    # Проверяем, что всего 4 транзакции.
    assert len(data) == 4


def test_get_formatted_data(test_transactions_base):
    data = get_formatted_data(test_transactions_base)
    # Проверяем отформатированные значения.
    assert data == ['26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб.', '03.07.2020 Перевод организации\n  -> Счет **5560\n8221.37 USD', '30.06.2018 Перевод организации\nСчет 7510 68** **** 6952 -> Счет **6702\n9824.07 USD', '23.03.2018 Открытие вклада\n  -> Счет **2431\n48223.05 руб.', '04.04.2019 Перевод со счета на счет\nСчет 1970 86** **** 8542 -> Счет **4188\n79114.93 USD']

