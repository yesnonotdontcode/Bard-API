from pywebio.input import *

code = textarea('Code Edit', code={
    'mode': "python",
    'theme': 'darcula',
}, value='import something\n# Write your python code')