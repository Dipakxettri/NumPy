
# This is a python script which does following :
# This script will:
# ✔️ Find all .ipynb files
# ✔️ Add their links to README.md
# ✔️ Convert their content to Markdown and append it

import os
import nbformat
from nbconvert import MarkdownExporter

repo_title = "My NumPy Learning Notebooks 📚"

# Initialize MarkdownExporter
md_exporter = MarkdownExporter()
md_exporter.exclude_input_prompt = True  # Remove cell numbers

# Get all .ipynb files
notebooks = []
for root, _, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):
            notebooks.append(os.path.join(root, file).replace("\\", "/"))

# Create README.md with links and content
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write(f"# {repo_title}\n\n")
    readme.write("Click on any notebook to open it in GitHub:\n\n")
    
    for nb in sorted(notebooks):
        readme.write(f"- [{nb}](./{nb})\n")

    # Add instructions for environment setup
    readme.write("## ⚙️ Activating Virtual Environment:\n\n")
    readme.write("Run the following commands to set up and activate the virtual environment:\n\n")
    
    readme.write("```sh\n")  # Start code block
    readme.write("python3 -m venv venv\n")
    readme.write("source venv/bin/activate  # For Linux/macOS\n")
    readme.write("venv\\Scripts\\activate  # For Windows\n")
    readme.write("pip install numpy  # install numpy library \n")
    readme.write("```\n\n")  # End code block

    readme.write("\n---\n\n## 📖 Notebook Contents\n\n")

    

    readme.write("\n---\n\n")

    for nb in sorted(notebooks):
        readme.write(f"### {nb}\n\n")
        with open(nb, "r", encoding="utf-8") as f:
            nb_content = nbformat.read(f, as_version=4)
            body, _ = md_exporter.from_notebook_node(nb_content)
            readme.write(body + "\n\n---\n\n")

print("✅ README.md updated successfully!")
