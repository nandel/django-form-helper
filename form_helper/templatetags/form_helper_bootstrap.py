"""
Shortcut to use Bootstrap Forms
"""
from django import template
from django.template import Context, loader
import form_helper

register = template.Library()

# ---------------------------------------------------------
# DEFAULT RENDER FUNCTONS TO WORK AUTOMATIC WITH BOOTSTRAP
# ---------------------------------------------------------

@register.filter
def render(form, style=None):
	"""
	Render the form with bootstrap
	"""
	template = 'bootstrap'
	if style:
		template = template + '-' + style

	return form_helper.render(form, 'form_helper/' + template + '/form.html')

# ---------------------------------------------------------

@register.filter
def render_fields(form, style=None):
	"""
	Render the Field with bootstrap
	"""
	template = 'bootstrap'
	if style:
		template = template + '-' + style

	return form_helper.render_fields(form, 'form_helper/' + template + '/form-fields.html')

# ---------------------------------------------------------

@register.filter
def render_field(field, style=None):
	"""
	Render a especified field with bootstrap
	"""
	template = 'bootstrap'
	if style:
		template = template + '-' + style

	try:
		field_classes = field.field.widget.attrs.get('class', '')
		field_classes += ' form-control'
		field.field.widget.attrs['class'] = field_classes
	except:
		pass

	return form_helper.render_field(field, 'form_helper/' + template + '/field-auto.html')

# ---------------------------------------------------------
# Functions to use with Prepend style of bootstrap
# ---------------------------------------------------------

@register.simple_tag
def field_prepend_super(name, label, prepend=None, input=None, value=None, default=None, style=None, help_text=None, errors=None):
	"""
	Output a field with a prepend accord to the parameters
	Can pass the input
	"""
	template = 'bootstrap'
	if style:
		template = template + '-' + style

	tmplt = loader.get_template('form_helper/' + template + '/field-with-prepend.html')
	context = Context({
		'name' : name,
		'label' : label,
		'value' : value,
		'default' : default,
		'help_text' : help_text,
		'errors' : errors,
		'prepend' : prepend,
		'input' : input
	})
	return tmplt.render(context)

# ---------------------------------------------------------

@register.simple_tag
def field_prepend(name, label, prepend=None, value=None, default=None, style=None, help_text=None, errors=None):
	"""
	Output a field with prepend accord to the parameters
	"""
	return field_prepend_super(name, label, prepend, None, value, default, style, help_text, errors)

# ---------------------------------------------------------

@register.simple_tag
def field_prepend_email(name, label, value=None, default=None, style=None, help_text=None, errors=None):
	"""
	Output a field with a prepend for email fields
	"""
	prepend = '<i class="glyphicon glyphicon-envelope"></i>'
	return field_prepend(name, label, prepend, value, default, style, help_text, errors)

# ---------------------------------------------------------

@register.simple_tag
def field_prepend_password(name, label, style=None, help_text=None, errors=None):
	"""
	Output a field with a prepend for pasword fields
	"""
	input = '<input type="password" class="form-control" id="id_' + name + '" name="' + name + '" placeholder="' + label +'">'
	prepend = '<i class="glyphicon glyphicon-lock"></i>'
	return field_prepend_super(name, label, prepend, input, None, None, style, help_text, errors)
