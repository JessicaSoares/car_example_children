from flask import render_template, request, redirect, url_for, flash
from app import app, db 
from app.models import Car, Part, add_or_check_car

@app.route('/', methods=['GET', 'POST'])
def submit_data():
    if request.method == 'POST':
        car_name = request.form.get('car_name')
        parts_names = request.form.getlist('part_name')
        parts_prices = request.form.getlist('part_price')
        parts_list = list(zip(parts_names, map(int, parts_prices)))
        message = add_or_check_car(db.session, car_name, parts_list)
        flash(message, 'info')
        return redirect(url_for('submit_data'))
    return render_template('index.html')
