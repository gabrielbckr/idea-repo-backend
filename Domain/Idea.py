from marshmallow import Schema, fields


class Idea():
    def __init__(self, title="", contact="", description="", wholeIdea=""):
        self.title = title
        self.description = description
        self.wholeIdea = wholeIdea
        self.contact = contact


class IdeaSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    wholeIdea = fields.Str()
    contact = fields.Str()