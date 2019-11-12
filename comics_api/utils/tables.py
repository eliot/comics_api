from peewee import IntegrityError

from ..models.base import RefCreatorRole, Creator
from ..models.comixology import ComixologyCreator, ComixologyGenre, ComixologyIssue, ComixologyIssueCreatorJunction, ComixologyIssueGenreJunction, ComixologyPublisher, ComixologyRefAgeRating, ComixologyRefCreatorRole, ComixologyRefSoldBy, ComixologySeries, ComixologyStoryArc, ComixologyVolume
from ..config import db, db_comixology


def create_ref_tables():
    '''Initialize the reference tables'''
    with db.atomic() as transaction:
        try:
            RefCreatorRole.create(role_name="writer")
            RefCreatorRole.create(role_name="inker")
            RefCreatorRole.create(role_name="pencils")
            RefCreatorRole.create(role_name="colors")
            RefCreatorRole.create(role_name="artist")
        except IntegrityError as e:
            transaction.rollback()
            print(e)

    Creator.create(title="Various", description='Various is a special "person" on Comixology that represents multiple writers, artists, etc.", name="Various', url='https://www.comixology.com/Various/comics-creator/1368')
            


def create_tables():
    models = [
        RefCreatorRole,
        Creator,
    ]

    db.create_tables(models)
    
    create_ref_tables(db)

def comixology_setup():
	comixology_create_tables()
	comixology_insert_ref_data()

def comixology_create_tables():
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
    
    db_comixology.create_tables(models)


def comixology_insert_ref_data():
    '''Initialize the reference tables'''
    with db_comixology.atomic() as transaction:
        try:
            ComixologyRefCreatorRole.create(role_name="writer")
            ComixologyRefCreatorRole.create(role_name="inker")
            ComixologyRefCreatorRole.create(role_name="pencils")
            ComixologyRefCreatorRole.create(role_name="colors")
            ComixologyRefCreatorRole.create(role_name="artist")
        except IntegrityError as e:
            transaction.rollback()
            print(e)
            
    ComixologyCreator.create(title="Various", description='Various is a special "person" on Comixology that represents multiple writers, artists, etc.", name="Various', url='https://www.comixology.com/Various/comics-creator/1368')

