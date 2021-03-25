from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# dummy data

ISSUES = [
	{
		'id': 1,
		'name': 'Detective Comics #1',
		'issue_number': 1
	}
]

SERIES = [
	{
		'id': 1,
		'name': 'Detective Comics #1',
	}
]

VOLUMES = [

]

STORY_ARCS = [

]

CREATIVES = [

]

CHARACTERS = [
	{
		'id': 1,
		'name': 'Batman'
		''
	}
]

class Home(Resource):
	def get(self):
		return 'You are reading this from the api service.'

class Issue(Resource):
	def get(self, issue_id):
		return {'hello': 'world' }

class IssueList(Resource):
	def get(self):
		return ISSUES

class Series(Resource):
	def get(self, series_id):
		return {'hello': 'world' }

class SeriesList(Resource):
	def get(self):
		return SERIES

class Volume(Resource):
	def get(self, volume_id):
		return {'hello': 'world' }

class VolumeList(Resource):
	def get(self):
		return VOLUMES

class StoryArc(Resource):
	def get(self, storyarc_id):
		return {'hello': 'world' }

class StoryArcList(Resource):
	def get(self):
		return STORY_ARCS

class Creative(Resource):
	def get(self, creative_id):
		return {'hello': 'world' }

class CreativeList(Resource):
	def get(self):
		return CREATIVES

class Character(Resource):
	def get(self, character_id):
		return {'hello': 'world' }

class CharacterList(Resource):
	def get(self):
		return CHARACTERS

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
