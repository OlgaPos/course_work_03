from utils import get_data


def main():
    DATA_STORAGE_URL = "https://www.jsonkeeper.com/b/ENNN"
    transactions_base, info = get_data(DATA_STORAGE_URL)
    if not transactions_base:
        exit(info)
    else:
        print(info)


if __name__ == "__main__":
    main()
