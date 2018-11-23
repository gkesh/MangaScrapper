class Engine(object):

    version = 1.0

    @classmethod
    def version(cls): return 1.0

    def download(self): raise NotImplementedError

    def crawl(self, links): raise NotImplementedError
