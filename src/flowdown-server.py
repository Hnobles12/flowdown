import click
import pathlib

@click.command()
@click.option('--config','-c',type=str, required=True)
def main(config:str):
    config = pathlib.Path(config)
    print(config)
    pass

if __name__ == "__main__":
    main()