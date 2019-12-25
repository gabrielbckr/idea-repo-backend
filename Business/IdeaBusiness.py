from Repository import IdeaRepository
from Domain.Idea import *


class IdeaBusiness():
    ideaRepository = IdeaRepository.IdeaRepository()

    def SaveIdea(self, ideaAttrs):
        idea = Idea(ideaAttrs[0], ideaAttrs[1], ideaAttrs[2])
        self.ideaRepository.SaveIdea(idea)
        return "200"

    def GetIdeas(self):
        ideaList = self.ideaRepository.GetIdeas()
        ideaSchema = IdeaSchema(many=True)
        response = ideaSchema.dumps(ideaList)
        return {"items": response}
