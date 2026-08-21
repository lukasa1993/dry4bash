from pathlib import Path

from dry4bash.core import find_duplicates, tokenize_file


def test_normalizes_identifiers_and_numbers(tmp_path: Path) -> None:
    path = tmp_path / ("sample" + '.sh')
    path.write_text('a() { if [[ "$1" -gt 0 ]]; then echo "$1"; fi; }\n', encoding="utf-8")
    values = [token.value for token in tokenize_file(path)]
    assert "ID" in values
    assert "NUM" in values


def test_finds_duplicate_blocks(tmp_path: Path) -> None:
    (tmp_path / ("a" + '.sh')).write_text('a() { if [[ "$1" -gt 0 ]]; then echo "$1"; fi; }\n', encoding="utf-8")
    (tmp_path / ("b" + '.sh')).write_text('b() { if [[ "$2" -gt 0 ]]; then echo "$2"; fi; }\n', encoding="utf-8")
    duplicates = find_duplicates(tmp_path, min_tokens=8)
    assert duplicates
    assert len(duplicates[0].locations) >= 2
