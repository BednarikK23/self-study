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

# lastly how to create/add new elements to xml file
newperson = domtree.createElement('person')
newperson.setAttribute('id', '7')

# create independet elements
name = domtree.createElement('name')
name.appendChild(domtree.createTextNode('Paul Green'))

age = domtree.createElement('age')
age.appendChild(domtree.createTextNode('12'))

weight = domtree.createElement('weight')
weight.appendChild(domtree.createTextNode('58'))

height = domtree.createElement('height')
height.appendChild(domtree.createTextNode('179'))

# add independent element into new person
newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

# now we have to append this person to the group object to the document elements
domtree.writexml(open('data3.xml', "w"))

