import pandas as pd
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from langchain_experimental.graph_transformers import LLMGraphTransformer
from Neo4J_KG import clean_text, process_file, extract_nodes
from MOFKG_Properties import ALLOWED_NODES, ALLOWED_RELATIONSHIPS, NODE_PROPERTIES, RELATIONSHIP_PROPERTIES
from Prompt_MOF import default_prompt
import os

# Make sure you download APOC and GDS plugins if using local host
# Make sure you have opened the graph first on Neo4j Local
os.environ["NEO4J_URI"] = "bolt://localhost:7687"
os.environ["NEO4J_USERNAME"] = "neo4j"
os.environ["NEO4J_PASSWORD"] = "AI4ChemS"

graph = Neo4jGraph(refresh_schema=False)

data = pd.read_csv("cif data/csv/CoRE_QMOF_expanded_filtered.csv")

input_file = "data/md/4/4.md"
input_doi = "10.1039/C5RA15937G"  # This can be easily found by appending a new column in the .csv with a "document id"

# Read md
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Clean the text
text = clean_text(content)

# Initialize metadata dictionary
metadata = {
    "id": input_doi,
    "MOFs": {}
}

# Filter DataFrame by DOI
filtered_df = data[data["DOI"] == input_doi]

# Iterate through the filtered DataFrame and populate the MOFs in metadata
for _, row in filtered_df.iterrows():
    mof_name = row["CSD code"]
    metals = row["Metal types"]
    space_group = row["Space group"]
    molecular_formula = row["Molecular formula"]
    
    # Store the MOF and its band gap in the metadata
    metadata["MOFs"][mof_name] = {
        "Metals": metals,
        "Space Group": space_group,
        "Molecular formula": molecular_formula
    }

RefCodes = list(metadata['MOFs'].keys())

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Loop through each RefCode and update csd_info
for ref_code in RefCodes:
    csd_info = f"Properties: [Metals: {metadata['MOFs'][ref_code]['Metals']}, \
    Space Group: {metadata['MOFs'][ref_code]['Space Group']}, \
    Molecular Formula: {metadata['MOFs'][ref_code]['Molecular formula']}]"

    # Print to check the csd_info for each iteration
    print(csd_info)

    # Pass text and metadata to the process_file function
    docs = process_file(text, metadatas={'id': metadata['id']})

    # Create a new transformer for each RefCode with updated csd_info
    llm_transformer = LLMGraphTransformer(llm=llm,
                                          allowed_nodes=ALLOWED_NODES,
                                          allowed_relationships=ALLOWED_RELATIONSHIPS,
                                          node_properties=NODE_PROPERTIES, 
                                          relationship_properties=RELATIONSHIP_PROPERTIES,
                                          prompt=default_prompt.partial(csd_info=csd_info))

    # Extract nodes and add to the graph
    graph_docs = extract_nodes(docs, llm_transformer, 10)
    graph.add_graph_documents(graph_docs, baseEntityLabel=True, include_source=True)
