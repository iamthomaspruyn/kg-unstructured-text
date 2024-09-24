import os
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer
from Neo4J_KG import clean_text, process_file, extract_nodes
from MOFKG_Properties import ALLOWED_NODES, ALLOWED_RELATIONSHIPS, NODE_PROPERTIES, RELATIONSHIP_PROPERTIES
from Prompt import default_prompt

# Set environment variables
with open(".apikey", 'r') as f:
    os.environ["OPENAI_API_KEY"] = f.read()

# Make sure you download APOC and GDS plugins if using local host
# Make sure you have opened the graph first on Neo4j Local
os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "AI4ChemS"

# Initialize Neo4j graph
graph = Neo4jGraph(refresh_schema=False)

# Define base directory where markdown files are located
base_dir = "data/md"

# Loop through all subdirectories and find .md files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md"):
            # Construct the full path to the markdown file
            input_file = os.path.join(root, file)
            
            # Open and read the markdown file
            with open(input_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Clean the text
            text = clean_text(content)
    
            # Process the file into documents
            docs = process_file(text)

            # Initialize LLM for the transformation
            llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)
            llm_transformer = LLMGraphTransformer(llm=llm,
                                                  allowed_nodes=ALLOWED_NODES,
                                                  allowed_relationships=ALLOWED_RELATIONSHIPS,
                                                  node_properties=NODE_PROPERTIES, 
                                                  relationship_properties=RELATIONSHIP_PROPERTIES,
                                                  prompt=default_prompt)

            # Extract nodes from the documents
            graph_docs = extract_nodes(docs, llm_transformer, 10)

            # Add the graph documents to Neo4j
            graph.add_graph_documents(graph_docs, baseEntityLabel=True, include_source=True)
