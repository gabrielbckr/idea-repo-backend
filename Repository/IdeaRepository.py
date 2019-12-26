from typing import List, Any

import pymongo as mongo
from Repository.BaseRepository import *
from Domain.Idea import *


class IdeaRepository(BaseRepository):
    class Meta:
        model = Idea

    def __init__(self):
        super(IdeaRepository, self)
        connection = mongo.MongoClient("mongodb://localhost/")
        self.ideasCollection = connection["idea-repo-db"].get_collection("ideas")
        #TODO: Set database endpoint as environment variable

    def SaveIdea(self, idea):
        data = self.ConvertFromModel(idea)
        self.ideasCollection.insert(data)

    def GetIdeas(self):
        items = self.ideasCollection.find()
        sx: List[Idea] = []
        for x in items:
            sx.append(self.ConverToModel(x))
        return sx
