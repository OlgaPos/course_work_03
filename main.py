from utils import get_data, get_filtered_data, get_last_values, get_formatted_data


def main():
    DATA_STORAGE_URL = "https://www.jsonkeeper.com/b/ENNN"
    FILTERED_EMPTY_FROM = True
    COUNT_LAST_VALUES = 5

    # Базу данных транзакций и инфо получаем из функции get_data по ссылке в константе
    transactions_base, info = get_data(DATA_STORAGE_URL)
    if not transactions_base:
        exit(info)
    else:
        print(info)

    data = get_filtered_data(transactions_base, filtered_empty_from=FILTERED_EMPTY_FROM)
    data = get_last_values(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)

    print("INFO: Вывод данных:")
    for row in data:
        print(row, end='\n\n')


if __name__ == "__main__":
    main()
