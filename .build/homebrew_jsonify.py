import os
import json
import re

def markdown_to_json(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Simple parser for headers and content
    sections = []
    current_section = None
    lines = content.split('\n')
    
    # Get main title from first # header
    title = ""
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
            
    # Split by ## headers
    parts = re.split(r'\n## ', content)
    
    # First part might contain introduction text before any ##
    intro = parts[0].strip()
    if title:
        # Remove the # Title from intro
        intro = re.sub(r'^# .*?\n', '', intro, flags=re.MULTILINE).strip()

    for part in parts[1:]:
        header_match = re.match(r'^(.*?)\n(.*)', part, re.DOTALL)
        if header_match:
            header = header_match.group(1).strip()
            body = header_match.group(2).strip()
            sections.append({
                "section": header,
                "content": body
            })
            
    return {
        "title": title,
        "introduction": intro,
        "sections": sections,
        "filename": os.path.basename(md_path)
    }

def main():
    homebrew_dir = "../homebrew-kit"
    json_dir = "json"
    os.makedirs(json_dir, exist_ok=True)
    
    all_guides = []
    
    if os.path.exists(homebrew_dir):
        for filename in sorted(os.listdir(homebrew_dir)):
            if filename.endswith(".md"):
                md_path = os.path.join(homebrew_dir, filename)
                print(f"Processing guide: {filename}")
                guide_data = markdown_to_json(md_path)
                all_guides.append(guide_data)
                
    output_path = os.path.join(json_dir, "homebrew_kit.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_guides, f, indent=2, ensure_ascii=False)
    print(f"Generated {output_path}")

if __name__ == "__main__":
    main()
