
# /utils/db.py - Beylog
#
# Copyright (c) 2006 beyking@gmail.com
# Distributed under the GPL License (See http://www.gnu.org/copyleft/gpl.html)
#



from django.contrib.contenttypes.models import ContentType


# Caches of content types/models class
_model_class_cache = {}
_content_type_cache = {}




def get_content_type_id(model_class):
    """Gets a content type id for a given model"""
    try:
        return _content_type_cache[model_class]
    except:
        ct_id = ContentType.objects.get_for_model(model_class).id
        _model_class_cache[ct_id] = model_class
        _content_type_cache[model_class] = ct_id
        return ct_id


def get_model_class(content_type_id):
    """Gets a model class for a given content_type_id"""
    try:
        return _model_class_cache[content_type_id]
    except KeyError:
        #if content_type_id is not exist that will raise a ContentType.DoesNotExist exception 
        ct = ContentType.objects.get(pk=content_type_id)
        mc = ct.model_class()
        _model_class_cache[content_type_id] = mc
        _content_type_cache[mc] = content_type_id
        return mc


def get_object(pk, content_type_id):
    """Gets an object with (content type id and a primary key value) """
    return get_model_class(content_type_id)._default_manager.get(pk=pk)