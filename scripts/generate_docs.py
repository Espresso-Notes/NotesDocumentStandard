from pathlib import Path
import json
import jsonschema2md
from jsonschema import Draft202012Validator

parser = jsonschema2md.Parser()

schema_path = Path('schemas/')
docs_path = Path('docs/')

def gen_docs_for_schema(input_file):
    schema_name = file.name.split('.')[0] + '.md'
    with open(input_file, "r") as json_file:
        md_lines = parser.parse_schema(json.load(json_file))

    with open(docs_path / schema_name, "w") as md_file:
        md_file.write(''.join(md_lines))

if __name__ == '__main__':
    for file in schema_path.iterdir():
        schema = json.loads(file.read_text())
        Draft202012Validator.check_schema(schema)
        gen_docs_for_schema(file)
