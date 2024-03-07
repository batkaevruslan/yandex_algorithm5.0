def read_inputs() -> tuple[int, int]:
    a, b = list(map(int, input().strip().split()))
    return a, b


def get_sum(a: int, b: int):
    return a + b


def main():
    a, b = read_inputs()
    print(get_sum(a, b))


if __name__ == '__main__':
    main()