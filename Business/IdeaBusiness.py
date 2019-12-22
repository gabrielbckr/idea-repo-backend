from Repository import IdeaRepository
import json
from Domain.Idea import *


class IdeaBusiness():
    ideaRepository = IdeaRepository.IdeaRepository()

    def SaveIdea(self, ideaAttrs):
        idea = Idea(ideaAttrs[0], ideaAttrs[1], ideaAttrs[2])
        self.ideaRepository.SaveIdea(idea)
        return "200"

    def GetIdeas(self):
        ownList = self.ideaRepository.GetIdeas()
        response = json.dumps(ownList)
        return response
