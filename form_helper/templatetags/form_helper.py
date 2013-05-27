# -*- coding: utf-8 -*-
from django import template
from django.template import Context, loader

register = template.Library()

# ---------------------------------------------------------

@register.filter
def render(form, template=None):
	tmplt = loader.get_template(template)
	context = Context({
		'form': form,
		'method' : 'POST',
		'action' : '',
		'template' : template,
	})
	return tmplt.render(context)

# ---------------------------------------------------------

@register.filter
def render_fields(form, template=None):
	tmplt = loader.get_template(template)
	context = Context({
		'form': form,
		'method' : 'POST',
		'action' : '',
		'template' : template,
	})
	return tmplt.render(context)

# ---------------------------------------------------------

@register.filter
def render_field(field, template=None):
	tmplt = loader.get_template(template)
	context = Context({
		'field': field,
		'template' : template,
	})
	return tmplt.render(context)

# ---------------------------------------------------------

@register.simple_tag
def form_field(name, label, value=None, template=None, type="text", default=None, help_text=None, errors=None, classes=None):
	if not template:
		input_fields = ['text', 'password', 'color', 'date', 'datetime', 'datetime-local', 'email', 'file', 'hidden', 'image', 'month', 'number', 'range', 'search', 'tel', 'time', 'url', 'week']

		if type in input_fields:
			template = 'form_helper/field-types/input.html'
		elif type == 'checkbox' or type == 'radio' or type == 'textarea':
			template = 'form_helper/field-types/' + type + '.html'
		else:
			print "%s field have a invalid type." % (name)
			raise "%s field have a invalid type." % (name)

	tmplt = loader.get_template(template)
	context = Context({
		'name': name,
		'label': label,
		'value': value,
		'default': default,
		'type': type,
		'style': style,
		'help_text': help_text,
		'errors': errors,
		'classes' : classes
	})
	return tmplt.render(context)