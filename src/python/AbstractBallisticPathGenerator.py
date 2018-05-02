from abc import ABCMeta, abstractmethod

class AbstractBallisticPathGenerator(object):

    __metaclass__ = ABCMeta

    def __init__(self, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def generate(self):
        raise NotImplementedError
