from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# dummy data

ISSUES = [
	{
		'id': 1,
		'name': 'Detective Comics #1',
		'issue_number': 1,
		'issue_authors': [],
		'issue_artists': [],
		'vol': 1,
		'story_arches': [],
		'release_date': '1937-3'
	}
]

SERIES = [
	{
		'id': 1,
		'name': 'Detective Comics',
		'run': {
				'start': 1937,
				'end': None
		}
	}
]

VOLUMES = [
	{
		'vol': 1,
		'issues': [],
		'run': {
				'start': 1937,
				'end': None
		}
	}
]

STORY_ARCS = [
	{
		'name': 'I Am Gotham',
		'issues': [],
		'run': {
				'start': 1937,
				'end': None
		}
	}
]

CREATIVES = [
	{
		'name': 'Bill Finger',
		'roles': [
			'author',
			'artist'
		]
	}
]

CHARACTERS = [
	{
		'id': 1,
		'name': {
			'alias': 'Batman',
			'real': 'Bruce Wayne'
		}
	}
]

class Home(Resource):
	def get(self):
		return 'You are reading this from the api service.'

class Issue(Resource):
	def get(self, issue_id):
		return {'hello': 'world' }

#Grab sublist sorted or filtered by attribute
class IssueList(Resource):
	def get(self):
		return ISSUES
	def sort_issue_list(attribute, value):
		#sort by any attribute
		return None
	def filter_issue_list(attribute, *args):
		#filter by as many values for a given attribute
		return None

#Need to grab whole series
#Sort and filter if needed
class Series(Resource):
	def get(self, series_id):
		return {'hello': 'world' }
	def sort_series_(attribute, value):
		#sort by any attribute
		return None
	def filter_series_(attribute, *args):
		#filter by as many values for a given attribute
		return None

#Need to grab series list
#sort and filter based on issue attributes
class SeriesList(Resource):
	def get(self):
		return SERIES
	def sort_series_list(attribute, value):
		#sort by any attribute
		return None
	def filter_series_list(attribute, *args):
		#filter by as many values for a given attribute
		return None

#Might not need this; otherwise treat like Series
class Volume(Resource):
	def get(self, volume_id):
		return {'hello': 'world' }

#Might not need this; otherwise treat like SeriesList
class VolumeList(Resource):
	def get(self):
		return VOLUMES

#Just grab object info
class StoryArc(Resource):
	def get(self, storyarc_id):
		return {'hello': 'world' }

#Might noteed this class, otherwise treat like SeriesList
class StoryArcList(Resource):
	def get(self):
		return STORY_ARCS

#Might not need this class as we only
#filter issues by their name
class Creative(Resource):
	def get(self, creative_id):
		return {'hello': 'world' }

#Need to grab whole list or filtered list
class CreativeList(Resource):
	def get(self):
		return CREATIVES
	def filter_creative_list(attribute, *args):
		#filter by as many values for a given attribute
		return None

#Need to get whole character object
class Character(Resource):
	def get(self, character_id):
		return {'hello': 'world' }

#Grab whole list or filtered list
class CharacterList(Resource):
	def get(self):
		return CHARACTERS
	def filter_character_list(character, *args):
		#filter by the attributes of a given character
		return None

api.add_resource(Home, '/')
api.add_resource(Issue, '/issue/<issue_id>')
api.add_resource(IssueList, '/issue/all')
api.add_resource(Series, '/series/<series_id>')
api.add_resource(SeriesList, '/series/all')
api.add_resource(Volume, '/volume/<volume_id>')
api.add_resource(VolumeList, '/volume/all')
api.add_resource(StoryArc, '/storyarc/<storyarc_id>')
api.add_resource(StoryArcList, '/storyarc/all')
api.add_resource(Creative, '/creative/<creative_id>')
api.add_resource(CreativeList, '/creative/all')
api.add_resource(Character, '/character/<character_id>')
api.add_resource(CharacterList, '/character/all')
