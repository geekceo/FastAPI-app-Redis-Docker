from app.configuration.routes.routes import Routes
from app.internal.routes import user, currency

__routes__ = Routes(routers=(user.router, currency.router))