from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect
from ..forms import AnswerForm
from villvill import db
from villvill.models import Search, S_Answer

bp = Blueprint('s_answer', __name__, url_prefix='/s_answer')

@bp.route('/create/<int:search_id>', methods=('POST', ))
def create(search_id):
    form = AnswerForm()
    search = Search.query.get_or_404(search_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = S_Answer(content=content, create_date=datetime.now())
        search.search_set.append(answer)
        db.session.commit()
        return redirect(url_for('search.search_detail', search_id=search_id))
        
    return render_template('search/search_detail.html', search=search, form=form)