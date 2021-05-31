from datetime import datetime
from werkzeug.utils import redirect
from flask import Blueprint, render_template, request, url_for
from villvill.models import Search
from ..forms import AnswerForm, QuestionForm
from .. import db

bp = Blueprint('search', __name__, url_prefix='/search')

@bp.route('/')
def search_li():
    page = request.args.get('page', type=int, default=1)    # 페이지
    search_list = Search.query.order_by(Search.create_date.desc())
    search_list = search_list.paginate(page, per_page=10)
    return render_template('search/search_list.html', search_list=search_list)

@bp.route('/<int:search_id>/')
def search_detail(search_id):
    form = AnswerForm()
    search = Search.query.get_or_404(search_id)
    return render_template('search/search_detail.html', search=search, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        search = Search(subject=form.subject.data, content=form.content.data,
                        create_date=datetime.now())
        db.session.add(search)
        db.session.commit()
        return redirect(url_for('search.search_li'))
    return render_template('search/search_form.html', form=form)

