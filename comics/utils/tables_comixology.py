from peewee import IntegrityError

from comics.models.comixology import ComixologyCreator, ComixologyGenre, ComixologyIssue, ComixologyIssueCreatorJunction, ComixologyIssueGenreJunction, ComixologyPublisher, ComixologyRefAgeRating, ComixologyRefCreatorRole, ComixologyRefSoldBy, ComixologySeries, ComixologyStoryArc, ComixologyVolume
from comics.config import db


# def create_ref_tables(db):
#     '''Initialize the reference tables'''
#     with db.atomic() as transaction:
#         try:
#             ComixologyRefCreatorRole.create(role_name="writer")
#             ComixologyRefCreatorRole.create(role_name="inker")
#             ComixologyRefCreatorRole.create(role_name="pencils")
#             ComixologyRefCreatorRole.create(role_name="colors")
#             ComixologyRefCreatorRole.create(role_name="artist")
#         except IntegrityError as e:
#             transaction.rollback()
#             print(e)
#
#     ComixologyCreator.create(name="Various", description='Various is a special "person" on Comixology that represents multiple writers, artists, etc.", name="Various', url='https://www.comixology.com/Various/comics-creator/1368')



# def create_tables():
#     models = [
#         RefCreatorRole,
#         Creator,
#     ]
#
#     db.create_tables(models)
#
#     create_ref_tables(db)

def comixology_setup():
    print("Setting up Comixology tables...")
    comixology_create_tables(db)
    comixology_insert_ref_data(db)
    print("Setup complete.")

def comixology_create_tables(db):
    models = [
        ComixologyRefCreatorRole,
        ComixologyRefSoldBy,
        ComixologyRefAgeRating,
        ComixologyCreator,
        ComixologyPublisher,
        ComixologyVolume,
        ComixologySeries,
        ComixologyStoryArc,
        ComixologyIssue,
        ComixologyIssueCreatorJunction,
        ComixologyGenre,
        ComixologyIssueGenreJunction,
    ]

    db.create_tables(models)


def comixology_insert_ref_data(db):
    '''Initialize the reference tables'''
    with db.atomic() as transaction:
        try:
            ComixologyRefCreatorRole.create(role_name="writer")
            ComixologyRefCreatorRole.create(role_name="inks")
            ComixologyRefCreatorRole.create(role_name="pencils")
            ComixologyRefCreatorRole.create(role_name="colors")
            ComixologyRefCreatorRole.create(role_name="artist")
        except IntegrityError as e:
            transaction.rollback()
            print(e)

    ComixologyCreator.create(name="Various", description='Various is a special "person" on Comixology that represents multiple writers, artists, etc.", name="Various', url='https://www.comixology.com/Various/comics-creator/1368')
