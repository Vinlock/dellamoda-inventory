
class Element:
    tag = ''

    def __init__(self, *args):
        self.content = []
        for arg in args:
            self.content.append(arg)

    def export(self):
        result = []
        for element in self.content:
            result.append(element.export())
        result = " ".join(result)
        if (self.tag is not None):
            return "<"+self.tag+">"+result+"</"+self.tag+">"
        else:
            return result


class Ul(Element):
    tag = 'ul'


class Li(Element):
    tag = 'li'


class Bold(Element):
    tag = 'b'


class String(Element):
    tag = None



class HTML:
    @staticmethod
    def bold(*args):
        return Bold(args)

    @staticmethod
    def ul(*args):
        return Ul(args)

    @staticmethod
    def li(*args):
        return Li(args)