'''
Pyfiglet is a python module for converting strings into ASCII Text with arts fonts
'''

from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('text to render'))