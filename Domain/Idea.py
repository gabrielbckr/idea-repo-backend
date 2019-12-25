from marshmallow import Schema, fields


class Idea():
    def __init__(self, title="", description="", wholeIdea=""):
        self.title = title
        self.description = description
        self.wholeIdea = wholeIdea


class IdeaSchema(Schema):
    title = fields.Str()
    description = fields.Str()
    wholeIdea = fields.Str()