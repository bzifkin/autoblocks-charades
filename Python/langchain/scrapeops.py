import re
import json
import requests
from urllib.parse import urlencode

# https://scrapeops.io/web-scraping-playbook/how-to-scrape-indeed/
#  Doesnt work - 403 error
if __name__ == "__main__":

    def get_indeed_search_url(keyword, location, offset=0):
        parameters = {"q": keyword, "l": location, "filter": 0, "start": offset}
        return "https://www.indeed.com/jobs?" + urlencode(parameters)


    headers = {
        "User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

    job_id_list = []

    ## Job Search Parameters
    keyword_list = ['software engineer']
    location_list = ['California']

    ## Loop Through Indeed Pages Until No More Jobs
    for keyword in keyword_list:
        for location in location_list:
            for offset in range(0, 1000, 10):
                try:
                    indeed_jobs_url = get_indeed_search_url(keyword, location, offset)
                    response = requests.get(indeed_jobs_url, headers=headers)
                    print('response: ', offset, response.status_code)

                    if response.status_code == 200:
                        script_tag = re.findall(r'window.mosaic.providerData\["mosaic-provider-jobcards"\]=(\{.+?\});',
                                                response.text)
                        if script_tag is not None:
                            json_blob = json.loads(script_tag[0])
                            jobs_list = json_blob['metaData']['mosaicProviderJobCardsModel']['results']
                            for index, job in enumerate(jobs_list):
                                if job.get('jobkey') is not None:
                                    job_id_list.append(job.get('jobkey'))

                            ## If response contains less than 10 jobs then stop pagination
                            if len(jobs_list) < 10:
                                break

                except Exception as e:
                    print('Error', e)

    print(job_id_list)
