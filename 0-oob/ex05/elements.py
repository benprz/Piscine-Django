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
    def __init__(self, attr={}):
        super().__init__(tag='meta', attr=attr, tag_type='simple')

class Img(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='img', attr=attr, tag_type='simple')

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
    def __init__(self, attr={}):
        super().__init__(tag='hr', attr=attr, tag_type='simple')

class Br(Elem):
    def __init__(self, attr={}):
        super().__init__(tag='br', attr=attr, tag_type='simple')

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

    elem_title = Title(Text("Hello ground!"))
    elem_meta = Meta({"charset": "utf-8"})
    elem_head = Head([elem_meta, elem_title], {"lang": "fr"})
    elem_h2 = H2(Text("BURNET Lucille"))
    elem_h1 = H1(Text("CV pour la Piscine Django"))
    elem_br = Br()
    elem_p = P([Text("parce qu'il faut bien la tester aussi"), elem_br])
    elem_img = Img({"src": "http://i.imgur.com/pfp3T.jpg"})
    elem_div = Div([elem_p, elem_img])
    elem_li = Li(Text("Algorithmique, Techniques d'optimisation et IA"))
    elem_ul = Ul(elem_li)
    elem_ol = Ol(elem_li)
    elem_span = Span([elem_ol, elem_ul])
    elem_th = Th(Text("Langues"), {"colspan": "2"})
    elem_tr0 = Tr(elem_th)
    elem_thead = Elem(tag='thead', content=elem_tr0)
    elem_td0 = Td()
    elem_td1 = Td(Text("niveau"))
    elem_tr1 = Tr([elem_td0, elem_td1])
    elem_tbody = Elem(tag='tbody', content=elem_tr1)
    elem_table = Table([elem_thead, elem_tbody])
    elem_hr = Hr()
    elem_body = Body([elem_h2, elem_h1, elem_div, elem_span, elem_table, elem_hr])
    elem_html = Elem(tag='html', content=[elem_head, elem_body], attr={'lang': 'fr'})
    print(elem_html)