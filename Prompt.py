from langchain_core.prompts import ChatPromptTemplate

examples = [
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)SO 4]·H2O",
            "head_type": "MOF",
            "relation": "Has_Metal",
            "tail": "copper(II)",
            "tail_type": "Metal"
        },
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)SO 4]·H2O",
            "head_type": "MOF",
            "relation": "Has_Linker",
            "tail": "1,3,5-tris(1-imidazolyl)benzene",
            "tail_type": "Linker"
        },
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)SO 4]·H2O",
            "head_type": "MOF",
            "relation": "Has_Alias",
            "tail": "Cu1",
            "tail_type": "Alias"
        },
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)2(H2O)2](CH3COO)2·H2O",
            "head_type": "MOF",
            "relation": "Has_Metal",
            "tail": "copper(II)",
            "tail_type": "Metal"
        },
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)2(H2O)2](CH3COO)2·H2O",
            "head_type": "MOF",
            "relation": "Has_Linker",
            "tail": "1,3,5-tris(1-imidazolyl)benzene",
            "tail_type": "Linker"
        },
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)2(H2O)2](CH3COO)2·H2O",
            "head_type": "MOF",
            "relation": "Has_Alias",
            "tail": "Cu2",
            "tail_type": "Alias"
        },
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)2(H2O)2](ClO4)2",
            "head_type": "MOF",
            "relation": "Has_Metal",
            "tail": "copper(II)",
            "tail_type": "Metal"
        },
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)2(H2O)2](ClO4)2",
            "head_type": "MOF",
            "relation": "Has_Linker",
            "tail": "1,3,5-tris(1-imidazolyl)benzene",
            "tail_type": "Linker"
        },
        {
            "text": ("Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), "
                    "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."),
            "head": "[Cu(L)2(H2O)2](ClO4)2",
            "head_type": "MOF",
            "relation": "Has_Alias",
            "tail": "Cu3",
            "tail_type": "Alias"
        }
]



