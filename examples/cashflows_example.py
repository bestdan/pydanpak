from datetime import date

from pydanpak import Cashflows, total_cashflows


def main():
    cf = Cashflows(cashflows={date(2023, 1, 1): 100.0, date(2023, 7, 1): -50.0})
    print(cf)
    print(f"Total cashflows: {total_cashflows(cf)}")


if __name__ == "__main__":
    main()
