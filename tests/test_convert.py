from importlib.resources import files

from calibre.ebooks.conversion.cli import main

from . import samples

BASIC_EPUB = files(samples) / 'childrens-literature.epub'

def test_epub_to_epub(tmp_path):
    retval = main(['ebook-convert', 
                   str(BASIC_EPUB), 
                   str(tmp_path / 'out.epub')])
    assert retval == 0