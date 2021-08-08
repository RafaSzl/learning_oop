class Tag(object):

    def __init__(self, name, content):
        self.start_tag = "<{}>".format(name)        # attributes of the class Tag
        self.end_tag = "</{}>".format(name)
        self.content = content

    def __str__(self):
        return "{0.start_tag} {0.content} {0.end_tag}".format(self)

    def display(self):
        print(self)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DOCTYPE doesnt have and end tag


class Head(Tag):

    def __init__(self):
        super().__init__('head', '')


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')  # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, content):
        new_tag = Tag(name, content)
        self._body_contents.append(new_tag)

    def display(self):
        for tag in self._body_contents:
            self.content += str(tag)

        super().display()


