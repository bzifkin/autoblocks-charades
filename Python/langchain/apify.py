from langchain.docstore.document import Document
from langchain.indexes import VectorstoreIndexCreator
from langchain.utilities import ApifyWrapper
import dotenv

# https://python.langchain.com/docs/use_cases/web_scraping#question-answering-over-a-website
#  doesnt work
dotenv.load_dotenv("../../.env")

apify = ApifyWrapper()
# Call the Actor to obtain text from the crawled webpages
loader = apify.call_actor(
    actor_id="apify/website-content-crawler",
    run_input={"startUrls": [{"url": "https://apply.workable.com/api/v2/accounts/smartnews/jobs/C7C1B211D1"}]},
    dataset_mapping_function=lambda item: Document(
        page_content=item["text"] or "", metadata={"source": item["url"]}
    ),
)

# Create a vector store based on the crawled data
index = VectorstoreIndexCreator().from_loaders([loader])

# Query the vector store
query = "What are the required technologies for these roles"
result = index.query(query)
print(result)