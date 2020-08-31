from pathlib import Path
from examples.displacy import save_as_image, TEXT


def test_save_as_image():
    file_path = Path(__file__).parent / 'displacy.svg'
    assert not file_path.exists()
    save_as_image(TEXT, file_path)
    assert file_path.exists()
    file_path.unlink()
    assert not file_path.exists()
