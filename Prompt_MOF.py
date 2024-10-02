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

Here is some context to help you perform this task, and identify the nodes and relationships:

### **Node Types:**
- **MOF (Metal-Organic Framework):** Refers to compounds consisting of metal ions or clusters coordinated to organic ligands. MOFs are sometimes reffered to as "Coordination Polymers". No standard naming convention exists, and they may or may not be presented as a chemical formula. Only create nodes for specific MOFs named in the paper! If the paper mentions "Zinc MOFs", do not extract this as a node. But if the paper said "[Zn₄O(BDC)₃]", do extract this as a node.
- **Metal:** A metal that is part the MOF structure, this may or may not be indicated in the MOF name. Only identify metals if they are contained within a MOF. Other references to metals within a paper can be ignored.
- **Linker:** An organic molecule connecting metal ions or clusters in a MOF. This may or may not be indicated in the MOF name.
- **Synthesis:** The text may include information regarding how a MOF was synthesized. If this information exists in the text, create a "Synthesis" node type and store the synthesis procedure in the node "description". If the paper does not include synthesis information, do not create a node.

### **Relationship Types:**
- **Has_Alias:** Indicates that two "MOF" type nodes refer to the same MOF, just under a different name. Ex: "MOF-801" may be reffered to as "Complex 1" in a different part of the text. 
- **Has_Metal:** Indicates that a "MOF" contains a specific "Metal". One MOF can have multiple metals
- **Has_Linker:** Indicates that a "MOF" contains a specific "Linker". One MOF can have multiple linkers.
- **Has_Synthesis:** Indicates that the text contains synthesis information about a specific "MOF" node.

### **Important Guidelines:**
1) No standard naming convention exists for MOFs. It is your job to correctly identify MOF node types in the given text. Here are some examples of how MOFs can be named:
    i) Based on institution of research group - Ex: "HKUST-1"
    ii) Based on order of discovery - Ex: "MOF-5"
    iii) Based on chemical formulas - Ex: "[Zr₆O₄(OH)₄(BDC)₆]"

2) It is your job to identify when the author of the text referring to a previously mentioned MOF under different naming convention. Give a "has_alias" relationship to these MOFs if you believe with certaintity that this is the case.
    i) Ex: "HKUST-1", "MOF-199" and "[Cu₃(BTC)₂]ₙ" are the same MOF. Understand the text to make this connection.
    ii) Ex: "[Zr₆O₄(OH)₄(BDC)₆]" and "UiO-66" are the same MOFUnderstand the text to make this connection.
    iii) Sometimes, the author will refer to a MOF named earlier by "Compound 1" or "Compound 2" etc. Ex: The text "The MOF [Cu₃(BTC)₂] 1) was synthesized" implies that "[Cu₃(BTC)₂]" and "Compound 1" are the same MOF
    iv) Do NOT assign a "has_alias" relationship to two "MOFs" just because they both have the word "Compound" or "Complex" in them. Ex: "Complex 1" and "Complex 2" should never have a "has_alias" relationship. "Compound 1" and "Compound 2" should never have a "has_alias" relationship.
    v) NEVER assign a "has_alias" relationship for just one node. Make sure it is two unique nodes

3) Note that not all chemical formulas mentioned in the text are MOFs. Some may be precursors used in the synthesis of the MOF. Use your expert chemistry knowledge to correctly identify when a chemical formula is a MOF. Here are some things to look for in the formula to tell if its a MOF:
    i) Metal ions, typically transition metals like Zinc (Zn), Copper (Cu), Chromium (Cr), Zirconium (Zr), Cobalt (Co), etc.
    ii) Organic molecules, often carboxylates or imidazolates, that act as linkers between metal ions. Sometimes abbrieviated - Ex: Benzene-1,3,5-tricarboxylate (BTC), Fumarate (FUM), 1,4-Benzenediphosphonate (BDP)




Below are a number of examples of text and their extracted entities and relationships.

Example 1:
- "Herein, we develop a facile carbon coating strategy to prepare CuOx@C with carbon skin through one-pot pyrolysis of a Cu-based metal organic framework HKUST-1 (Cu3(BTC)2, Cu-BTC)."
    -From this text, "Cu3(BTC)2, Cu-BTC" and "HKUST-1" should both be identified as "MOF" node types. Since these two entities are referring to the same MOF under two different naming conventions,  
    HKUST-1 should have a "has_alias" relationship with Cu3(BTC)2, Cu-BTC. As well, "Cu" should be identified as a metal node type, and should have a "has_metal" relationship with 
    Cu3(BTC)2, Cu-BTC. BTC should be identified as a "organic linker" node type, and should have a "has_organic_linker" relationship with Cu3(BTC)2, Cu-BTC. Also note that CuOx@C is a MOF-derived material, 
    not a MOF. Therefore it should be not identified as a MOF or any other type of node. The correct classification of this text is:
    
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "has_metal", "tail": "Cu", "tail_type": "Metal"}}`
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "has_linker", "tail": "BTC", "tail_type": "Linker"}}`
    `{{"head": "Cu3(BTC)2, Cu-BTC"", "head_type": "MOF", "relation": "has_alias", "tail": "HKUST-1", "tail_type": "MOF"}}`
'''

system_prompt = (
    "# Knowledge Graph Instructions for GPT\n"
    "## 1. Overview\n"
    "You are a top-tier algorithm with expert chemistry knowledge designed for extracting information in structured "
    "formats to build a knowledge graph.\n"
    "Your particular field of expertise is in Metal-Organic Frameworks (MOFs)"
    "and you have expert ability in reading and understanding scientific literature related to MOFs"
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
        "Your job is to find only ONE specific MOF in this text, and add it to the knowledge graph\n"
        "I am going to present you with some information that can help. The MOF you find should have the same Metals, Chemical Formula, and Space Group"
        "Multiple MOFs may share the same Space Group or Meta, but only create a MOF node type if you are certain it is the same MOF I am looking for."
        "Here is information about the MOF I am looking for:\n"
        "{csd_info}\n"
        f"{context}\n"  
        "Use your expert chemistry knowledge to create a MOF node type for the MOF I am looking for, as well as all its aliases."
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