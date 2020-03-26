class view:
    def __init__(self):
        self.name = ''
        self.season = None
        self.episode = None
        self.lang = ''

    def __init__(self,name,lang,season = None ,episode = None):
        self.name = name
        self.lang = lang
        self.season = season
        self.episode = episode

    def genJSONtype(self):
        x = {'lang' : self.lang,'movieName' : self.name}
        if self.season is not None:
            x['season'] = self.season
        if self.episode is not None:
            x['episode'] = self.episode
        return x
