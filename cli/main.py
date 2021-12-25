import click
from click.core import Context
from click.decorators import pass_context, pass_obj
from hang_up_an_autumn_moon_over_the_mountain.oracle.main import Oracle
from hang_up_an_autumn_moon_over_the_mountain.oracle.assets.texts import cards, credit
from simple_term_menu import TerminalMenu


@click.group()
def cli():
    pass

@cli.command()
@click.option('-s', '--sparrow-mode', is_flag=True, help='only sparrow haikus')
def oracle(sparrow_mode):
    o = Oracle(sparrow_mode=sparrow_mode)

    digests = o.create_digests()
    click.echo('\n' + digests)
    
    terminal_menu = TerminalMenu(['1','2','3'])
    menu_entry_index = terminal_menu.show()
    selection = int(menu_entry_index)

    oracle = o.run_oracle(selection)

    response_str = o.format_response(**oracle)

    click.echo(response_str)

@cli.command()
def credits():
    click.echo(Oracle().haiku_credit())

# if __name__ == '__main__':
#     oracle()