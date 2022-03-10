from models.dollar_exchange import dollar_exchange
from models.conversion import conversion_doll_real

def main() -> None:
    wallet()


def wallet() -> None:
    doll = dollar_exchange()
    print(f"{'-'*15} Dollar Exchange {'-'*15}")
    print(f"1 US Dollar equal. R${doll:.2f}")
    print(" ")
    print("Conversion...")
    conversion_doll_real(doll)

    #return print('ih')


if __name__ == '__main__':
    main()