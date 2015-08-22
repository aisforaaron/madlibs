from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict # used to keep dict item order consistent
from stories.models import Story # for db calls
import re  # regular expression methods


# homepage, print form for user to pick story by title
def index(request):
    request.session.flush() # make sure session starts out clean
    context = {'story_list': get_stories()}
    return render(request, 'stories/index.html', context)


# print form for web user to enter token values
def answers_form(request):
    story_num = int(request.POST['choice'])
    # get story text based on id passed in form
    story = get_stories(story_num)
    # replace tokens in story so they are unique. {noun} to {1noun}
    story_text = story_with_unique_tokens(story.story_body)
    request.session['story_text'] = story_text # save to session
    # get list of tokens in story, if set to 'pretty' remove '{#'..'}'
    tokens = get_tokens(story_text, request)
    tokens_pretty = get_tokens(story_text, request, 'pretty')
    # create custom tokens key/value dict - OrderedDict used to keep proper token order
    tokens = OrderedDict(zip(tokens, tokens_pretty))
    # print new form with tokens to replace
    context = {'tokens': tokens, 'story_num': story_num}
    return render(request, 'stories/replace.html', context)


# return story text with {#token-name} replaced from {token-name}
# called by answers_form
def story_with_unique_tokens(story_picked):
    # split story text into lines by line break delimeter (splitlines method)
    story_lines = story_picked.splitlines()
    # replace tokens w/unique tokens 
    story_lines_tokens = []
    counter=1
    # loop through lines in story
    for line in story_lines:
        # each updated line is saved into list as an item
        line_final = [] 
        # if the line is a line break "\n" line is null
        # so add empty slot to list
        if not line:
            story_lines_tokens.append('')
        else:
            # loop through all words in line, split by spaces
            for word in line.split(' '):
                # see if word is a token. a string like {...}
                w = check_word_for_token(word)
                # if there is a match, it's a token so replace with unique token name
                if w:
                    word_final = '{' + str(counter) + w.group(2) + '}' + w.group(4) # w.group(4) is for punctuation/spaces
                    counter+=1
                else:
                    word_final = word
                # rebuild line w/tokens
                line_final.append(word_final)
            # rebuild line w/line breaks
            j = ' '.join(line_final)
            story_lines_tokens.append(j)
    # convert new story w/unique tokens back to string
    story_picked = '\n'.join(story_lines_tokens)    
    return story_picked


# take user entered tokens from form, replace and print updated story
def print_story(request):
    story_text = request.session['story_text']
    for key, value in request.POST.iteritems():
        if key[0] == '{':
            story_text = re.sub(key, value, story_text)
    context = {'story_text': story_text}
    return render(request, 'stories/done.html', context)


# return all stories or one specific story 
def get_stories(story_num=None):
    if story_num is not None:
        story_num = int(story_num)
        story_items = Story.objects.get(id=story_num)
    else:
        story_items = Story.objects.all().order_by('id').reverse()
    # @todo check for errors if no story(s) returned
    return story_items


def check_word_for_token(word):
    # see if word is a token by pattern: {letters}
    return re.match(r'({)(.*?)(})(.*)', word, re.M|re.I)


def get_tokens(story, request, token_format=None):
    # return list of tokens per story
    tokens = re.findall(r'({.*?})', request.session.get('story_text'), re.M|re.I)
    if token_format == 'pretty':
        # remove {} from tokens list
        tokens_pretty = map(lambda tokens:tokens.strip('{}'),tokens)
        # remove unique number from token
        tokens_pretty_final = []
        for token in tokens_pretty:
            tokens_pretty_final.append(''.join(i for i in token if i.isalpha()))
        tokens = tokens_pretty_final
    return tokens