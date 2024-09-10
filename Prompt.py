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
### **Node Types:**
- **MOF (Metal-Organic Framework):** Refers to compounds consisting of metal ions or clusters coordinated to organic ligands. No standard naming convention exists, and they may or may not be presented as a chemical formula.
- **Metal:** A chemical element forming positive ions and involved in the MOF's structure.
- **Linker:** An organic molecule connecting metal ions or clusters in a MOF.

### **Relationship Types:**
- **Has_Bond:** Links an "Atom" to another "Atom" via a bond within a MOF.
- **Has_Atom:** Indicates that a "MOF" contains a specific "Atom".
- **Has_Linker:** Indicates that a "MOF" contains a specific "Linker".

### **Important Guidelines:**
1. **Scientific Context:** Interpret terms within the context of chemistry. For example, "Atom" should refer to elements within a MOF, not other uses of the word.
2. **Disambiguation:** If a term could be ambiguous, prefer the scientific interpretation. Ignore non-scientific entities or terms unless directly relevant to MOFs.
3. **Entity Consistency:** Ensure consistent naming for entities. For example, always use the full name of a MOF or a chemical element even if it appears in a shortened form in the text.
4. **Domain-Specific Instructions:** Use technical jargon or abbreviations only within the context of chemistry, and classify them correctly.
5. **Filtering Non-Relevant Content:** Ignore or deprioritize non-scientific text or sections irrelevant to the chemistry-specific nodes and relationships.

Below are a number of examples of text and their extracted entities and relationships.

Example 1:
- "Herein, we develop a facile carbon coating strategy to prepare CuOx@C with carbon skin through one-pot pyrolysis of a Cu-based metal organic framework HKUST-1 (Cu3(BTC)2, Cu-BTC)."
    -From this text, "Cu3(BTC)2, Cu-BTC" and "HKUST-1" should both be identified as "MOF" node types. Since these two entities are referring to the same MOF under two different naming conventions,  
    HKUST-1 should have a "has_alias" relationship with Cu3(BTC)2, Cu-BTC. As well, "Cu" should be identified as a metal node type, and should have a "has_metal" relationship with 
    Cu3(BTC)2, Cu-BTC. BTC should be identified as a "organic linker" node type, and should have a "has_organic_linker" relationship with Cu3(BTC)2, Cu-BTC. Also note that CuOx@C is a MOF-derived material, 
    not a MOF. Therefore it should be not identified as a MOF or any other type of node. The correct classification of this text is:
    
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "has_metal", "tail": "Cu", "tail_type": "Metal"}}`
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "has_organic_linker", "tail": "BTC", "tail_type": "Organic_Linker"}}`
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "has_alias", "tail": "HKUST-1", "tail_type": "MOF"}}`
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
    "Adhere to the rules strictly. Non-compliance will result in termination."
    )

human_string_parts = ( 
        "Based on the following example, extract entities and "
        "relations from the provided text.\n"
        f"{context}\n"  # Add additional context here as well
        "Below are a number of examples of text and their extracted "
        "entities and relationships."
        #f"\n\n{examples}\n"
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