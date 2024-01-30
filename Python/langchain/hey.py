# import os
#
# os.environ["GOOGLE_CSE_ID"] = "40f4d593849114c6d"
# os.environ["GOOGLE_API_KEY"] = "AIzaSyDR3KLneK0Yj14Ug_OSY-Y54XqcTEBokY4"
#
#
# from langchain.tools import Tool
# from langchain.utilities import GoogleSearchAPIWrapper
#
# # search = GoogleSearchAPIWrapper()
# #
# # tool = Tool(
# #     name="Google Search",
# #     description="Search Google for recent results.",
# #     func=search.run,
# # )
# #
# # tool.run("Obama's first name?")
#
#


from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

loader = AsyncChromiumLoader(["https://www.wsj.com"])
html = loader.load()

bs_transformer = BeautifulSoupTransformer()
docs_transformed = bs_transformer.transform_documents(html, tags_to_extract=["p", "li", "div", "a"])