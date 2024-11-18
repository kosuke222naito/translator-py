import os

import pytest

from translator import remove_timestamps_from_file


@pytest.fixture
def setup_test_files():
    input_filename = "test_input.txt"
    custom_output_filename = "custom_output.txt"

    input_content = "00:01:23\n"
    expected_content = "\n"

    with open(input_filename, "w", encoding="utf-8") as f:
        f.write(input_content)

    yield input_filename, custom_output_filename, expected_content

    if os.path.exists(input_filename):
        os.remove(input_filename)
    if os.path.exists(custom_output_filename):
        os.remove(custom_output_filename)
    default_output_filename = "test_input_timestamps_removed.txt"
    if os.path.exists(default_output_filename):
        os.remove(default_output_filename)


def test_remove_timestamps_with_default_output(setup_test_files):
    input_filename, _, expected_content = setup_test_files

    remove_timestamps_from_file(input_filename)

    output_filename = "test_input_timestamps_removed.txt"
    with open(output_filename, "r", encoding="utf-8") as f:
        actual_content = f.read()

    assert actual_content == expected_content


def test_remove_timestamps_with_custom_output(setup_test_files):
    input_filename, custom_output_filename, expected_content = setup_test_files

    remove_timestamps_from_file(input_filename, custom_output_filename)

    with open(custom_output_filename, "r", encoding="utf-8") as f:
        actual_content = f.read()

    assert actual_content == expected_content
