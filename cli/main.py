import click
from hang_up_an_autumn_moon_over_the_mountain.oracle.main import Oracle
from hang_up_an_autumn_moon_over_the_mountain.oracle.assets.texts import cards, haiku_credit, guidebook_text
from simple_term_menu import TerminalMenu
import prettytable
from prettytable import ALL as ALL


@click.group()
@click.option('-s', '--sparrow-mode', is_flag=True, help='only sparrow haikus')
@click.pass_context
def cli(ctx, sparrow_mode=False):
    '''
    I almost forgot\\To hang up an autumn moon\\Over the mountain.\n
        - Richard Wright

    hang-up-an-autumn moon is an oracular CLI based on the late haiku of Richard Wright

    To receive a spread of cards pseudo-randomly generated from the haiku run:
    `hang-up-an-autumn-moon oracle` and select a card to recieve your oracle.
    To limit the oracle to haiku about sparrows, use the sparrow-mode flag:
        `hang-up-an-autumn-moon --sparrow-mode oracle`
    '''
    ctx.ensure_object(dict)
    ctx.obj['sparrow_mode'] = sparrow_mode

@cli.command()
@click.pass_context
def oracle(ctx):   
    '''
    pick a card and recieve your oracle
    ''' 
    sparrow_mode = ctx.obj['sparrow_mode']
    o = Oracle(sparrow_mode)

    selection_cards = o.draw_selection_cards()
    click.echo('\n' + selection_cards)

    if sparrow_mode:
        click.echo(f'\nsparrow_mode is {"ON" if sparrow_mode else "OFF"}')    
    
    terminal_menu = TerminalMenu(['1','2','3'])
    menu_entry_index = terminal_menu.show()
    selection = int(menu_entry_index)

    oracle = o.run_oracle(selection)

    response_str = o.format_response(**oracle)

    click.echo(response_str)

@cli.command()
def credits():
    """
    read credits to Richard Wright's haiku
    """
    click.echo(haiku_credit)

@cli.command()
def guidebook():
    """
    read the guidebook to the oracle
    """
    click.echo(guidebook_text)
    
    guidebook = prettytable.PrettyTable(hrules=ALL)
    guidebook.field_names = ["haiku", "oracle", "mode"]
    for card in cards:
        guidebook.add_row([card['text'], ' - OR - '.join(card['oracle']), card['mode']])
    click.echo(f'\n{guidebook}')