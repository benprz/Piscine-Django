#!/usr/bin/python3

class Text(str):
    """
    A Text class to represent a text you could use with your HTML elements.

    Because directly using str class was too mainstream.
    """

    @staticmethod
    def __replace_chars_with_codes(text: str) -> str:
        return text.replace('&', "&amp;")\
                    .replace('"', "&quot;")\
                    .replace("'", "&apos;")\
                    .replace('<', "&lt;")\
                    .replace('>', "&gt;")
        
    def __str__(self):
        """
        Do you really need a comment to understand this method?..
        """
        return self.__replace_chars_with_codes(super()).replace('\n', '\n<br />\n')

class Elem:
    """
    Elem will permit us to represent our HTML elements.
    """

    def __init__(self, tag='div', attr={}, content=None, tag_type='double'):
        self.tag = tag
        self.attr = attr
        self.content = []
        if isinstance(content, type(None)) or self.check_type(content):
            if content:
                if not type(content) == list: self.content = [content]
                else: self.content = content
        else:
            raise Elem.ValidationError
        self.tag_type = tag_type

    def __str__(self):
        """
        The __str__() method will permit us to make a plain HTML representation
        of our elements.
        Make sure it renders everything (tag, attributes, embedded
        elements...).
        """
        result = ''
        if self.tag_type == 'double':
            result = f"<{self.tag}{self.__make_attr()}>"
            content_result = self.__make_content()
            if content_result != '' and content_result != '\n':
                result += content_result
                result = self.__replace_codes_with_chars(result)
                result = result.replace('\n', '\n  ')
                result = result[0:-2]
            result += f"</{self.tag}>"
        elif self.tag_type == 'simple':
            result = f"<{self.tag}{self.__make_attr()}>"
        return result


    def __make_attr(self):
        """
        Here is a function to render our elements attributes.
        """
        result = ''
        for pair in sorted(self.attr.items()):
            result += ' ' + str(pair[0]) + '="' + str(pair[1]) + '"'
        return result

    def __make_content(self):
        """
        Here is a method to render the content, including embedded elements.
        """

        if len(self.content) == 0:
            return ''
        result = '\n'
        for elem in self.content:
            if str(elem) != '':
                result += f"{elem}\n"
        return result

    def add_content(self, content):
        if not Elem.check_type(content):
            raise Elem.ValidationError
        if type(content) == list:
            self.content += [elem for elem in content if elem != Text('')]
        elif content != Text(''):
            self.content.append(content)

    @staticmethod
    def check_type(content):
        """
        Is this object a HTML-compatible Text instance or a Elem, or even a
        list of both?
        """
        return (isinstance(content, Elem) or type(content) == Text or
                (type(content) == list and all([type(elem) == Text or
                                                isinstance(elem, Elem)
                                                for elem in content])))

    @staticmethod
    def __replace_codes_with_chars(text: str) -> str:
        return text.replace("&amp;", '&')\
                    .replace("&quot;", '"')\
                    .replace("&apos;", "'")\
                    .replace("&lt;", '<')\
                    .replace("&gt;", '>')

    class ValidationError(Exception):
        pass
