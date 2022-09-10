from flask import Blueprint, render_template, url_for, redirect, flash, request


blueprint = Blueprint('admin_login', __name__)


@blueprint.route('/admin/user/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')