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

    readme.write("\n---\n\n## 📖 Notebook Contents\n\n")

    for nb in sorted(notebooks):
        readme.write(f"### {nb}\n\n")
        with open(nb, "r", encoding="utf-8") as f:
            nb_content = nbformat.read(f, as_version=4)
            body, _ = md_exporter.from_notebook_node(nb_content)
            readme.write(body + "\n\n---\n\n")

print("✅ README.md updated successfully!")
