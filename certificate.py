#! certificate.py
"""
File certificate.py: a Python script to generate a bare-bones class completion certificate: printed,
and saved in text and html files displayed ina  web browser.
"""

import time, sys, webbrowser
import html

htmlescape =  html.escape


maxline = 60
browser = True
saveto  = 'Certificate.txt'
template = """
%s

===> Official Certificate <===

Date: %s

This certifies that:

\t%s

has survived the massive time:

\t%s

and is now entitled to all privileges thereof, including
the right to proceed on to learning how to develop Web
sites, desktop GUIs, scientific models, and assorted apps,
with the possible assistance of follow-up applications
books such as Programming Python (shameless plug intended).

--Mark Lutz, Instructor

(Note: certificate void where obtained by skipping ahead.)

%s
"""

# interact, setup
for c in 'Congratuations!'.upper():
    print(c, end=' ')
    sys.stdout.flush()
    time.sleep(0.25)
print()

date = time.asctime()
name = input('Enter your name: ').strip() or 'An unknown reader'
sept = '*' * maxline
book = 'Learning Python 5th Edition'

#Make text file version
file = open(saveto, 'w')
text = template % (sept, date, name, book, sept)
print(text, file=file)
file.close()

# Make htmlk file version
htmlto = saveto.replace('.txt', '.html')
file = open(htmlto, 'w')

tags = text.replace(sept, '<hr>')
tags = tags.replace('===>', '<h1 align=center>')
tags = tags.replace('<===', '</h1>')

tags = tags.split('\n')

tags = ['<p>' if line == ''
else line for line in tags]
tags = ['<i>%s</i>' % htmlescape(line) if line[:1] == '\t' else line for line in tags]
tags = '\n'.join(tags)
link = '<i><a href="http://www.rmi.net/~lutz">Book support site</a></i>\n'
foot = '<table>\n<td><img src="ora-lp.jpg" hspace=5>\n<td>%s</table>\n' % link
tags = '<html><body bgcolor=beige>' + tags + foot + '</body></html>'

print(tags, file=file)
file.close()

# display results
print('[file: %s]' % saveto, end=' ')
print('\n' * 2, open(saveto).read())

if browser:
    import os
    print(os.getcwd())
    print('open browser-----------%s' % htmlto)
    # res2 = webbrowser.open('file:///Users/justin/Desktop/Python3/Certificate.html', new=True)
    res2 = webbrowser.open('file://' + os.path.realpath(htmlto), new=True)

    print(res2)

if sys.platform.startswith('win'):
    input('[Press Enter]')
