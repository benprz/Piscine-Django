from elem import Elem
from elements import *

class Page(Elem):
    __supported_tags = [ 'html', 'head', 'body', 'title', 'meta', 'img', 'table', 'th', 'tr', 'td', 'ul', 'ol', 'li', 'h1', 'h2', 'p', 'div', 'span', 'hr', 'br' ]
    __body_and_div_allowed_tags = [ 'h1', 'h2', 'div', 'table', 'ul', 'ol', 'span']
    
    def __init__(self, content: Elem):
        self.content = content

    def is_valid(self):
        valid = True
        if not self.__check_if_elem_tags_are_supported(self.content):
            valid = False
        elif not self.__check_if_elems_are_correctly_nested(self.content):
            valid = False
        return valid

    # True if valid, False if not
    @staticmethod
    def __check_if_elem_tags_are_supported(elem):
        #recusively check if all tags are supported
        if not isinstance(elem, Elem):
            return True
        if elem.tag not in Page.__supported_tags:
            return False
        if elem.content:
            for content in elem.content:
                if not Page.__check_if_elem_tags_are_supported(content):
                    return False
        return True
    
    def __check_if_elems_are_correctly_nested(self, elem):
        if not self.__check_if_html_elem_is_valid(elem):
            return False
        elif not self.__check_if_head_elem_is_valid(elem.content[0]):
            return False
        elif not self.__check_if_body_and_div_elems_are_valid(elem.content[1]):
            return False
        elif not self.__check_if_title_hx_li_th_td_elems_are_valid(elem):
            return False
        elif not self.__check_if_p_elems_are_valid(elem):
            return False
        return True
    
    @staticmethod
    def __check_if_html_elem_is_valid(elem):
        if elem.tag == 'html':
            if not elem.content or len(elem.content) != 2:
                return False
            if not elem.content[0].tag == 'head' or not elem.content[1].tag == 'body':
                return False
        return True
    
    @staticmethod
    def __check_if_head_elem_is_valid(elem):
        if elem.tag == 'head':
            if not elem.content or len(elem.content) != 1:
                return False
            if not elem.content[0].tag == 'title':
                return False
        return True
    
    @staticmethod
    def __check_if_body_and_div_elems_are_valid(elem):
        #recursively check if all body and div elems only contain  H1, H2, Div, Table, Ul, Ol, Span, or Text elements
        if elem.content and (elem.tag == 'body' or elem.tag == 'div'):
            for content in elem.content:
                if not isinstance(content, Text):
                    if content.tag not in Page.__body_and_div_allowed_tags:
                        return False
                    elif content.tag == 'div':
                        if not Page.__check_if_body_and_div_elems_are_valid(content):
                            return False
        return True
    
    @staticmethod
    def __check_if_title_hx_li_th_td_elems_are_valid(elem):
        #recursively check if all title, hx, li, th, and td elems only contain one text element
        if elem.content:
            for content in elem.content:
                if not isinstance(content, Text):
                    if (content.tag == 'title' or content.tag == 'h1' or content.tag == 'h2' or content.tag == 'li' or content.tag == 'th' or content.tag == 'td'):
                        if (len(content.content) != 1 or not isinstance(content.content[0], Text)):
                            return False
                    elif not Page.__check_if_title_hx_li_th_td_elems_are_valid(content):
                        return False
        return True
    
    @staticmethod
    def __check_if_p_elems_are_valid(elem):
        #recursively check if all p elems only contain Text elements
        if elem.content:
            for content in elem.content:
                if isinstance(content, Elem):
                    if content.tag == 'p':
                        if not isinstance(content.content[0], Text):
                            return False
                    if Page.__check_if_p_elems_are_vaxslid(content):
                        return False
        return True
    
    @staticmethod
    def __check_if_span_elemes_are_valid(elem):
        #recursively check if all span elems only contain Text or P elements
        if elem.content:
            for content in elem.content:
                if isinstance(content, Elem) and content.tag == 'span':
                    if not isinstance(content.content, Text) and not isinstance(content.content, P):
                        return False
                elif not Page.__check_if_span_elemes_are_valid(content):
                    return False
        return True

if __name__ == '__main__':
    page = Page(Html([
        Head([
            # Meta(attr={'charset': 'UTF-8'}),
            Title(Text('"Hello ground!"'))
            # Elem(tag='title', content=Text('"Hello ground!"'))
        ]),
        Body([
            # Meta(attr={'charset': 'UTF-8'}),
            H1(Text('"Oh no, not again!"')),
            Span(P([Text('"Oh no, not again!"'), Text('"O"')]))
        ])
    ]))
    print(page.is_valid())