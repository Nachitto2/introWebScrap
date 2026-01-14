import requests, sys,webbrowser,bs4

if len(sys.argv)>1:
    res = requests.get('https://pypi.org/search/?q=' +' '.join(sys.argv[1:]))
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text,"html parser")
    link_elem = soup.select(".package-snippet")

    num_open = min(5,len(link_elem))

    for i in range(num_open):
        url_to_open= ""+ link_elem[i].get("href")
        print("Opening...", url_to_open)
        webbrowser(url_to_open)
else:
    print("Nada")