class Visitor:
    def __str__(self):
        return self.__class__.__name__

class Visitable:
    def accept(self, visitor:Visitor):
        visitor.visit(self)
        return self