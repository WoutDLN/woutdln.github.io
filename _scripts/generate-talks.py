
import os
import re

# Paths
input_file = "../_bibliography/talks.bib"
output_dir = "../_talks"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to slugify text
def slugify(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

# Read BibLaTeX file
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# Split entries by '@conference'
entries = [e.strip() for e in content.split('@conference') if e.strip()]

for entry in entries:
    lines = entry.split('\n')
    fields = {}
    for line in lines:
        line = line.strip().strip(',')
        if '=' in line:
            k, v = line.split('=', 1)
            # Remove braces and extra spaces
            val = v.strip().lstrip('{').rstrip('}').strip()
            # Quote values with colons
            if ':' in val:
                val = '"' + val.replace('"', '\\"') + '"'
            fields[k.strip()] = val

    # Rename 'type' to 'category' and slugify its value
    if 'type' in fields:
        fields['category'] = slugify(fields.pop('type'))

    # Determine date for filename
    date = fields.get('date')
    if date:
        date = date.split('/')[0]  # Take first part if range
    else:
        eventdate = fields.get('eventdate', '')
        date = eventdate.split('/')[0] if eventdate else 'unknown-date'

    date = date.replace('{', '').replace('}', '').strip()

    # Slugify title
    title_slug = slugify(fields.get('title', 'untitled'))

    # Filename
    filename = f"{date}-{title_slug}.md"
    filepath = os.path.join(output_dir, filename)

    # Build YAML front matter
    yaml_lines = ["---"]
    yaml_lines.append("layout: page")
    yaml_lines.append("img:")
    for k, v in fields.items():
        yaml_lines.append(f"{k}: {v}")
    yaml_lines.append("---")

    # Write markdown file
    with open(filepath, "w", encoding="utf-8") as md:
        md.write("\n".join(yaml_lines))

print(f"Created {len(entries)} markdown files in {output_dir}.")
