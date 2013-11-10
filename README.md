django-form-helper
==================
django-form-helper is a tool to render forms using bootstrap while developping with django

install:
  Add in your instaled apps:
    <code>INSTALED_APPS += ('form_helper',);</code>

usage:
<code>
{% load form_helper_bootstrap %}

<fieldset>
	<legend>Info</legend>
	{{ form.title_field|render_field:"horizontal" }}	
	{{ form.date_field|render_field:"horizontal" }}	
	{{ form.text_field|render_field:"horizontal" }}	
</fieldset>
</code>
