#!/usr/bin/env python3
import os

WHEEL_DIR = "wheelhouse"
INDEX_FILE = "index.html"

def generate_index():
    if not os.path.exists(WHEEL_DIR):
        print(f"Error: '{WHEEL_DIR}' directory not found.")
        return

    # Find and sort all wheel files in the directory
    wheels = sorted(
        [f for f in os.listdir(WHEEL_DIR) if f.endswith(".whl")],
        key=lambda s: s.lower()
    )

    # Generate the complete HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Federate Tyres - Pre-compiled Android Wheels</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 40px auto;
            padding: 0 20px;
            color: #333;
        }}
        h1 {{
            border-bottom: 2px solid #eaecef;
            padding-bottom: 0.3em;
            color: #24292e;
        }}
        p {{
            color: #586069;
        }}
        ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        li {{
            padding: 8px 12px;
            border-bottom: 1px solid #f6f8fa;
        }}
        li:hover {{
            background-color: #f6f8fa;
        }}
        a {{
            color: #0366d6;
            text-decoration: none;
            font-family: "SFMono-Regular", Consolas, monospace;
            font-size: 0.9em;
            word-break: break-all;
        }}
        a:hover {{
            text-decoration: underline;
        }}
    </style>
</head>
<body>
    <h1>Pre-compiled Android/Termux Wheels</h1>
    <p>This page acts as a lookaside wheel repository (wheelhouse) for Federate installations on Android (Termux) using Python 3.13.</p>
    <p><strong>Total wheels hosted: {len(wheels)}</strong></p>
    
    <ul>
"""

    for wheel in wheels:
        html_content += f'        <li><a href="{WHEEL_DIR}/{wheel}">{wheel}</a></li>\n'

    html_content += """    </ul>
</body>
</html>
"""

    # Write the updated index.html
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Success: Updated '{INDEX_FILE}' with {len(wheels)} wheels.")

if __name__ == "__main__":
    generate_index()