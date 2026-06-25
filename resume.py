import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Load YAML
with open("resume.yaml", "r", encoding="utf-8") as f:
    resume_data = yaml.safe_load(f)

# Configure Jinja2
env = Environment(
    loader=FileSystemLoader("."),
    trim_blocks=True,
    lstrip_blocks=True
)

# Load template
template = env.get_template("resume_template.j2")

# Render template
html = template.render(**resume_data)

# Create output directory
Path("output").mkdir(exist_ok=True)

# Save html
with open("output/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Resume generated successfully!")