from importlib.resources import files
import pytest

from calibre.customize.ui import output_format_plugins
from calibre.ebooks.conversion.cli import main

from . import samples

BASIC_EPUB = files(samples) / 'childrens-literature.epub'

@pytest.mark.parametrize('extension', [p.file_type for p in output_format_plugins()])
def test_epub_to_format(tmp_path, extension):
    retval = main(['ebook-convert', 
                   str(BASIC_EPUB), 
                   str(tmp_path / f'out.{extension}')])
    assert retval == 0
