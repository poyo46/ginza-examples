import subprocess
from examples.similarity import (
    similarity_matrix, EXAMPLE_TEXTS, EXAMPLE_SCRIPT
)


def test_similarity_matrix():
    rows = similarity_matrix(EXAMPLE_TEXTS)
    n = len(rows)
    for i in range(n):
        assert rows[i][i] == 1.0
        for j in range(i):
            assert rows[i][j] == rows[j][i]


def test_script():
    return_code = subprocess.call(EXAMPLE_SCRIPT.split(' '))
    assert return_code == 0
