import pytest

from translator import remove_timestamps_from_str


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        # 基本ケース
        ("1:00 This is a test.\n", " This is a test.\n"),
        ("12:34 Another test line.\n", " Another test line.\n"),
        # 複数行のケース
        ("1:18 Line one.\n00:45:12 Line two.\n", " Line one.\n Line two.\n"),
        # 空白行の削除
        ("1:00 Line one.\n\n00:45:12 Line two.\n\n", " Line one.\n Line two.\n"),
        # タイムスタンプがない場合
        ("This line has no timestamp.\n", "This line has no timestamp.\n"),
    ],
)
def test_remove_timestamps_from_str(input_text, expected_output):
    assert remove_timestamps_from_str(input_text) == expected_output
