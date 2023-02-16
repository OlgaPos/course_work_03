import requests
from datetime import datetime
from pprint import pprint


def get_data(url):
    try:
        # Через request делаем запрос на данные
        response = requests.get(url)
        # Если запрос успешный, то возвращаем данные в виде json и комментарий, что данные получены.
        if response.status_code == 200:
            return response.json(), "Данные получены успешно\n"
        # Вернём None с описанием другого статус кода.
        return None, f"status_code: {response.status_code}\n"
    # Вернём None с описанием ошибки в случае ошибки подключения к адресу.
    except requests.exceptions.ConnectionError:
        return None, "ConnectionError\n"
    # Вернём None с описанием ошибки в случае, если данные не переводятся в json.
    except requests.exceptions.JSONDecodeError:
        return None, "JSONDecodeError\n"


def get_filtered_data(transactions_base, filtered_empty_from=False):
    """
    Отсеиваем транзакции, у которых нет EXECUTED и поле from пусто.
    :param transactions_base:
    :param filtered_empty_from:
    :return: Отфильтрованные данные
    """
    # Возьмём из базы первые 5 значений.
    transactions_base = [x for x in transactions_base if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        transactions_base = [x for x in transactions_base if "from" in x]
    return transactions_base


def get_last_values(data, count_last_values):
    """
    Выводит нужное количество последних транзакций.
    :param data:
    :param count_last_values:
    :return: Список последних транзакций.
    """
    # Используем обычную сортировку.
    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def get_formatted_data(data):
    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]
        from_info, from_account = "", ""
        if "from" in row:
            sender = row["from"].split()
            from_account = sender.pop(-1)
            from_account = f"{from_account[:4]} {from_account[4:6]}** **** {from_account[-4:]}"
            from_info = " ".join(sender)
        to = f"{row['to'].split()[0]} **{row['to'][-4:]}"
        operation_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{from_info} {from_account} -> {to}
{operation_amount}""")
    return formatted_data
