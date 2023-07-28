# xml - way how to hierarchically structure our data,
# it is platform and application independent

# two modules:
# SAX - simple module
# DOM - object oriented module

# starting with sax
import xml.sax
import xml.sax.handler

# need 2 things:
# handler - handles the xml file, works with the file
# parser - parser, parses the data
# handler = xml.sax.handler.ContentHandler() - we could do it basically like that
# but we want our own handler so we gonna create our own
# and then override and inherit from ContentHandler()

class GroupHandler(xml.sax.handler.ContentHandler):
    # this function is first function that gets called when our handler processes an element
    def startElement(self, name, attrs):
        # name = tag name
        self.current = name
        if self.current == "person":
            print("---PERSON---")
            print("id: {}".format(attrs['id']))

    # gets elements one by one (like <name> <age>...)
    def characters(self, content):
        if self.current == "name":
            self.name = content
        if self.current == "age":
            self.age = content
        if self.current == "weight":
            self.weight = content
        if self.current == "height":
            self.height = content

    def endElement(self, name):
        if self.current == "name":
            print("Name: {}".format(self.name))
        if self.current == "age":
            print("Age: {}".format(self.age))
        if self.current == "weight":
            print("Weight: {}".format(self.weight))
        if self.current == "height":
            print("Height: {}".format(self.height))


handler = GroupHandler()

parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')



