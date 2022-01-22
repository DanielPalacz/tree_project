import click
from tree import run


# setuptools ---> żeby poziomu z widzieć paczkę z poziomu pipa ( wypchać na zewnątrz do pipa )

class Config:
    """Configuration class will be used across click module context for handling configuration details"""
    def __init__(self):
        self.version = "0.1"


pass_config = click.make_pass_decorator(Config, ensure=True)


@click.command()
@click.argument("dirname", type=str, default=".", required=False)
@pass_config
def cli(config, dirname):
    """tree-like python3 implementation

    python app.py DIRNAME (Optional)

    DIRNAME directory-input for printing tree representation of directories

    """
    config.dirname = dirname
    print("\n", config.dirname, "\n", sep="")
    input()
    run(config.dirname)


if __name__ == "__main__":
    cli()
