import re

def get_json(response):
    # Retrieve json from response
    pattern = rf"```json\s+(.*?)\s+```"
    json_block = re.search(pattern, response.content, re.DOTALL) # Using re.DOTALL to make the dot match newlines as well
    json_code = None
    if json_block:
        extracted_json = json_block.group(1)
        json_code = extracted_json
    return json_code