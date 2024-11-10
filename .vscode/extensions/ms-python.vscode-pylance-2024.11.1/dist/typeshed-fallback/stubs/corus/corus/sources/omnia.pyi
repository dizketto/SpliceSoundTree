from _typeshed import Incomplete
from collections.abc import Generator

from corus.record import Record

class OmniaDoc(Record):
    __attributes__: Incomplete
    id: Incomplete
    attrs: Incomplete
    pars: Incomplete
    def __init__(self, id, attrs, pars) -> None: ...

class OmniaPar(Record):
    __attributes__: Incomplete
    sents: Incomplete
    def __init__(self, sents) -> None: ...

class OmniaSent(Record):
    __attributes__: Incomplete
    tokens: Incomplete
    def __init__(self, tokens) -> None: ...

class OmniaToken(Record):
    __attributes__: Incomplete
    text: Incomplete
    lemma: Incomplete
    atag: Incomplete
    tag: Incomplete
    ztag: Incomplete
    g: Incomplete
    def __init__(self, text, lemma, atag, tag, ztag, g) -> None: ...

DID: str
G_TAG: str
S_END: str
P_END: str
DOC_END: str

def take_until(stream, value) -> Generator[Incomplete]: ...
def group_bounds(stream, end) -> Generator[Incomplete]: ...
def group_doc_bounds(stream) -> Generator[Incomplete]: ...
def group_pairs(stream) -> Generator[Incomplete]: ...
def parse_tokens(lines) -> Generator[Incomplete]: ...
def parse_sents(lines) -> Generator[Incomplete]: ...
def parse_pars(lines) -> Generator[Incomplete]: ...
def parse_tag_attrs(tag) -> Generator[Incomplete]: ...
def parse_doc_header(header): ...
def parse_docs(lines) -> Generator[Incomplete]: ...
def load_omnia(path) -> Generator[Incomplete, Incomplete, None]: ...