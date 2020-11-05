To upload your stuff to Github, you should not directly clone this repository. Instead, you should make a copy with your own account (a [fork](https://docs.github.com/en/enterprise-server@2.20/github/getting-started-with-github/fork-a-repo)). You are not allowed to `git push` your stuff to my copy, but you can to yours.

I split this up into blocks. If you have troubles finishing them all, (esp BeautifulSoup), no problem. We can talk about what you finish. 

# Table of Contents
- [Table of Contents](#table-of-contents)
- [General Python](#general-python)
  - [The Python Interpreter/CLI](#the-python-interpretercli)
  - [Autocomplete](#autocomplete)
  - [Extending the palindrome](#extending-the-palindrome)
- [More Git](#more-git)
- [Object-Oriented Programming](#object-oriented-programming)
- [Lambdas & some Functional programming](#lambdas--some-functional-programming)
- [BeautifulSoup](#beautifulsoup)
  - [Copying HTML](#copying-html)
  - [Browser Inspect Element](#browser-inspect-element)
  - [BeautifulSoup](#beautifulsoup-1)
  - [The actual assignment](#the-actual-assignment)


# General Python 

## The Python Interpreter/CLI
Using python's command-line interpreter (CLI) is often more useful than writing a file. This is what pops up when you run `python` with no other arguments. You can more easily test things in the CLI. Just remember that any variable you declare will continue to exist until you exit with `quit()`. 

For the files that I have already written, it may be useful to test their functionality without running the entire file. If you try to run `tictactoe.py`, it will fail. However, you can run the CLI, then import `Board` and/or `Game` with `import tictactoe`, then run a function like this: `b = tictactoe.Board()`. You can then do something like `b.valid_move(5)`. 

Whenever you change a file, this will not show up in the CLI. You will need to restart it. Alternatively, you can `import importlib` (only needs to be done once), then `importlib.reload(tictactoe)`.

## Autocomplete
Most terminal-like environments will have some sort of autocomplete. You may have this with `cd`: you can try typing half of the name of a directory, hit `<tab>`, and it should fill in the rest of the directory name.

Similarly, python will autocomplete. If you look @ the above, typing `importlib.reload(tic` and `<tab>` should fill it out.

## Extending the palindrome

I would not bother with this part until last. If you are having trouble w/ BeautifulSoup and want to take a break, maybe do this instead: make a file with an extended palindrome checker. It should not include spaces/punctuation in flipped phrase: `"Madam, I'm Adam"`. You should still include numbers, though.

# More Git

You may notice that there is a `.gitignore` file. You may want to look up what it does. 

In addition, please go find a `.gitigore` file more suited for python, and replace the existing one. Feel free to plagiarize.

# Object-Oriented Programming

I wrote up a file that creates & plays a tic-tac-toe game between two players. There are two objects: `Board` controls the state of the board, and `Game` controls the interaction between players. 

Any function that has a `TODO` or `pass` in it is unfinished. The `TODO`s are just comments, but `pass` means "do nothing" in python. 

Each function should only depend on the state of the class it is in. Additionally, _one function does not need to be within an object_, because it does not depend on any of the state! Just try to identify that one so we can talk about it.

# Lambdas & some Functional programming

Functional programming is a different methodology than Object-Oriented. You can see a breakdown [here](https://www.tutorialspoint.com/functional_programming/functional_programming_introduction.htm). I don't expect you to know everything it says. 

Basically, what you should know: functional programming does __not__ use objects. This can make it hard to remember the state of your application. For example, our `Board` and `Game` use objects that hold several variables within them: player names, the token, etc. It would be possible to write this without objects, but might be harder to read. Just take my word for it for now.

However, it makes for some interesting design patterns:

1. functions as a return value
2. generators
3. map/reduce/filter

I wrote some directions in the `functional.py` file itself.

You might want to use the python CLI to test my functions. For example, you may want to try line 11 with a different `x` value.

# BeautifulSoup

Let's transition into using some libraries. Hopefully you are familiar with the concept of HTML. HTML has a lot of tags, which we may or may not get into. When you write an HTML file, the browser looks at it and creates a Document Object Model (DOM). [DOM is the tree model used to represent HTML](https://stackoverflow.com/a/4110090/7163811) (the next answer is also pretty good). Although you write a `.py` file, when you run it, it becomes a "program." HTML and the DOM are like that.

## Copying HTML

At any time, you can look at the raw HTML of a page by right clicking -> "view page source." 
1. Take a page from wikipedia, copy the source to a new file with the `html` extension.
2. Try opening the file (just double click it in your file explorer)
3. It should look mostly the same, but it might be weird because we didn't also copy the CSS & Javascript.

Although the HTML may not include styling or scripts, it should include most of what you actually read on the page.

## Browser Inspect Element

More usefully, you can right click -> "Inspect element" to bring up your browser's inspector. [Here](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) is an excellent guide to it. I recommend using it on an element (like an image, or a block of text, or a header). Try changing the text of the element. Try looking for the CSS rules (in that pane) and changing the element size or layout. Some elements may resist change, depending on their parents.

If you have the pane open, you should see a box with a mouse icon in the top left. Using this will allow you to select a new DOM element.

We may use 'inspect element' a lot. It allows you to debug your HTML/CSS without changing the file & reloading.

## BeautifulSoup

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) is a library for fetching and parsing the HTML of a webpage using python. 

You should be able to install it with `pip`, which is the package manager for python. `pip` comes with python, and manages your external libraries. Try `pip install beautifulsoup4`.

The [documentation]((https://www.crummy.com/software/BeautifulSoup/bs4/doc/)) is very good, but it is still intended for people with more experience. Sometimes Google or StackOverflow will be more useful. Don't be afraid to [ask me a question](https://stackoverflow.com/help/how-to-ask). Feel free to text me or email me.

## The actual assignment

Make a new python file.

We will scrape the [Wikipedia outline of web design and web development](https://en.wikipedia.org/wiki/Outline_of_web_design_and_web_development). Like any good programmer, we are going to ignore everything unless we absolutely need it.

I would like you to use BeautifulSoup to parse this page, and make two arrays, one for each of the lists on the webpage. You should __not__ be hardcoding any of the contents of the list. You may need the strings `"Web_Design"` and `"Web_Development"`, but that should be about it.

Your function should look something like this:
```python
import requests
from bs4 import BeautifulSoup
def get_design_dev_lists():
  url = "https://en.wikipedia.org/wiki/Outline_of_web_design_and_web_development"
  res = requests.get(url) # make a HTTP request for the page
  text = res.text # get the actual HTML from the request
  soup = BeautifulSoup(text, 'html.parser') # heyyy, it's an object!
  
  ...
  # get the contents of the lists & put them in two arrays
```

It should return or print two lists. Each list should be a _list of dictionaries_. Each dictionary should contain information about the element of the list:
- title
- the link to the page
- if it has subtopics, include those (as a list of dicts)

```python
web_design = [
  {
    'title': 'graphic design',
    'link': 'https://en.wikipedia.org/wiki/Graphic_design',
    'subtopics': [
      {
        'title': 'typography',
        'link': 'https://en.wikipedia.org/wiki/Typography',
      },{
        'title': 'page layout',
        'link': 'https://en.wikipedia.org/wiki/Page_layout',
      }
    ]
  },{
    'title': 'User experience design (UX design)',
    ... 
]

web_development = [
  {
    'title': 'Front-end web development – the practice of converting data to a graphical interface, through the use of HTML, CSS, and JavaScript, so that users can view and interact with that data.',
    'link': 'https://en.wikipedia.org/wiki/Front-end_web_development',
    'subtopics': [
      ... 
    ]
  }, ...
]
```

Notice that "Web Design" is within `<h2><span class="mw-headline" id="Web_Design">Web Design</span> ... </h2>`. You can get the `<span>` by looking for its id, then the `<h2>` is the parent of that span. After the `<h2>`, the next node in the DOM is the `<ul>` that contains all of the links.

Take it easy. Just start with grabbing the `<span>`, then try for the `<h2>`, then the `<ul>`, and so on. 