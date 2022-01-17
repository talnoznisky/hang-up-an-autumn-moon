from select import select
import click
import time
from hang_up_an_autumn_moon_over_the_mountain.oracle.main import Oracle
from hang_up_an_autumn_moon_over_the_mountain.oracle.assets.texts import cards, project_credit, guidebook_text
from simple_term_menu import TerminalMenu
import prettytable
from prettytable import ALL as ALL


@click.group()
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
    
    cli_header = '''
    *   .   *    .  ' .   *   '   *    *  . .   .     
 
 *   H A N G   U P   A N   A U T U M N   M O O N    * 
 
    .    * '   .   .  .  .    *  .   '  *   .  *      
    '''
    click.secho(cli_header, fg='cyan', bold=True)

@cli.command()
@click.pass_context
@click.option('-s', '--sparrow-mode', is_flag=True, help='only sparrow haikus') 
def oracle(ctx, sparrow_mode):   
    '''
    pick a card and recieve your oracle
    ''' 
    # sparrow_mode = ctx.obj['sparrow_mode']
    o = Oracle(sparrow_mode)

    time.sleep(.5)
    click.prompt("Tell us what's on your mind", default='', show_default=False)
    
    time.sleep(.7)
    click.echo('Thanks for sharing.')
    
    time.sleep(.7)
    click.echo('Pick a card:')    
    
    time.sleep(.5)
    spread = o.draw_selection_cards()
    
    spread_table = prettytable.PrettyTable(border=False, header=False)
    spread_table.add_row([spread[0], spread[1], spread[2]])
    spread_table.add_row(["1", "2", "3"])
    
    click.echo(spread_table)

    terminal_menu = TerminalMenu(['1','2','3'])
    menu_entry_index = terminal_menu.show()
    selection = int(menu_entry_index)
    
    click.echo(f'\nYour selection: {selection + 1}')
    
    idx = o.spread[selection]['idx']
    oracle = o.run_oracle(idx)
    
    time.sleep(.5)
    click.echo('\n\nHAIKU:\n\n{haiku}\n\n\nORACLE: {oracle}\n'.format(**oracle))

@cli.command()
def credits():
    """
    see credits for sources used in this project
    """
    click.echo(project_credit)

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
