import re


def find_name(url=None):
    if url is None:
        return
    return re.findall(r"~[a-zA-Z]+", url)


try:
    with open("urls.txt", "r") as f:
        urls = f.readlines()
        urls = [url.strip().replace("\n", "") for url in urls]
except FileNotFoundError as err:
    print(f"[ERROR]!! {err}")

else:
    for url in urls:
        name = find_name(url)
        print(name[0].replace("~", ""))

