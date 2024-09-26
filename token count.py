import os
import tiktoken  # Assuming you are using tiktoken for tokenization
import seaborn as sns
import matplotlib.pyplot as plt

# Function to calculate number of tokens from a string
def num_tokens_from_string(string: str, model: str = "gpt-4o") -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(model)
    num_tokens = len(encoding.encode(string))
    return num_tokens

# Define base directory where markdown files are located
base_dir = "data/md"

# Lists to store file names and their token counts
file_names = []
token_counts = []

# Loop through all files in the base directory and subdirectories
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".md"):
            # Construct full file path
            file_path = os.path.join(root, file)

            # Open and read the markdown file
            with open(file_path, "r", encoding="utf-8") as f:
                file_content = f.read()

            # Calculate the number of tokens in the file
            num_tokens = num_tokens_from_string(file_content)
            
            # Append file name and token count
            file_names.append(file)
            token_counts.append(num_tokens)

# Create a figure to hold both plots
plt.figure(figsize=(14, 10))

# First plot: Distribution of token counts (Histogram)
plt.subplot(2, 1, 1)
sns.histplot(token_counts, kde=False)
plt.title('Distribution of Token Counts in Markdown Files')
plt.xlabel('Token Count')
plt.ylabel('Frequency')

# Second plot: Token count per file (Bar plot)
plt.subplot(2, 1, 2)
sns.barplot(x=file_names, y=token_counts)
plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
plt.title('Token Count per Markdown File')
plt.xlabel('Markdown Files')
plt.ylabel('Token Count')

# Adjust layout to avoid overlap
plt.tight_layout()

# Show the plots
plt.show()


