import os
import nbconvert
import nbformat

repo_title = "My NumPy Learning Notebooks 📚"

# Get all Jupyter Notebook files in the repo
notebooks = [f for f in os.listdir() if f.endswith(".ipynb")]

# Create a new README.md file
with open("README.md", "w", encoding="utf-8") as readme:
    readme.write(f"# {repo_title}\n\n")
    readme.write("These are my NumPy learning notebooks. Below is their content:\n\n")
    
    for nb in notebooks:
        readme.write(f"## {nb}\n\n")
        
        # Load the notebook
        with open(nb, "r", encoding="utf-8") as f:
            notebook = nbformat.read(f, as_version=4)
        
        # Convert notebook to markdown
        exporter = nbconvert.MarkdownExporter()
        body, _ = exporter.from_notebook_node(notebook)
        
        # Write the notebook content into README.md
        readme.write(body + "\n\n")
