

def markdown_beasts(bestiary):
    """
    Assumes that bestiary is a list of dicts, not a dict with nested lists.
    :param list[dict] bestiary:
    :return: a markdown formated string, with the name, id + img of beasts
    :rtype: str|unicode
    """
    md = ""
    layout = "Name: {name} Id: {id}  \n![image](http://flightrising.com{img})\n\n\n"
    for beast in bestiary:
        md += layout.format(name=beast['name'], id=beast['id'], img=beast['src'])
    return md

def write_markdown(bestiary, filename="bestiary.md"):
    """
    Given a bestiary, create markdown and write it to filename
    :param list[dict] bestiary:
    :param str|unicode filename:
    :rtype: NoneType
    """
    with open(filename, "w") as f:
        md = markdown_beasts(bestiary)
        f.write(md)

