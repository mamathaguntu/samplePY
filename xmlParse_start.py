# Parse and Process XML 
import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("samplexml.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))

    # create new skill tag and append in the file
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name","React")
    doc.firstChild.appendChild(newSkill)

    skills = doc.getElementsByTagName("skill")
    print("%d skills: " % skills.length)
    for skill in skills:
        print(skill.getAttribute("name"))


if __name__ == "__main__":
    main()