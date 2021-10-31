import yaml
from yaml import CLoader as Loader
from cerberus import Validator



def _load_doc(yamlPath):
    with open(yamlPath, 'r') as stream:
        try:
            return yaml.load(stream, Loader=Loader)
        except yaml.YAMLError as exception:
            raise exception

def checker(schema, yamlPath):
    #schema = eval(open('./schema.py', 'r').read())
    v = Validator(schema)
    doc = _load_doc(yamlPath)
    correctness = ""
    if v.validate(doc, schema):
        correctness = "Your answer is correct!"
    else:
        correctness = "Your answer was not correct. Please try again."

    print("IS VALID: ", correctness)
    print("ERRORS: ", v.errors)