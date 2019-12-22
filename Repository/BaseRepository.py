class BaseRepository(object):
    def ConvertFromModel(self, obj):
        return obj.__dict__

    def ConverToModel(self, dict):
        modelClass = self.Meta.model()
        modelClass.__dict__.update(dict)
        return modelClass