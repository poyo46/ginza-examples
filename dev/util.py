from typing import List


def table_md(header: List[str], rows: List[List[str]]) -> str:
    head_md = '| ' + ' | '.join(header) + ' |\n'
    hr_md = '| ' + ' | '.join([':--'] * len(header)) + ' |\n'
    body_md = ''
    for row in rows:
        body_md += '| ' + ' | '.join(row) + ' |\n'
    return head_md + hr_md + body_md
