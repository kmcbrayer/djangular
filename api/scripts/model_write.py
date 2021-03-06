#model changeing script:
import json, re

def build_model_strings(json):
	model_string = "import models\n\n"
	for model in json:
		model_string+=build_model_string(model)
	return model_string

def build_model_string(json):
	model_string = "class "+json['name'].title()+"(models.Model):\n\t"
	for value in json['values']:
		model_string = model_string+value['name']+" = "+build_model_field(value)

	return model_string+"\n"

def build_model_field(field):
	field_string = "models."
	if field['type'] == "Number":
		field_string=field_string+"DecimalField(max_didgets=5,decimal_places=2)"
	elif field['type'] == "boolean":
		field_string=field_string+"BooleanField()"
	else:
		field_string=field_string+"CharField(max_length=200)"
	field_string+="\n\t"
	return field_string

def write_models_to_file(string): 
	with open('cpy.py','w+') as models_py:
		models_py.write(string)

#read json file
#json_file needs to be args[0]
with open('json_file.json', 'r') as jsn:
	write_models_to_file(build_model_strings(json.load(jsn)))