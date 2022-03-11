from models.dollar_exchange import dollar_exchange
from models.conversion import conversion_doll_real
from datetime import datetime


def main() -> None:
    wallet()


def wallet() -> None:
    doll = dollar_exchange()
    print(f"{'-'*15} Dollar Exchange {'-'*15}")
    print(f"1 US Dollar equal. R${doll:.2f} / {datetime.today().strftime('%Y-%m-%d %H:%M')}")
    print(" ")
    print("Conversion...")
    while True:
        conti = str(input("Want to convert more [Y/N]: ")).upper()[0]
        if conti == 'Y':
            conversion_doll_real(doll)
        else:
            print('End...')
            break


if __name__ == '__main__':
    main()