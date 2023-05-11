import bs4, requests

def getAmazonPrice(productUrl):
    res=requests.get(productionUrl)
    res.raise_for_status()

    soup=bs4.BeautifulSoup(res.text, 'html.parser')
    elems=soup.select('#medianNoAccordion > div.a-row > div.a-column.a-span7.a-text-right.a-span > span.a-size-medium.a-color-price.header-price')
    return elems[0].text.strip()
    

getAmazonPrice('https://www.amazon.com/Defiant-Skyward-Brandon-Sanderson/dp/0593309715/?_encoding=UTF8&pd_rd_w=7TCbb&content-id=amzn1.sym.3231f70a-83f6-4cbe-a07c-05f81963a64f&pf_rd_p=3231f70a-83f6-4cbe-a07c-05f81963a64f&pf_rd_r=NTT4SJE9VHVRDH0GEEBB&pd_rd_wg=CEnb9&pd_rd_r=b2e29f82-4a30-4528-b20d-9f9a81c2ed41&ref_=pd_gw_bmx_gp_aa71az9n')
print('The Price is '+price)
