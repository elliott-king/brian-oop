import requests
from bs4 import BeautifulSoup

def get_design_dev_lists():
    url = "https://en.wikipedia.org/wiki/Outline_of_web_design_and_web_development"
    res = requests.get(url) # make a HTTP request for the page
    text = res.text # getting the actual HTML from the request
    soup = BeautifulSoup(text, 'html.parser')

    list1 = []
    web_design = soup.find("span", id="Web_Design") # finding the web design section
    ul1 = web_design.parent.next_sibling.next_sibling # finding the unordered list of items in that section
    for list_item in ul1.contents:
        if list_item != "\n":
            if not list_item.ul:
                list1.append({'title': list_item.a['title'], 'link': "https://en.wikipedia.org" + list_item.a['href'], 'subtopics': None})
            else:
                try:
                    if list_item.contents[0]['title']:
                        subtopics_temp = []
                        for list_item_sub in list_item.contents[2]:
                            if list_item_sub != "\n":
                                subtopics_temp.append({'title': list_item_sub.a['title'], 'link': "https://en.wikipedia.org" + list_item_sub.a['href']})
                        list1.append({'title': list_item.contents[0]['title'], 'link': "https://en.wikipedia.org" + list_item.contents[0]['href'], 'subtopics': subtopics_temp})
                except:
                    subtopics_temp = []
                    for list_item_sub in list_item.contents[1]:
                        if list_item_sub != "\n":
                            subtopics_temp.append({'title': list_item_sub.a['title'], 'link': "https://en.wikipedia.org" + list_item_sub.a['href']})
                    list1.append({'title': list_item.contents[0].rstrip(), 'link': "None", 'subtopics': subtopics_temp})
    
    list2 = []
    web_dev = soup.find("span", id="Web_Development")
    ul2 = web_dev.parent.next_sibling.next_sibling
    for list_item in ul2.contents:
        if list_item != "\n":
            if not list_item.ul:
                list2.append({'title': list_item.contents[0], 'link': None, 'subtopics': None})
            else:
                if list_item.contents[0]['title']:
                    subtopics_temp = []
                    for list_item_sub in list_item.contents[2]:
                        if list_item_sub != "\n":
                            try:
                                subtopics_temp.append({'title': list_item_sub.a['title'], 'link': "https://en.wikipedia.org" + list_item_sub.a['href']})
                            except:
                                subtopics_temp.append({'title': list_item_sub.string, 'link': None, 'subtopics': None})
                    list2.append({'title': list_item.contents[0]['title'], 'link': "https://en.wikipedia.org" + list_item.contents[0]['href'], 'subtopics': subtopics_temp})
    print("Web Design List: ", list1)
    print("\n")
    print("Web Development List: ", list2)
if __name__ == "__main__":
    get_design_dev_lists()