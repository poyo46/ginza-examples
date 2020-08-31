from typing import Optional, List
import inspect


def table_md(header: List[str], rows: List[List[str]]) -> str:
    head_md = '| ' + ' | '.join(header) + ' |\n'
    hr_md = '| ' + ' | '.join([':--'] * len(header)) + ' |\n'
    body_md = ''
    for row in rows:
        body_md += '| ' + ' | '.join(row) + ' |\n'
    return head_md + hr_md + body_md


def get_function_source(f):
    try:
        lines_to_skip = len(f.__doc__.split('\n'))
    except AttributeError:
        lines_to_skip = 0

    all_lines = inspect.getsourcelines(f)[0]
    body_lines = all_lines[lines_to_skip + 1:]
    lines = []
    for line in body_lines:
        if 'return ' in line:
            continue
        if line.startswith('    '):
            lines.append(line[4:])
        else:
            lines.append(line)
    return ''.join(lines).strip('\n')


def basic_src(f: object, text: str,
              imports: Optional[List[str]] = None) -> str:
    if imports is None:
        imports = []
    imports.insert(0, 'import spacy')
    import_block = '\n'.join(imports) + '\n'
    blocks = [
        import_block,
        "nlp = spacy.load('ja_ginza')\n",
        get_function_source(f).replace('nlp(text)', f"nlp('{text}')")
    ]
    return '\n'.join(blocks) + '\n\n'


if __name__ == '__main__':
    from examples.token_information import tokenize, TEXT

    print(basic_src(tokenize, TEXT, ['import ginza']))
