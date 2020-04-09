import click
from GenUsers import GenUsers
from GenGroups import GenGroups
from Utils import cursor, close_connection
from ArtistGenerator import ArtistGenerator
from AlbumGenerator import AlbumGenerator


@click.group()
def cli():
    pass


@click.command()
@click.option('-n', default=10_000, help='The number of records')
def add_users(n):
    gen_users = GenUsers()
    gen_users.get_primary_key_data(n)
    for u in gen_users.data:
        params = gen_users.get_params()
        print(u, params, sep=': ')
        cursor.execute('insert into "user" (email, name, icon_path, password) values(%s, %s, %s, %s);commit;',
                       (u, params.get('name'), params.get('icon_path'), params.get('password')))
    print(n, "Records added", sep=' ')


@click.command()
@click.option('-n', default=10_000, help='The number of records')
def add_groups(n):
    gen_groups = GenGroups()
    gen_groups.get_primary_key_data(n)
    for g in gen_groups.data:
        params = gen_groups.get_params()
        print(g, params, sep=': ')
        cursor.execute('insert into "group"(name, "desc", country, icon_path) values(%s, %s, %s, %s);commit;',
                       (g, params.get('desc'), params.get('country'), params.get('icon_path')))
    print(n, "Records added", sep=' ')


@click.command()
@click.option('-n', default=10_000, help='The number of artists')
def add_artists(n):
    gen_artists = ArtistGenerator()
    gen_artists.get_primary_key_data(n)
    for a in gen_artists.data:
        params = gen_artists.get_params()
        print(a, params, sep=': ')
        cursor.execute(
            'insert into artist (name, "desc", country, icon_path, "group") values (%s, %s, %s, %s, %s);commit;',
            (a, params.get('desc'), params.get('country'), params.get('icon_path'), params.get('group')))
    print(n, "Artists added", sep=' ')


@click.command()
@click.option('-n', default=10_000, help='The number of albums')
def add_albums(n):
    gen_albums = AlbumGenerator()
    data = gen_albums.get_primary_key_data(n)
    for d in data:
        params = gen_albums.get_params()
        print('id: ', d, params, sep=': ')
        cursor.execute(
            'insert into album (id, name, year, duration, quantity, icon_path) values (%s, %s, %s, %s, %s, %s);commit;',
            (d, params.get('name'), params.get('year'), params.get('duration'), params.get('quantity'),
             params.get('icon_path')))
    print(n, "Albums added", sep=' ')


@click.command()
@click.option('-table_name', default="group", help='Delete all records in table')
def del_records(table_name):
    cursor.execute('delete from %s;', (table_name,))
    click.echo("All records in ", table_name, "deleted")


@click.command()
def exitt():
    close_connection()


cli.add_command(del_records)
cli.add_command(add_users)
cli.add_command(add_groups)
cli.add_command(add_artists)
cli.add_command(add_albums)
cli.add_command(del_records)
cli.add_command(exitt)

if __name__ == '__main__':
    cli()
