import pytest

from translator import remove_timestamps_from_str


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("1:00\nThis is a test.\n", "\nThis is a test.\n"),
        ("Intro\n1:00\nTest line.\n", "Intro\n\nTest line.\n"),
    ],
)
def test_remove_timestamps_from_str(input_text, expected_output):
    assert remove_timestamps_from_str(input_text) == expected_output
