import requests


def io_bound_func():
    result = requests.get("https://google.com")
    return result


if __name__ == "__main__":
    for i in range(5):
        result = io_bound_func()
