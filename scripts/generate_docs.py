import os
import json
import jsonschema2md

parser = jsonschema2md.Parser()

with open("./schemas/notesdoc.schema.json", "r") as json_file:
    md_lines = parser.parse_schema(json.load(json_file))

with open("./docs/notesdoc.schema.md", "w") as md_file:
    md_file.write(''.join(md_lines))