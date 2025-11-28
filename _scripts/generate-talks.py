
import os
import re
import unicodedata

# Paths
input_file = "../_bibliography/talks.bib"
output_dir = "../_talks"

# ! Running this script overwrites elete all .md files in ../_talks
target_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "../_talks"))
removed = 0
if os.path.isdir(target_dir):
    for fname in os.listdir(target_dir):
        if fname.lower().endswith(".md"):
            try:
                os.remove(os.path.join(target_dir, fname))
                removed += 1
            except OSError:
                pass
print(f"Removed {removed} .md files from {target_dir}")

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

    # Determine date for filename, YYYY-MM format
    date = fields.get('date')
    if date:
        date = date.strip()[:7] 
    else:
        eventdate = fields.get('eventdate', '')
        date = eventdate.strip()[:7] if eventdate else 'unknown-date'

    date = date.replace('{', '').replace('}', '').strip()

    # determine city for filename
    city = fields.get('location')
    city = unicodedata.normalize('NFKD', city).encode('ascii', 'ignore').decode('ascii') # decode diacritics
    city = city.split(',')[0] # remove country
    city_slug = slugify(city) 

    # determine short title for filename
    title_short = fields.get('title', 'untitled')
    # take the first word from the title and create a slug
    words = title_short.strip().split()
    if not words:
        first_word = 'untitled'
    else:
        first_word = words[0]
        # skip leading articles
        if first_word.lower() in ('the', 'a') and len(words) > 1:
            first_word = words[1]
    first_word = unicodedata.normalize('NFKD', first_word).encode('ascii', 'ignore').decode('ascii')
    first_word_slug = slugify(first_word)

    # Filename
    filename = f"{date}_{city_slug}_{first_word_slug}.md"
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
