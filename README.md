# madlibs
Madlibs game.


# Overview
MadLibs is a script where you can create a file of stories with tokens,
then have the script ask the user which story to play and prompt with
tokens to replace.


# Adding Stories
Stories should be added to the stories.py file like so:

```python
madlibStories = {

	'Title Test' : '''Test story is the {adjective}!''',

	'Title of your story' : '''Content of your story.


You can add line breaks. This is how you add tokens for a {verb} and {noun} or {plural-noun}.''',

}
```

# How to play
Run this script from the command line:
	<code>$ python madlibs.py</code>