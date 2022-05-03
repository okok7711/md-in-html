import markdown

test = """
# PyScript to avoid using HTML
[TOC]
## Why?
No one likes HTML, with pyscript you can use HTML to use JS to use WASM to use PY to use MD to avoid using HTML! Doesn't this sound awesome? Thanks  [PyScript](https://pyscript.net/)!
Add some CSS to make it look like GitHub's markdown using a modified version of [`github-markdown-css`](https://github.com/sindresorhus/github-markdown-css)  <br>
Now, I have to admit. It Might be a bit slow, since it has to evaluate and run all the python code before anything is displayed. BUT, no one cares.
## Ok, but Why?
Honestly, I don't know. Why does PyScript exist.
## How to? it sounds pretty nice!
Just edit the content of the [`main.py`](https://github.com/okok7711/md-in-html/blob/master/main.py) with your Markdown, refresh the site, and boom!
## TODO
- Read the Readme, so you dont need to look into python at all
"""

print(markdown.markdown(test, extensions=["toc"]))