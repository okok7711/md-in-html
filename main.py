import markdown
from js import fetch
import asyncio

# Fetch local README
content = await (await fetch("./README.md")).text()

print(markdown.markdown(content, extensions=["toc"]))