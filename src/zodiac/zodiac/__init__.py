from pyramid.config import Configurator
from resources import Root
import views
import pyramid_jinja2
import os

__here__ = os.path.dirname(os.path.abspath(__file__))


def make_app():
    """ This function returns a Pyramid WSGI application.
    """
    settings = {}
    settings['mako.directories'] = os.path.join(__here__, 'templates')
    config = Configurator( root_factory=Root, settings=settings )
    config.add_renderer('.jinja2', pyramid_jinja2.Jinja2Renderer)
    
    

    config.add_view(views.zodiac_view,
                    context=Root,
                    renderer='zodiac.mako')

    config.add_route( "entra_dades", "/entra_dades" )
    config.add_view( views.entra_dades_view, route_name="entra_dades", renderer="entra_dades.mako" )

    config.add_route( "guest_book", "/guest_book" )
    config.add_view( views.guest_book_view, route_name="guest_book", renderer="guest_book.mako" )



    config.add_static_view(name='static',
                           path=os.path.join(__here__, 'static'))
    return config.make_wsgi_app()

application = make_app()