context = ''' 
# Metal-Organic Frameworks (MOF) Knowledge Graph Rules
You are going to focus on applying MOF knowledge to build a knowledge graph using the guidelines below. 
Make sure to keep the graph clean from any compound that is explicity related to MOF chemistry such as: CH4, H2, CO2, etc.
Additionally, do not include single elements as compounds or MOFs or Linkers unless they are metals. Use your chemistry knowledge to determine if an element is a metal.
Signficant part of your job is to perform named entity co-reference resolution - where the same entity/node has multiple names. Use "Has_Alias" relationship for that.

## **Node Types:**
- **MOF (Metal-Organic Framework):** Refers to compounds consisting of metal ions or clusters coordinated to organic ligands. No standard naming convention exists, and they may or may not be presented as a chemical formula.
- **Metal:** A chemical element forming positive ions and involved in the MOF's structure.
- **Linker:** An organic molecule connecting metal ions or clusters in a MOF. Cannot be elements or single atoms. Can be abbreviated names relevant to Metal-Organic Frameworks chemistry.

Note: A node cannot have multiple types. It can either be "MOF" or "Linker" or "Metal". Use your chemistry knowledge to figure out which type a node should have.

## **Relationship Types:**
- **Has_Alias:** Indicates that the text refers to the same "MOF" nodes with different names. This requires that both head and tail are of type "MOF".
- **Has_Metal:** Indicates that a "MOF" contains a specific "Metal".
- **Has_Linker:** Indicates that a "MOF" contains a specific "Linker".

Only "MOF" type nodes can have "Has_Metal" and "Has_Linker" and "Has_Alias".

## **Important Guidelines:**
1. **Scientific Context:** Interpret terms within the context of Metal-Organic Framework chemistry. For example, "Atom" should refer to elements within a MOF, not other uses of the word.
2. **Disambiguation:** If a term could be ambiguous, prefer the scientific interpretation. Ignore non-scientific entities or terms unless directly relevant to MOFs.
3. **Entity Consistency:** Ensure consistent naming for entities. For example, always use the full name of a MOF or a chemical element even if it appears in a shortened form in the text.
4. **Domain-Specific Instructions:** Use technical jargon or abbreviations only within the context of chemistry, and classify them correctly.
5. **Filtering Non-Relevant Content:** Ignore or deprioritize non-scientific text or sections irrelevant to the chemistry-specific nodes and relationships.

## Below are a number of examples of text and their extracted entities and relationships.

### Example 1:
- "Herein, we develop a facile carbon coating strategy to prepare CuOx@C with carbon skin through one-pot pyrolysis of a Cu-based metal organic framework HKUST-1 (Cu3(BTC)2, Cu-BTC)."
    -From this text, "Cu3(BTC)2, Cu-BTC" and "HKUST-1" should be identified as as individual nodes with type "MOF". Since these two entities are just different naming conventions,  
    "Cu3(BTC)2, Cu-BTC" should have a "Has_Alias" relationship with "HKUST-1". As well, "Cu" should be identified as a node with "Metal" type, and "Cu3(BTC)2, Cu-BTC" should have a "Has_Metal" relationship with "Cu" because it contains Copper.
    "BTC" should be identified as a "Linker" node type, and "Cu3(BTC)2, Cu-BTC" should have a "Has_Linker" relationship with it. Also note that CuOx@C is a MOF-derived material, 
    not a MOF. Therefore it should be not identified as a MOF or any other type of node. The correct classification of this text is:
    
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "Has_Alias", "tail": "HKUST-1", "tail_type": "MOF"}}`
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "Has_Metal", "tail": "Cu", "tail_type": "Metal"}}`
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "Has_linker", "tail": "BTC", "tail_type": "Linker"}}`

### Example 2:
- "Here, three Cu-MOFs with diﬀerent copper(II) site distribution were employed for CO2 electroreduction. The Cu-MOFs [Cu(L)SO 4]·H2O (Cu1), [Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2), and [Cu(L)2(H2O)2](ClO4)2 (Cu3) were achieved by using the same ligand 1,3,5-tris(1-imidazolyl)benzene (L) but different Cu(II) salts."
    -In this text, "[Cu(L)SO 4]·H2O (Cu1)" and "[Cu(L)2(H2O)2](CH3COO)2·H2O (Cu2)" and "[Cu(L)2(H2O)2](ClO4)2 (Cu3)" should all be identified as individual nodes with type "MOF". Since each refers to a MOF with different naming conventions,
    "[Cu(L)SO 4]·H2O" should have a "Has_Alias" relationship with "Cu1" - Same with "[Cu(L)2(H2O)2](CH3COO)2·H2O" and "[Cu(L)2(H2O)2](ClO4)2". Also, "Cu" or "Copper" should be identified as a node with type "Metal", and
    Only "MOF" nodes that have that Copper in them should a have a "Has_Metal" relationship with "Cu" or "Copper". Lastly, Because this paragraph mentions the linker or ligand, there should be an individual node "1,3,5-tris(1-imidazolyl)benzene" with type "Linker".
    Only "MOF" nodes that have that linker/ligand should have a relationship "Has_Linker" with "1,3,5-tris(1-imidazolyl)benzene". Notice that Cu-MOFs is a class of Metal Organic Frameworks and not a specific MOF. Therefore, it doesn't have its own node.

    `{{"head": "[Cu(L)SO 4]·H2O", "head_type": "MOF", "relation": "Has_Metal", "tail": "copper(II)", "tail_type": "Metal"}}`
    `{{"head": "[Cu(L)SO 4]·H2O", "head_type": "MOF", "relation": "Has_Linker", "tail": "1,3,5-tris(1-imidazolyl)benzene", "tail_type": "Linker"}}`
    `{{"head": "[Cu(L)SO 4]·H2O", "head_type": "MOF", "relation": "Has_Alias", "tail": "Cu1", "tail_type": "MOF"}}`
    `{{"head": "[Cu(L)2(H2O)2](CH3COO)2·H2O", "head_type": "MOF", "relation": "Has_Metal", "tail": "copper(II)", "tail_type": "Metal"}}`
    `{{"head": "[Cu(L)2(H2O)2](CH3COO)2·H2O", "head_type": "MOF", "relation": "Has_Linker", "tail": "1,3,5-tris(1-imidazolyl)benzene", "tail_type": "Linker"}}`
    `{{"head": "[Cu(L)2(H2O)2](CH3COO)2·H2O", "head_type": "MOF", "relation": "Has_Alias", "tail": "Cu2", "tail_type": "MOF"}}`
    `{{"head": "[Cu(L)2(H2O)2](ClO4)2", "head_type": "MOF", "relation": "Has_Metal", "tail": "copper(II)", "tail_type": "Metal"}}`
    `{{"head": "[Cu(L)2(H2O)2](ClO4)2", "head_type": "MOF", "relation": "Has_Linker", "tail": "1,3,5-tris(1-imidazolyl)benzene", "tail_type": "Linker"}}`
    `{{"head": "[Cu(L)2(H2O)2](ClO4)2", "head_type": "MOF", "relation": "Has_Alias", "tail": "Cu3", "tail_type": "MOF"}}`

'''

