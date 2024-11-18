import re
from re import Pattern

TIMESTAMP_PATTERN: Pattern = re.compile(r"^\d{1,2}:\d{2}(:\d{2})?")
EXTRA_NEWLINES_PATTERN: Pattern = re.compile(r"\n\s*\n")


def remove_timestamps_from_str(text: str) -> str:
    lines: list[str] = text.splitlines(keepends=True)
    cleaned_lines: list[str] = []
    for line in lines:
        if TIMESTAMP_PATTERN.match(line):
            cleaned_lines.append("\n")
        else:
            cleaned_lines.append(line)
    return "".join(cleaned_lines)


def remove_timestamps_from_file(input_filename: str, output_filename: str | None = None) -> None:
    with open(input_filename, "r", encoding="utf-8") as f:
        content = f.read()

    cleaned_content = remove_timestamps_from_str(content)

    if output_filename is None:
        filename, extension = input_filename.split(".")
        output_filename = f"{filename}_timestamps_removed.{extension}"

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(cleaned_content)
