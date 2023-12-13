import sys, os

def get_variables(filename: str) -> dict:
    variables = {}
    with open(filename) as file:
        content = file.read()
        if content:
            exec(content, variables)
    return variables

def get_formatted_template_content(template_filename: str, variables: dict) -> str:
    with open(template_filename, 'r') as file:
        content = file.read()
        return content.format(**variables)

def write_html(content: str, basename: str):
    with open(basename + ".html", 'w') as file:
        file.write(content)

def run(template_filename: str, settings_filename: str):
    if os.path.exists(template_filename) and os.path.exists(settings_filename):
        basename, extension = os.path.splitext(template_filename)
        if extension == ".template":
            variables = get_variables(settings_filename)
            if len(variables):
                formatted_content = get_formatted_template_content(template_filename, variables)
                write_html(formatted_content, basename)
        else:
            print("Template filename must have .template extension")
    else:
        print("File not found")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        run(sys.argv[1], 'settings.py')
    else:
        print("Usage: python render.py <template_filename>")