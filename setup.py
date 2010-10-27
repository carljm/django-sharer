import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='django-sharer',
    version='0.2.1',
    description="A Django app that provides helpers for serving static files.",
    long_description=read('README'),
    author='Taylan Pince',
    author_email='taylan@taylanpince.com',
    license='Apache',
    url='http://github.com/taylanpince/django-sharer/',
    packages=[
        'sharer',
        'sharer.templatetags',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    package_data={'sharer': ['fixtures/*.json',
                             'media/css/*.css',
                             'media/js/*.js',
                             'media/images/*.png',
                             'media/icons/*.png',
                             'templates/sharer/*.*',
                             'templates/sharer/includes/*.*',
                             ]}
)