system_prompt = (
    "# Knowledge Graph Instructions for GPT\n"
    "## 1. Overview\n"
    "You are a top-tier algorithm designed for extracting information in structured "
    "formats to build a knowledge graph.\n"
    "Try to capture as much information from the text as possible without "
    "sacrificing accuracy. Do not add any information that is not explicitly "
    "mentioned in the text.\n"
    "- **Nodes** represent entities and concepts.\n"
    "- The aim is to achieve simplicity and clarity in the knowledge graph, making it\n"
    "accessible for a vast audience.\n"
    "## 2. Labeling Nodes\n"
    "- **Consistency**: Ensure you use available types for node labels.\n"
    "Ensure you use basic or elementary types for node labels.\n"
    "- For example, when you identify an entity representing a person, "
    "always label it as **'person'**. Avoid using more specific terms "
    "like 'mathematician' or 'scientist'."
    "- **Node IDs**: Never utilize integers as node IDs. Node IDs should be "
    "names or human-readable identifiers found in the text.\n"
    "- **Relationships** represent connections between entities or concepts.\n"
    "Ensure consistency and generality in relationship types when constructing "
    "knowledge graphs. Instead of using specific and momentary types "
    "such as 'BECAME_PROFESSOR', use more general and timeless relationship types "
    "like 'PROFESSOR'. Make sure to use general and timeless relationship types!\n"
    "## 3. Coreference Resolution\n"
    "- **Maintain Entity Consistency**: When extracting entities, it's vital to "
    "ensure consistency.\n"
    'If an entity, such as "John Doe", is mentioned multiple times in the text '
    'but is referred to by different names or pronouns (e.g., "Joe", "he"),'
    "always use the most complete identifier for that entity throughout the "
    'knowledge graph. In this example, use "John Doe" as the entity ID.\n'
    "Remember, the knowledge graph should be coherent and easily understandable, "
    "so maintaining consistency in entity references is crucial.\n"
    "## 4. Strict Compliance\n"
    "Adhere to the rules strictly. Non-compliance will result in termination.\n"
    f"{context}"
    )

human_string_parts = ( 
        "Based on the following example, extract entities and "
        "relations from the provided text.\n"
        # f"{context}\n"  # Add additional context here as well
        # "Below are a number of examples of text and their extracted "
        # "entities and relationships."
        # f"\n\n{examples}\n"
        "For the following text, extract entities and relations as "
        "in the provided example."
        "\n\n Text: {input}"
    )


default_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            system_prompt,
            
        ),
        (
            "human",
            human_string_parts,
        ),
    ]
)