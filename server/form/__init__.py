from flask import request

def form_get(field) :
    return request.json.get(field, "")

def confirm_is_json():
    return request.is_json