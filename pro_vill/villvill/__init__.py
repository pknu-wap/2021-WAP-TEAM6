from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    
    # 블루프린트
    from .views import main_views, search_views, s_answer_views, transfer_views, t_answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(search_views.bp)
    app.register_blueprint(s_answer_views.bp)
    app.register_blueprint(transfer_views.bp)
    app.register_blueprint(t_answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    
    return app