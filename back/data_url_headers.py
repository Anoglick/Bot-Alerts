from dataclasses import dataclass


@dataclass
class ForPars:
    url = 'https://animego.org/search/all?q='
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/000000000 Safari/537.36'}


all_components = ForPars()