from django.shortcuts import render

# Create your views here.
def django(request):
    context = dict(
        title='Ex01: Django, framework web.',
        cssfile='style1.css',
        content='Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Django was born in the fall of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications.'
    )

    return render(request, 'base.html', context)
    
def display(request):
    context = dict(
        title='Ex01: Display process of a static page.',
        cssfile='style1.css',
        content='User requests a url, django then searches for the corresponding view function, which renders the template with the context and returns an HttpResponse object.'
    )

    return render(request, 'base.html', context)

def templates(request):
    context = dict(
        title='Ex01: Template engine.',
        cssfile='style2.css',
        content="Django's default template engine is a system that allows you to define HTML templates with placeholders for dynamic content.\
            These placeholders are filled with data when the template is rendered.\
                Blocks: Blocks are defined using {% block blockname %} and {% endblock %} tags. They act as placeholders for content that can be overridden in child templates. This is useful for sections of your site that you want to customize for different pages, like the title or main body content. \
            Loops (for ... in): Django's template language includes a {% for %} tag for looping over items in a list. The syntax is {% for item in list %}. Inside the loop, you can use {{ item }} to display the current item. The loop ends with a {% endfor %} tag.\
If Control Structures: You can use {% if %} tags to conditionally display content. The syntax is {% if condition %}. If the condition is true, the content inside the if block is displayed. You can also use {% elif %} and {% else %} tags for more complex conditions. The if block ends with a {% endif %} tag.\
Display of Context Variables: You can display context variables using {{ variable_name }} syntax. When the template is rendered, each {{ variable_name }} is replaced with the value of the corresponding variable in the context. If the variable is a complex Python object, you can access its attributes using dot notation, like {{ variable.attribute }}."
    )

    return render(request, 'base.html', context)