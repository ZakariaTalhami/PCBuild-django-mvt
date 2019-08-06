import os
import json
from django.db.utils import IntegrityError

def import_model(model_name: str):
    components = model_name.split('.')
    model = __import__(components[0])
    for comp in components[1:]:
        model = getattr(model, comp)
    return model;

def json_to_objects(json_url: str):
    """
    Parameters
    ----------
    json_url: str
        The URL for the json file
    
    Returns
    -------
    list
        A list of a generated objects

    """
    if not os.path.exists(json_url):
        raise FileNotFoundError("Provided JSON file does not exist")
    with open(json_url, 'r') as json_file:
        try:
            configurations = json.load(json_file)
        except json.JSONDecodeError:
            raise json.JSONDecodeError()
        
        objects = []
        for config in configurations:
            if not all(key in config for key in ['class' , 'data']):
                raise KeyError("JSON doesnt contain both 'class' and 'data' fields")
            model = import_model(config['class'])
            for data in config['data']:
                instance = model()
                for key, value in data.items():
                    if isinstance(value, dict):
                        temp_model = import_model(value['class'])
                        value = temp_model.objects.get(pk=value['pk'])
                    setattr(instance, key, value)
                try:
                    instance.save()
                    objects.append(instance)
                except IntegrityError:
                    raise InterruptedError("Provided JSON has some missing properties")
        return objects
    
            
            



