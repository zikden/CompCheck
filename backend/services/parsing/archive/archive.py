from bs4 import BeautifulSoup as bs
from lxml import etree
import requests

from archive.models import ProcessorModel


URL = "https://benchmark.best/en/"
PROCESSOR_URL = "https://benchmark.best/en/cpu_table.html"
VIDEOCARD_URL = "https://benchmark.best/en/gpu_specif.html"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0",
}


class ParsingProcessor:
    """Parsint site processors"""

    def __init__(self) -> None:
        self.responce = requests.get(PROCESSOR_URL, headers=HEADERS)

    def parsing_main_CPU(self):
        soup = bs(self.responce.text, "lxml")
        tbody = soup.find("tbody")
        trs = tbody.find_all("tr")
        model_processors = list(ProcessorModel.objects.all().values_list("name"))
        for i, tr in enumerate(trs):
            if i == 5:
                break
            processor = tr.find("td", class_="cpus2")
            processor_link = URL + processor.find('a').get('href')
            processor = processor.text

            if "AMD" or "amd" in processor:
                brand = "AMD"
                processor = processor.replace("AMD", "")
                processor = processor.replace("amd", "")
            elif "intel" or "Intel" or "INTEL" in processor:
                brand = "Intel"
                processor = processor.replace("intel", "")
                processor = processor.replace("Intel", "")
                processor = processor.replace("INTEL", "")

            processor = processor.strip()

            if processor not in model_processors:
                ranking = tr.find("span", class_="spandiag").text
                min_frequency = tr.find("td", class_="cpus4").text.replace(" MHz", "")
                max_frequency = tr.find("td", class_="cpus5").text.replace(" MHz", "")
                core, threads = tr.find("td", class_="cpus6").text.split("/")
                core = core.replace(" ", "")
                threads = threads.replace(" ", "")
                soket, tdp = self.parsing_secondory_CPU(processor_link)
            else:
                continue
            # yield brand, processor, ranking, min_frequency, max_frequency, core, threads

    def parsing_secondory_CPU(self, url: str):
        responce = requests.get(url, headers=HEADERS)
        soup = bs(responce.text, "html.parser")
        tdp_search = soup.find_all('td', class_="tdc2")[10].text

        soket = soup.find("td", id="tdsocketid").text
        tdp = tdp_search.replace(' W', '')
        return soket, tdp


class ParsingVideoCard:
    def __init__(self, url: str) -> None:
        self.url = url

    def parsing(self): ...

    def save(self): ...
