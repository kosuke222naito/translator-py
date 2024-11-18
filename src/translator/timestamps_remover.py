import re
from re import Pattern

TIMESTAMP_PATTERN: Pattern = re.compile(r"^\d{1,2}:\d{2}(:\d{2})?", re.MULTILINE)
EXTRA_NEWLINES_PATTERN: Pattern = re.compile(r"\n\s*\n")


def remove_timestamps_from_str(text: str) -> str:
    cleaned_text: str = TIMESTAMP_PATTERN.sub("", text)
    return EXTRA_NEWLINES_PATTERN.sub("\n", cleaned_text)


def remove_timestamps_from_file(input_filename: str, output_filename: str | None = None) -> None:
    with open(input_filename, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned_content = remove_timestamps_from_str(content)

    if output_filename is None:
        filename, extension = input_filename.split(".")
        output_filename = f"{filename}_timestamps_removed.{extension}"

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(cleaned_content)
