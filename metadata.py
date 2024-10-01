import pandas as pd
from Neo4J_KG import clean_text, process_file, extract_nodes

data = pd.read_csv("cif data/csv/CoRE_or_QMOF_properties.csv")


input_file = "data/md/1/1.md"
input_doi = "10.1039/c3ce40346g" #when we scale this - this can be easily found by appending a new column in our .csv with a "document id- that way DOI for each paper is easily found in the same row

# Read md
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Clean the text
text = clean_text(content)


# Find relevant metadatas in dataframe

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
    band_gap = row["Band gap (eV)"]
    
    # Store the MOF and its band gap in the metadata
    metadata["MOFs"][mof_name] = {
        "Band Gap": band_gap
    }


#Pass text and meta data to the proces
#docs = process_file(text, metadatas=metadata)

print(metadata)

