from flask import Blueprint

from app.libs.redprint import Redprint

api = Redprint('book')

@api.route('/get',methods=['GET','POST'])
def get_book():
    return 'get book'
