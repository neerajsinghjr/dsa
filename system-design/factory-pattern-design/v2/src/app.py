from factory.biz_factory import BizFactory
from factory.std_factory import StdFactory


def main():
    v1 = BizFactory.get_type("audi")
    v2 = StdFactory.get_type("maruti")
    vehicles = [v1, v2]
    for v in vehicles:
        if v:
            print(v.info())


if __name__ == "__main__":
    main()