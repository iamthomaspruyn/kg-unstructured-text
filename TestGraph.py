from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer
from Neo4J_KG import clean_text, process_file, extract_nodes
from MOFKG_Properties import ALLOWED_NODES, ALLOWED_RELATIONSHIPS, NODE_PROPERTIES, RELATIONSHIP_PROPERTIES
from Prompt import default_prompt
import os

with open(".apikey", 'r') as f:
    os.environ["OPENAI_API_KEY"] = f.read()

# Make sure you download APOC and GDS plugins if using local host
# Make sure you have opened the graph first on Neo4j Local
os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "AI4ChemS"

graph = Neo4jGraph(refresh_schema=False)

input_file = "data/md/1/1.md"

with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# clean the text
text = clean_text(content)

docs = process_file(text)

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
llm_transformer = LLMGraphTransformer(llm=llm,
                                        allowed_nodes=ALLOWED_NODES,
                                        allowed_relationships=ALLOWED_RELATIONSHIPS,
                                        node_properties=NODE_PROPERTIES, 
                                        relationship_properties=RELATIONSHIP_PROPERTIES,
                                        prompt = default_prompt)

graph_docs = extract_nodes(docs, llm_transformer, 10)

print(graph_docs)
print(graph_docs)
print(type(graph_docs))

graph.add_graph_documents(graph_docs, baseEntityLabel=True, include_source=True)
