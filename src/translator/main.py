import typer

from .timestamps_remover import remove_timestamps_from_file

app = typer.Typer()


@app.command()
def translate(file_path: str):
    """
    Translate a given text file using the OpenAI API.
    """
    typer.echo(f"Translating file: {file_path}")


@app.command()
def remove_timestamps(input_filename: str, output_filename: str | None = None):
    """
    Remove timestamps from a given file and save the result.
    """
    try:
        remove_timestamps_from_file(input_filename, output_filename)
        print("Timestamps removed successfully")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    app()


if __name__ == "__main__":
    main()
