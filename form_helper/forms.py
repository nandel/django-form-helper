from django.template import Context, loader

class BaseForm(object):
	"""
	Abstract class to add some method to render the form as bootstrap_forms
	"""
	def as_template(self, template):
		"Returns this form fields rendered as Bootstrap form."
		tmplt = loader.get_template(template)
		context = Context({
			'form': self,
			})
		return tmplt.render(context)

class BaseBootstrap(BaseForm):
	"""
	Abstract class to add some method to render the form as Bootstrap
	"""
	def as_bootstrap(self):
		"Returns this form fields rendered as Bootstrap form."
		return self.as_template('form_helper/bootstrap/form-fields.html')

	def as_bootstrap_horizontal(self):
		"Returns this form fields rendered as Bootstrap form-horizontal."
		return self.as_template('form_helper/bootstrap-horizontal/form-fields.html')

	def as_bootstrap_inline(self):
		"Returns this form fields rendered as Bootstrap form-inline."
		return self.as_template('form_helper/bootstrap-inline/form-fields.html')