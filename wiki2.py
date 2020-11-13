import requests
from bs4 import BeautifulSoup, NavigableString
import pprint

# def has_subtopics(list_item):
    # return T/F

def get_link(list_item):
    # check is it just text, or does it have a link?
    node_itself_no_children = list_item.contents[0]
    if isinstance(node_itself_no_children, NavigableString):
        return "None"
    else:
        return "https://en.wikipedia.org" + node_itself_no_children['href']

def get_name(list_item):
    node_itself_no_children = list_item.contents[0]
    if isinstance(node_itself_no_children, NavigableString):
        return node_itself_no_children.rstrip()
    else:
        return node_itself_no_children['title']

def get_subtopics(list_item):
    subtopics = []
    if list_item.ul: # check if has subtopics
        contents = list_item.ul.contents # array of list items
        for li in contents:
            if li != "\n":
                subtopics.append({
                    '_title': get_name(li),
                    'link': get_link(li),
                    'subtopics': get_subtopics(li),
                })
    
    return subtopics

def create_list(ul):
    list_topics = []
    for list_item in ul.contents:
        if list_item != "\n":

            list_topics.append({
                '_title': get_name(list_item),
                'link': get_link(list_item),
                'subtopics': get_subtopics(list_item),
            })
    return list_topics


def get_design_dev_lists():
    url = "https://en.wikipedia.org/wiki/Outline_of_web_design_and_web_development"
    res = requests.get(url) # make a HTTP request for the page
    text = res.text # getting the actual HTML from the request
    soup = BeautifulSoup(text, 'html.parser')

    web_design = soup.find("span", id="Web_Design") # finding the web design section
    ul1 = web_design.parent.find_next_sibling("ul") # finding the unordered list of items in that section
    list1 = create_list(ul1)

    web_dev = soup.find("span", id="Web_Development")
    ul2 = web_dev.parent.next_sibling.next_sibling
    list2 = create_list(ul2)

    file = open("output2.txt", "w+")
    pprint.pprint("Web Design List:", file)
    pprint.pprint(list1, file)
    pprint.pprint("", file)
    pprint.pprint("", file)
    pprint.pprint("", file)
    pprint.pprint("", file)
    pprint.pprint("", file)
    pprint.pprint("", file)
    # pprint.pprint("Web Development List: ", list2)
    pprint.pprint("Web Development List:", file)
    pprint.pprint(list2, file)
    file.close()

if __name__ == "__main__":
    get_design_dev_lists()