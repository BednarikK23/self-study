import xml.dom.minidom

# when working with dom we re working basically w dom tree
# they wiew xml file as a tree and every element is like an object/node in that tree

domtree = xml.dom.minidom.parse("data.xml")
group = domtree.documentElement

persons = group.getElementsByTagName('person')

for person in persons:
    print("---PERSON---")
    if person.hasAttribute('id'):
        print("ID: {}".format(person.getAttribute('id')))

    # from getElemByName we get list of objects even if there is only one so we have to pick our one object from this list -> [0]
    # but this was just the element we want get the value of this element so we use .childnodes() - again list so pick first -> [0]
    # then again we dont want the object but we want its data so we have to say .data at the end
    print("Name: {}".format(person.getElementsByTagName('name')[0].childNodes[0].data))
    print("Age: {}".format(person.getElementsByTagName('age')[0].childNodes[0].data))
    print("Weight: {}".format(person.getElementsByTagName('weight')[0].childNodes[0].data))
    print("Height: {}".format(person.getElementsByTagName('height')[0].childNodes[0].data))

# how to change?
# we take for example 3rd person and change something ike this:
# watch out we using nodeValue here
persons[2].getElementsByTagName('name')[0].childNodes[0].nodeValue = "New Value"

persons[0].setAttribute('id', '100')
persons[3].getElementsByTagName('age')[0].childNodes[0].nodeValue = "-110"
# these changes now are just in python code - in the ram just now we need to
# change it actually in dom tree like this: (i ll use new file to see result but can rewrite the old one...)
domtree.writexml(open('data2.xml', "w"))


