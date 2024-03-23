from pathlib import Path
import json
import jsonschema2md
from jsonschema import Draft202012Validator

parser = jsonschema2md.Parser()

schema_path = Path('schemas/')
docs_path = Path('docs/')

def gen_docs_for_schema(input_file) -> str:
    schema_name = input_file.name.split('.')[0] + '.md'
    with open(input_file, "r") as json_file:
        md_lines = parser.parse_schema(json.load(json_file))

    schema_file = docs_path / schema_name
    with open(schema_file, "w") as md_file:
        md_file.write(''.join(md_lines))

    return schema_file

def gen_all_schemas() -> list:
    schemas = []
    for file in schema_path.iterdir():
        print(f'Loading Schema from {file}')
        schema = json.loads(file.read_text())
        title = schema['title']

        print(f'Validating Schema for {title}')
        Draft202012Validator.check_schema(schema)

        print(f'Generating Markdown File for Schema {title}')
        file_name = gen_docs_for_schema(file)
        schemas.append({'title': title, 'file_name': file_name})

        print('')

    return schemas

def gen_schemas_overview(schemas : dict):
    overview_path = docs_path / 'overview.md'
    overview_md = '# Espresso Notes Schemas\n\n'

    for schema in schemas:
        overview_md += f"- [{schema['title']}]({schema['file_name']})\n"

    overview_path.write_text(overview_md)


if __name__ == '__main__':
    schemas = gen_all_schemas()
    gen_schemas_overview(schemas)