import bs4, requests

link = "https://autbor.com/example3.html"
response = requests.get(link)

response.raise_for_status()

example_soup = bs4.BeautifulSoup(response.text, "html.parser")

negrita = example_soup.select("p > b")[0].text

foto = example_soup.select("img")[0].get("src")

print(negrita)
print(foto)


