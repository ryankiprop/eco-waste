import click
from lib.db.models import session, WasteEntry, DisposalMethod
from datetime import date

@click.group()
def cli():
    pass

@cli.command()
@click.option('--type', prompt='Waste type')
@click.option('--weight', prompt='Weight (kg)', type=float)
@click.option('--method', prompt='Disposal method')
def log_waste(type, weight, method):
    entry = WasteEntry(
        date=date.today(),
        waste_type=type,
        weight_kg=weight
    )
    disposal = DisposalMethod(method=method, waste_entry=entry)
    session.add_all([entry, disposal])
    session.commit()
    click.echo(f"Logged {weight}kg of {type} ({method})")

@cli.command()
def report():
    total = session.query(WasteEntry).count()
    recycled = session.query(DisposalMethod).filter_by(method="Recycled").count()
    click.echo(f"Total waste: {total} entries")
    click.echo(f"Recycled: {recycled} items")

if __name__ == "__main__":
    cli()