def put_yen(num):
    """
    値を送ると、円をつけて返す関数
    """
    return str(num) + "円"

if __name__ == "__main__":
    print(put_yen(100))
    print(put_yen.__doc__)


