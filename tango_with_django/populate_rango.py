import os

def populate():
    python_cat = add_cat('Python', 128, 64)
    add_page(cat=python_cat,
            title='Official Python Tutorial',
            views='5',
            url='http://docs.python.org/2/tutorial/')
    add_page(cat=python_cat,
            title='Learn Python in 10 minutes',
            views='2',
            url='http://www.korokithakis.net/tutorials/python/')
    add_page(cat=python_cat,
            title='How to Think like a Computer Scientist',
            views='10',
            url='http://www.greenteapress.com/thinkpython/')

    django_cat = add_cat('Django', 64, 32)
    add_page(cat=django_cat,
            title='Official Django Tutorial',
            views='50',
            url='https://docs.djangoproject.com/en/1.5/intro/tutorial01/')
    add_page(cat=django_cat,
            title='Django Rocks',
            views='1',
            url='http://www.djangorocks.com/')
    add_page(cat=django_cat,
            title='How to Tango with Django',
            views='100',
            url='http://www.tangowithdjango.com/')

    frame_cat = add_cat('Other Frameworks', 32, 16)
    add_page(cat=frame_cat,
            title='Bottle',
            views='120',
            url='http://bottlepy.org/docs/dev/')
    add_page(cat=frame_cat,
            title='Flask',
            views='55',
            url='http://flask.pocoo.org')

    # Print out what we have added to the user
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print '- {0} - {1}'.format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url,
                                    views=views)[0]
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c

# Start execution here!
if __name__ == '__main__':
    print 'Starting Rango population script...'
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'tango_with_django.settings')
    from rango.models import Category, Page
    populate()
