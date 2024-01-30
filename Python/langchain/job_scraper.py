import os
from typing import List, Any

import dotenv
from llama_index import GPTVectorStoreIndex, download_loader
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.chains.conversation.memory import ConversationBufferMemory
from autoblocks.vendor.langchain import AutoblocksCallbackHandler
from autoblocks.tracer import AutoblocksTracer
from langchain.utilities import GoogleSerperAPIWrapper
from langchain.agents import initialize_agent, Tool
import uuid


dotenv.load_dotenv("../../.env")


tracer = AutoblocksTracer(
    ingestion_key=os.environ["AUTOBLOCKS_INGESTION_KEY"],
    trace_id=str(uuid.uuid4()),
    properties=dict(
        provider="openai"
    )
)

if __name__ == "__main__":

    # search = GoogleSerperAPIWrapper()
    llm = OpenAI(temperature=0)
    handler = AutoblocksCallbackHandler()

    # def get_job_search_results(query: str) -> list[Any]:
    #     """Searches google for the exact query provided by the user."""
    #     print('Query:    ', query, '/n')
    #     results = search.results(query)
    #     return results
    #
    # def get_links_from_search_results(postings: dict) -> list[Any]:
    #     """Extracts the links from the search results."""
    #     links_list = []
    #     for i in range(10):
    #         link = postings.get("organic")[i].get("link")
    #         links_list.append(link)
    #
    #     print(links_list)
    #     return links_list


    BeautifulSoupWebReader = download_loader("BeautifulSoupWebReader")
    loader = BeautifulSoupWebReader()
    documents = loader.load_data(urls=[workable_urls])
    print(documents[0].json())
    tracer.send_event("document_loader.data", properties=dict(documents=documents[0].json()))

    index = GPTVectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()


    tools = [
        Tool(
            name='Get job search results',
            func=get_job_search_results,
            description=f"Searches google for jobs using the users exact input.",
        ),
        Tool(
            name='Get links from results',
            func=get_job_search_results,
            description=f"Extracts links from the results.",
        ),
        Tool(
            name="Job detail scraper",
            func=lambda q: query_engine.query(q),
            description=f"Given the details of a job, returns the job details. If details of job are not found, returns an empty list.",
        )
    ]

    memory = ConversationBufferMemory(memory_key="chat_history")

    agent = initialize_agent(
        tools, llm, agent="zero-shot-react-description", memory=memory, verbose=True
    )
    print(agent.agent.llm_chain.prompt.template)
    output = agent.run("devops san francisco site:https://apply.workable.com/", callbacks=[handler])
    print(output)
