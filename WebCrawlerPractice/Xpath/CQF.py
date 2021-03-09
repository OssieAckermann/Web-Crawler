
#-*- coding:utf-8 -*-

from lxml import etree
import requests as rq


def one_page(page_number,cqf_distinction, cqf_ordinary):
    url = 'https://www.cqf.com/why-cqf/global-alumni/alumni-listing?page='+str(page_number)
    response = rq.get(url=url)

    #etree parse
    html = etree.HTML(response.text)
    ind_list = html.xpath("/html/body/div[2]/div[3]/div/div/section/div/div/table/tbody/tr")

    for tr in ind_list:
        name, cohort, country = tr.xpath("td[1]/text()")[0], tr.xpath("td[2]/time/text()")[0], tr.xpath("td[3]/text()")[0]
        if tr.xpath("td[1]/div/text()") == ['D']:
            cqf_distinction.append({"Name":name,
                                    "Cohort":cohort,
                                    "Country":country})
        else:
            cqf_ordinary.append({"Name": name,
                                "Cohort": cohort,
                                "Country": country})

if __name__ == '__main__':
    global cqf_distinction
    global cqf_ordinary
    cqf_distinction = []
    cqf_ordinary = []
    for page_number in range(1,102):
        one_page(page_number,cqf_distinction, cqf_ordinary)
        print("page "+str(page_number)+' completed')
    print(len(cqf_ordinary))
    print(len(cqf_distinction))