"""Console script for tv_pyremote."""
import sys
from typing import Any, Iterable, Optional

import click


@click.command()
def main(args: Optional[Iterable[Any]] = None) -> int:
    """Console script for tv_pyremote.

    Parameters
    ----------
    args : Iterable, optional
        CLI args, by default None

    Returns
    -------
    int
        Exit code
    """
    click.echo("Replace this message by putting your code into " "tv_pyremote.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
