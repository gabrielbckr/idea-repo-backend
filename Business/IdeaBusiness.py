from Repository import IdeaRepository
from Domain.Idea import *


class IdeaBusiness():
    ideaRepository = IdeaRepository.IdeaRepository()

    def SaveIdea(self, title, contact, description, wholeIdea):
        idea = Idea(title, contact, description, wholeIdea)
        self.ideaRepository.SaveIdea(idea)
        return "200"

    def GetIdeas(self):
        ideaList = self.ideaRepository.GetIdeas()
        ideaSchema = IdeaSchema(many=True)
        response = ideaSchema.dumps(ideaList)
        return  response
