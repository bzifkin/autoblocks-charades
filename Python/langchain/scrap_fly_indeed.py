from collections import defaultdict
from urllib.parse import quote
from parsel import Selector
from scrapfly import ScrapeConfig, ScrapflyClient

scrapfly_client = ScrapflyClient("scp-live-69c5424dc944438ea385a285006b0ade")


import re
import json
import os

# https://scrapfly.io/blog/how-to-scrape-indeedcom/
#  works
if __name__ == "__main__":

    def parse_search_page(html: str):
        data = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});', html)
        data = json.loads(data[0])
        return {
            "results": data["metaData"]["mosaicProviderJobCardsModel"]["results"],
            "meta": data["metaData"]["mosaicProviderJobCardsModel"]["tierSummaries"],
        }


    result = scrapfly_client.scrape(
        ScrapeConfig(
            url="https://www.indeed.com/jobs?q=python&l=Texas",
            asp=True,
        )
    )
    print(parse_search_page(result.content))



    # def parse_search_results(selector: Selector):
    #     """parse search results from google search page"""
    #     results = []
    #     for box in selector.xpath("//h1[contains(text(),'Search Results')]/following-sibling::div[1]/div"):
    #         title = box.xpath(".//h3/text()").get()
    #         url = box.xpath(".//h3/../@href").get()
    #         text = "".join(box.xpath(".//div[@data-sncf]//text()").getall())
    #         if not title or not url:
    #             continue
    #         url = url.split("://")[1].replace("www.", "")
    #         results.append((title, url, text))
    #     return results
    #
    #
    # def scrape_search(query: str, page=1, country="US"):
    #     """scrape search results for a given keyword"""
    #     # retrieve the SERP
    #     url = f"https://www.google.com/search?hl=en&q={quote(query)}" + (f"&start={10*(page-1)}" if page > 1 else "")
    #     print(f"scraping {query=} {page=}")
    #     results = defaultdict(list)
    #     result = scrapfly.scrape(ScrapeConfig(url, country=country, asp=True))
    #     # parse SERP for search result data
    #     results["search"].extend(parse_search_results(result.selector))
    #     return dict(results)
    #
    # # Example use: scrape 3 pages: 1,2,3
    # for page in [1]:
    #     results = scrape_search("devops san francisco site:https://apply.workable.com/*", page=page)
    #     for result in results["search"]:
    #         print(result)