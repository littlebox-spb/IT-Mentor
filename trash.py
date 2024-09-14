lst_in = [
    "ustanovka-i-zapusk-yazyka",
    "ustanovka-i-poryadok-raboty-pycharm",
    "peremennyye-operator-prisvaivaniya-tipy-dannykh",
    "arifmeticheskiye-operatsii",
    "ustanovka-i-poryadok-raboty-pycharm",
]


d = {}
for url in lst_in:
    if url in d:
        print(f"Взято из кэша: HTML-страница для адреса {url}")
    else:
        d[url] = url
        print(f"HTML-страница для адреса {url}")
