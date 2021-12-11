from flask import render_template, request, redirect
from db_config import *


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/instructions')
def instructions():
    return render_template('instructions.html')


@app.route('/view/<int:id>/view_update', methods=['post', 'get'])
def update(id):
    contacts = Contacts.query.get(id)
    if request.method == 'POST':
        contacts.first_name = request.form['first_name']
        contacts.second_name = request.form['second_name']
        contacts.phone = request.form['phone']
        contacts.email = request.form['email']

        try:
            db.session.add(contacts)
            db.session.commit()
            return redirect('/view')
        except:
            return "Some error occurs"
    else:

        return render_template('view_update.html', contacts=contacts)


@app.route('/add_contact', methods=['post', 'get'])
def add_contact():
    if request.method == 'POST':
        first_name = request.form['first_name']
        second_name = request.form['second_name']
        phone = request.form['phone']
        email = request.form['email']
        contacts = Contacts(first_name=first_name, second_name=second_name, phone=phone,
                            email=email)
        try:
            db.session.add(contacts)
            db.session.commit()
            return redirect('/view')
        except:
            return "Some error occurs"
    else:
        return render_template('add_contact.html')


@app.route('/view')
def view():
    show_info = Contacts.query.order_by(Contacts.date.desc()).all()
    return render_template('view.html', show_info=show_info)


@app.route('/view/<int:id>')
def view_details(id):
    show_info_details = Contacts.query.get(id)
    return render_template('view_details.html', show_info_details=show_info_details)


@app.route('/view/<int:id>/del')
def view_delete(id):
    show_info_details = Contacts.query.get_or_404(id)

    try:
        db.session.delete(show_info_details)
        db.session.commit()
        return redirect("/view")
    except:
        return "Error !"


if __name__ == '__main__':
    app.run(debug=True)
