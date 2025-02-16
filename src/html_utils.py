from lxml import etree
from lxml.html.clean import Cleaner
from lxml.html.soupparser import fromstring
import re
import unicodedata


cleaner = Cleaner()

cleaner.scripts = True
cleaner.javascript = True
cleaner.comments = True
cleaner.style = True
cleaner.links = False
cleaner.meta = True
cleaner.page_structure = False
cleaner.processing_instructions = True
cleaner.embedded = True
cleaner.frames = True
cleaner.forms = True
cleaner.annoying_tags = True
cleaner.remove_unknown_tags = False


# cleaner = Cleaner()
# # cleaner.scripts = True
# # cleaner.javascript = True
# # cleaner.comments = True
# cleaner.style = True
# cleaner.links = False
# # cleaner.page_structure = True
# # cleaner.embedded = True
# # cleaner.frames = False
# # cleaner.forms = False
# # cleaner.annoying_tags = False
# # cleaner.remove_unknown_tags = False
# # cleaner.safe_attrs_only = False

def clean_spaces(text):
    return " ".join(re.split(r"\s+", text.strip()))


def clean_format_str(text):
    text = clean_spaces(text)
    text = "".join(ch for ch in text if unicodedata.category(ch)[0] != "C")
    text = "".join([c if ord(c) < 128 else "" for c in text])
    return text


def get_cleaned_body(html):
    html = html.replace("\0", "")  # Delete NULL bytes.
    html = clean_format_str(html)
    etree_root = fromstring(html)
    etree_root = cleaner.clean_html(etree_root)
    dom_tree = etree.ElementTree(etree_root)
    return dom_tree.getroot().body
