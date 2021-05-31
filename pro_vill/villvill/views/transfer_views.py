import os
from datetime import datetime
from werkzeug.utils import redirect, secure_filename
from flask import Blueprint, render_template, request, url_for
from base64 import b64encode
from villvill.models import Transfer
from ..forms import AnswerForm, QuestionForm
from .. import db

bp = Blueprint('transfer', __name__, url_prefix='/transfer')

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/')
def transfer_li():
    page = request.args.get('page', type=int, default=1)    # 페이지
    transfer_list = Transfer.query.order_by(Transfer.create_date.desc())
    transfer_list = transfer_list.paginate(page, per_page=10)
    return render_template('transfer/transfer_list.html', transfer_list=transfer_list)

@bp.route('/<int:transfer_id>/')
def transfer_detail(transfer_id):
    form = AnswerForm()
    transfer = Transfer.query.get_or_404(transfer_id)
    images = []

    if transfer.img1_name != None:
        img1 = b64encode(transfer.img1).decode("utf-8")
        images.append(img1)
    if transfer.img2_name != None:
        img2 = b64encode(transfer.img2).decode("utf-8")
        images.append(img2)
    if transfer.img3_name != None:
        img3 = b64encode(transfer.img3).decode("utf-8")
        images.append(img3)
    if transfer.img4_name != None:
        img4 = b64encode(transfer.img4).decode("utf-8")
        images.append(img4)
    if transfer.img5_name != None:
        img5 = b64encode(transfer.img5).decode("utf-8")
        images.append(img5)
        
    return render_template('transfer/transfer_detail.html', transfer=transfer, form=form, images = images)


@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        f1 = request.files['image1']
        f2 = request.files['image2']
        f3 = request.files['image3']
        f4 = request.files['image4']
        f5 = request.files['image5']
        if f1 and allowed_file(f1.filename):
            f1name = secure_filename(f1.filename)
            m1type = f1.mimetype
            if f2 and allowed_file(f2.filename):
                f2name = secure_filename(f2.filename)
                m2type = f2.mimetype
            else:
                f2name=None
                m2type=None

            if f3 and allowed_file(f3.filename):
                f3name = secure_filename(f3.filename)
                m3type = f1.mimetype
            else:
                f3name=None
                m3type=None
                
            if f4 and allowed_file(f4.filename):
                f4name = secure_filename(f4.filename)
                m4type = f4.mimetype
            else:
                f4name=None
                m4type=None

            if f5 and allowed_file(f5.filename):
                f5name = secure_filename(f5.filename)
                m5type = f5.mimetype
            else:
                f5name=None
                m5type=None
            
            transfer = Transfer(subject=form.subject.data, content=form.content.data,
                            img1_name = f1name, 
                            img1=f1.read(),
                            mimetype1=m1type,
                            
                            img2_name = f2name, 
                            img2=f2.read(),
                            mimetype2=m2type,
                            
                            img3_name = f3name, 
                            img3=f3.read(),
                            mimetype3=m3type,

                            img4_name = f4name, 
                            img4=f4.read(),
                            mimetype4=m4type,

                            img5_name = f5name, 
                            img5=f5.read(),
                            mimetype5=m5type,
                            
                            create_date=datetime.now())
            db.session.add(transfer)
            db.session.commit()
            return redirect(url_for('transfer.transfer_li'))
        else:
            transfer = Transfer(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
            db.session.add(transfer)
            db.session.commit()
        return redirect(url_for('transfer.transfer_li'))

    return render_template('transfer/transfer_form.html', form=form)

# @bp.route('/uploader', methods = ['POST'])
# def upload_file():
#     f = request.files['file']
#     if f and allowed_file(f.filename):
#         fname = secure_filename(f.filename)
#         mtype = f.mimetype
#         image_test = ImageTest(name = fname, data = f.read(), mimetype = mtype)
#         db.session.add(image_test)
#         db.session.commit()
#         return 'file uploaded successfully'
#     else :
#         return 'Only Image available'

