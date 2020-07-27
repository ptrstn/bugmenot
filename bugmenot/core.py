import pathlib

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://bugmenot.com/view/"


def extract_url_name(url):
    parts = pathlib.Path(url).parts
    return parts[0] if "http" not in parts[0] else parts[1]


def extract_credentials(soup):
    dd_elements = soup.findAll("dd")
    statistics = soup.find("dd", {"class": "stats"}).findAll("li")
    return {
        "username": dd_elements[0].text,
        "password": dd_elements[1].text,
        "success_rate": statistics[0].text.rstrip(" success rate"),
        "votes": int(statistics[1].text.rstrip(" votes")),
        "age": statistics[2].text.rstrip(" old"),
    }


def get_credentials(website):
    url_name = extract_url_name(website)
    url = f"{BASE_URL}{url_name}"
    response = requests.get(url)

    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    account_elements = soup.findAll("article", {"class": "account"})

    return [extract_credentials(element) for element in account_elements]
