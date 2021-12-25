import click
from click.core import Context
from click.decorators import pass_context, pass_obj
from hang_up_an_autumn_moon_over_the_mountain.oracle.main import Oracle
from hang_up_an_autumn_moon_over_the_mountain.oracle.assets.texts import cards, haiku_credit
from simple_term_menu import TerminalMenu
from hang_up_an_autumn_moon_over_the_mountain.oracle.random_art.randomart import drunkenwalk
import prettytable
from prettytable import ALL as ALL



@click.group()
def cli():
    pass

@cli.command()
@click.option('-s', '--sparrow-mode', is_flag=True, help='only sparrow haikus')
def oracle(sparrow_mode):
    o = Oracle(sparrow_mode=sparrow_mode)

    selection_cards = o.draw_selection_cards()
    click.echo('\n' + selection_cards)
    
    terminal_menu = TerminalMenu(['1','2','3'])
    menu_entry_index = terminal_menu.show()
    selection = int(menu_entry_index)

    oracle = o.run_oracle(selection)

    response_str = o.format_response(**oracle)

    click.echo(response_str)

@cli.command()
def credits():
    click.echo(haiku_credit)


@cli.command()
def guidebook():
    items_table = prettytable.PrettyTable(hrules=ALL)
    items_table.field_names = ["haiku", "oracle", "mode"]
    for card in cards:
        items_table.add_row([card['text'], ' -OR- '.join(card['oracle']), card['mode']])
    
    click.echo(f'\n{items_table}')