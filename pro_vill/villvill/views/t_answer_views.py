from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect
from ..forms import AnswerForm
from villvill import db
from villvill.models import Transfer, T_Answer

bp = Blueprint('t_answer', __name__, url_prefix='/t_answer')

@bp.route('/create/<int:transfer_id>', methods=('POST', ))
def create(transfer_id):
    form = AnswerForm()
    transfer = Transfer.query.get_or_404(transfer_id)
    if form.validate_on_submit():
        content = request.form['content']
        answer = T_Answer(content=content, create_date=datetime.now())
        transfer.transfer_set.append(answer)
        db.session.commit()
        return redirect(url_for('transfer.transfer_detail', transfer_id=transfer_id))
        
    return render_template('transfer/transfer_detail.html', transfer=transfer, form=form)