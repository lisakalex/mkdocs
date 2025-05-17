#!/home/al/.venv/bin/python3


import argparse
import sys


def fill_template(template_path, filename, variables):
    template = ''
    filename = filename.lower().replace(' ', '-')
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()
    except FileNotFoundError:
        print(f"Error: Template file '{template_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading template file: {e}")
        sys.exit(1)

    for key, value in variables.items():
        placeholder = f"{{{{ {key} }}}}"
        template = template.replace(placeholder, value)

    try:
        with open('docs/' + filename + '.md', 'w', encoding='utf-8') as f:
            f.write(template)
    except Exception as e:
        print(f"Error writing to output file: {e}")
        sys.exit(1)

    print(f"Markdown file '{filename}.md generated from template '{template_path}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a Markdown file from a template.")

    parser.add_argument('--template', default='template.md', help='Path to the input template file')
    # parser.add_argument('--output', default='report.md', help='Path to the output markdown file')
    parser.add_argument('--filename', default='untitled-report', help='Title of the report and file name')
    parser.add_argument('--title', default='', help='')
    parser.add_argument('--author', default='', help='')
    parser.add_argument('--date', default='', help='')
    parser.add_argument('--summary', default='', help='')
    parser.add_argument('--notes', default='', help='')

    args = parser.parse_args()

    variables_to_fill = {
        'title': args.title,
        'author': args.author,
        'date': args.date,
        'summary': args.summary,
        'notes': args.notes
    }

    fill_template(args.template, args.filename, variables_to_fill)
