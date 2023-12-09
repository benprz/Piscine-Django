from elem import Elem, Text

"""
• html, head, body
• title
• meta
• img
• table, th, tr, td
• ul, ol, li
• h1
• h2
• p
• div
• span
• hr
• br"""

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='html', content=content, attr=attr)

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='head', content=content, attr=attr)

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='body', content=content, attr=attr)

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='title', content=content, attr=attr)

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='meta', content=content, attr=attr)

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='img', content=content, attr=attr)

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='table', content=content, attr=attr)

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='th', content=content, attr=attr)

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='tr', content=content, attr=attr)

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='td', content=content, attr=attr)

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ul', content=content, attr=attr)

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='ol', content=content, attr=attr)

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='li', content=content, attr=attr)

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h1', content=content, attr=attr)

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='h2', content=content, attr=attr)

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='p', content=content, attr=attr)

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='div', content=content, attr=attr)

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='span', content=content, attr=attr)

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='hr', content=content, attr=attr)

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__(tag='br', content=content, attr=attr)

if __name__ == '__main__':
    print( Html( [Head(), Body()] ) )

    """<html>
<head>
<title>
"Hello ground!"
</title>
</head>
<body>
<h1>
"Oh no, not again!"
</h1>
<img src="http://i.imgur.com/pfp3T.jpg" />
</body>
</html>"""

    html = Html( [
        Head( [Title( [Text('"Hello ground!"')] )] ),
        Body( [
            H1( [Text('"Oh no, not again!"')] ),
            Img( attr={'src': 'http://i.imgur.com/pfp3T.jpg'} )
        ] )
    ] )
    print(html)