from garbage import Garbage
from paper_garbage import PaperGarbage
from plastic_garbage import PlasticGarbage
from dustbin_content_error import DustbinContentError


class Dustbin:
    def __init__(self, color):
        self.color = color
        self.paper_content = []
        self.plastic_content = []
        self.house_waste_content = []

    def throw_out_garbage(self, garbage):
        if isinstance(garbage, PlasticGarbage):
            pass
        elif isinstance(garbage, PlasticGarbage):
            pass
        elif isinstance(garbage, PlasticGarbage):
            pass
        else:
            pass

    def empty_contents(self):
        pass
