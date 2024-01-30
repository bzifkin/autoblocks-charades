import json
from typing import List, Any

from langchain.utilities import GoogleSerperAPIWrapper
from langchain.llms.openai import OpenAI
from langchain.agents import initialize_agent, Tool
import dotenv


dotenv.load_dotenv("../../.env")

if __name__ == "__main__":

    search = GoogleSerperAPIWrapper()
    llm = OpenAI(temperature=0)


    def get_job_search_results(query: str) -> list[Any]:
        """Searches google for the exact query provided by the user."""
        print('Query:    ', query, '/n')
        results = search.results(query)
        return results


    def get_links_from_search_results(postings: dict) -> list[Any]:
        """Extracts the links from the search results."""
        links_list = []
        for i in range(10):
            link = postings.get("organic")[i].get("link")
            links_list.append(link)

        print(links_list)
        return links_list


    tools = [
        Tool(
            name='Get job search results',
            func=get_job_search_results,
            description=f"Searches google for jobs using the users exact input.",
        ),
        Tool(
            name='Get links from results',
            func=get_job_search_results,
            description=f"Extracts the apply.workable.com link from the results.",
        ),
    ]

    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    print(agent.agent.llm_chain.prompt.template)
    output = agent.run("find jobs matching: devops san francisco site:https://apply.workable.com/")
    print(output)
