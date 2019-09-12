from flask import request

def form_get(field) :
    return request.form.get(field, "")