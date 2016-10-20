
class Element:
    tag = ''

    def __init__(self, *args):
        self.content = []
        for arg in args[0]:
            if not HTML.is_blank(arg):
                self.content.append(arg)

    def add(self, element):
        self.content.append(element)
        return self

    def export(self):
        if self.is_empty():
            return ""
        result = []
        for element in self.content:
            if isinstance(element, Element):
                if not element.is_empty():
                    result.append(element.export())
            else:
                if not HTML.is_blank(element):
                    result.append(element)
        result = " ".join(result)
        if self.tag is not None:
            return "<"+self.tag+">"+result+"</"+self.tag+">"
        return result

    def _remove_blanks(self, alist):
        result = []
        for a in alist:
            if a is not None and a is not "":
                result.append(a)
        return result

    def addIf(self, element, test):
        if test:
            self.add(element)
        return self

    def is_empty(self):
        if self.content[0] is None:
            return True
        return False


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

    @staticmethod
    def str(*args):
        return String(args)

    @staticmethod
    def is_blank(test):
        if test is None:
            return True
        elif test == "":
            return True
        else:
            return False