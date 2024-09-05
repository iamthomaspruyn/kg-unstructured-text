from langchain_core.prompts import ChatPromptTemplate

examples = [
    {
        "text": (
            "Adam is a software engineer in Microsoft since 2009, "
            "and last year he got an award as the Best Talent"
        ),
        "head": "Adam",
        "head_type": "Person",
        "relation": "WORKS_FOR",
        "tail": "Microsoft",
        "tail_type": "Company",
    },
    {
        "text": (
            "Adam is a software engineer in Microsoft since 2009, "
            "and last year he got an award as the Best Talent"
        ),
        "head": "Adam",
        "head_type": "Person",
        "relation": "HAS_AWARD",
        "tail": "Best Talent",
        "tail_type": "Award",
    },
    {
        "text": (
            "Microsoft is a tech company that provide "
            "several products such as Microsoft Word"
        ),
        "head": "Microsoft Word",
        "head_type": "Product",
        "relation": "PRODUCED_BY",
        "tail": "Microsoft",
        "tail_type": "Company",
    },
    {
        "text": "Microsoft Word is a lightweight app that accessible offline",
        "head": "Microsoft Word",
        "head_type": "Product",
        "relation": "HAS_CHARACTERISTIC",
        "tail": "lightweight app",
        "tail_type": "Characteristic",
    },
    {
        "text": "Microsoft Word is a lightweight app that accessible offline",
        "head": "Microsoft Word",
        "head_type": "Product",
        "relation": "HAS_CHARACTERISTIC",
        "tail": "accessible offline",
        "tail_type": "Characteristic",
    },
]

context = ''' 
### **Node Types:**
- **MOF (Metal-Organic Framework):** Refers to compounds consisting of metal ions or clusters coordinated to organic ligands.
- **Bond:** Represents a connection between two atoms within a MOF.
- **Atom:** The basic unit of a chemical element in a MOF.
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
6. **Known Misinterpretations:** Do not classify journal names, like "Dalton Transactions," as a scientific entity like "MOF."

### **Examples of Correct Classifications:**
- "The MOF Zn-BTC has a bond between Zinc (Metal) and Benzene Tricarboxylate (Linker)."
  - `{{"head": "Zn-BTC", "head_type": "MOF", "relation": "Has_Bond", "tail": "Zinc", "tail_type": "Metal"}}`
  - `{{"head": "Zn-BTC", "head_type": "MOF", "relation": "Has_Linker", "tail": "Benzene Tricarboxylate", "tail_type": "Linker"}}`

### **Incorrect Classifications to Avoid:**
- "Dalton Transactions is a journal related to MOFs."
  - **Incorrect:** `{{}"head": "Dalton Transactions", "head_type": "MOF", "relation": "Has_Linker", "tail": "MOFs", "tail_type": "Linker"}` 
  - **Correct Approach:** Do not classify "Dalton Transactions" as a "MOF" or any other node type.
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
    #    f"{examples}\n"
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