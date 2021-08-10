class Tag(object):

    def __init__(self, name, content):
        self.start_tag = "<{}>".format(name)        # attributes of the class Tag
        self.end_tag = "</{}>".format(name)
        self.content = content

    def __str__(self):
        return "{0.start_tag} {0.content} {0.end_tag}".format(self)

    def display(self, file=None):
        print(self, file=file)


class DocType(Tag):

    def __init__(self):
        super().__init__('!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" http://www.w3.org/TR/html4/strict.dtd', '')
        self.end_tag = ''  # DOCTYPE doesnt have and end tag


class Head(Tag):

    def __init__(self, title=None):
        super().__init__('head', '')
        if title:
            self._title_tag = Tag('title', title)
            self.contents = str(self._title_tag)


class Body(Tag):

    def __init__(self):
        super().__init__('body', '')  # body contents will be built up separately
        self._body_contents = []

    def add_tag(self, name, content):
        new_tag = Tag(name, content)
        self._body_contents.append(new_tag)

    def display(self, file=None):
        for tag in self._body_contents:
            self.content += str(tag)

        super().display(file=file)

# COMPOSITION
# class HtmlDoc(object):
#
#     def __init__(self, title=None):
#         self._doc_type = DocType()
#         self._head = Head(title)
#         self._body = Body()
#
#     def add_tag(self, name, content):
#         self._body.add_tag(name, content)
#
#     def display(self, file=None):
#         self._doc_type.display(file=file)
#         print('<html>', file=file)
#         self._head.display(file=file)
#         self._body.display(file=file)
#         print('</html>', file=file)

# AGGREGATION ( we defined separately doctype, head and body classes that they can exist without my_page
class HtmlDoc(object):

    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, name, content):
        self._body.add_tag(name, content)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


if __name__ == '__main__':
    # COMPOSITION
    # my_page = HtmlDoc('Demo doc')
    # my_page.add_tag('h1', 'Main heading')
    # my_page.add_tag('h2', 'sub-heading')
    # my_page.add_tag('p', 'This is a paragraph that will appear on the page')
    # with open('test.html', 'w') as test_doc:
    #     my_page.display(file=test_doc)

    # AGGREGATION
    new_body = Body()
    new_body.add_tag('h1', 'Aggregation')
    new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                     "of objects to build up another object.")
    new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of"
                     " - if it is destroyed, those objects continue to exist.")

    new_docType = DocType()
    new_header = Head('Aggregation document')
    my_page = HtmlDoc(new_docType, new_header, new_body)

    with open('test3.html', 'w') as test_doc:
        my_page.display(file=test_doc)

# COMPOSITION
# # give our document content by switching it's body
# my_page._body = new_body
# with open('test2.html', 'w') as test_doc:
#     my_page.display(file=test_doc)
