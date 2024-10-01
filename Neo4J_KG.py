from langchain.text_splitter import MarkdownTextSplitter 
from concurrent.futures import ThreadPoolExecutor
import re
from typing import Optional, List

def clean_text(text: str):
    # Delete the pattern [MISSING_PAGE_FAIL:x]
    cleaned_text = re.sub(r"\[MISSING_PAGE_FAIL:\d+\]", "", text)

    # Delete the acknowledgements section
    cleaned_text = re.sub(
        r"## Acknowledgements.*?(?=##|$)", "", cleaned_text, flags=re.S
    )

    # delete the references section 
    cleaned_text = re.sub(r"## *Notes And References.*", "", cleaned_text, flags=re.S)

    return cleaned_text

def process_file(text: str, metadatas: Optional[dict] = None):
    splitter = MarkdownTextSplitter(chunk_size=2000, chunk_overlap=0)
    return splitter.create_documents([text], [metadatas])


def extract_nodes(documents, llm, max_workers: int = 1):
    def process_document(doc):
        return llm.convert_to_graph_documents([doc])

    graph_documents = []

    with ThreadPoolExecutor(max_workers = max_workers) as executor:
        futures = [executor.submit(process_document, document) for document in documents]

        for future in futures:
            graph_document = future.result()
            graph_documents.extend(graph_document)

    return graph_documents

