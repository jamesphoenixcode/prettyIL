# PrettyIL
## A pretty way to use instaloader lib.
This was an idea for better and pretty organization of IL Lib downloaded data.
In short, data hoarding.
## Install all the requirements:
```
pip install -r requirements.txt
```
### This will be the folder tree generated when the script runs:
```bash
    |-- username/
    |   |-- Highlights/
    |   |   |-- HighlightTitle/
    |   |   |   |-- {DATE_UTC}_UTC.jpg
    |   |   |   |-- {DATE_UTC}_UTC.mp4
    |   |   |   |-- {DATE_UTC}_UTC.json.xz
    |   |-- Posts/
    |   |   |-- DateUTC/
    |   |   |   |-- {DATE_UTC}_UTC.jpg
    |   |   |   |-- {DATE_UTC}_UTC_1.jpg 
    |   |   |   |-- {DATE_UTC}_UTC_2.mp4 
    |   |   |   |-- {DATE_UTC}_UTC.json.xz 
    |   |   |   |-- {DATE_UTC}_UTC_comments.json
    |   |-- {username}.json
    |   |-- {username}_resume.txt
```
**NOT OPTIONAL:**

For use this without errors, you need to add a @property to the `Profile` class:
- 1. Got to your site-packages folders:
    - If you have a virtual env: `venv\Lib\site-packages\instaloader\structures.py`
    - Or global python:
    `python3Folder\Lib\site-packages\instaloader\structures.py`
- 2. Paste this code wherever inside `Profile` class, i recommend below `biography` property at line: `876`
```python
@property
def entities(self) -> str:
    '''This property will return a list or single ``string`` of the sponsored accounts/entities showed in the target profile
        or ``No sponsors list.`` string.
        '''
    # Check if the target has entities.
    if len(self._metadata('biography_with_entities')["entities"]) == 0:
        return "No sponsors list."
    else:
        # If so, create the list/single string and return it.
        sponsorsList = ""
        for item in self._metadata('biography_with_entities')["entities"]:
            sponsorsList = sponsorsList + f'{item["user"]["username"]}\n'
        return sponsorsList
```
I open a pull req to instaloader lib with that modification: [My Pull Req](https://github.com/instaloader/instaloader/pull/1899)

## Any advice for better coding, comment, docummentation or related it's apreciate, i'm starting in coding and sharing that code thank u <3.
## Thanks to this project build by me for being an inspiration for a bigger idea [PyPanelX](https://github.com/jamesphoenixcode/pypanelx)
