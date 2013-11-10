Django Form helper
==================
django-form-helper is a tool to render forms using bootstrap3 while developping with django

Install
-----
Add ``form_helper`` in your ``INSTALLED_APPS``::

	INSTALLED_APPS = (
	...
	'form_helper',
	)
	

Usage
------
In your template use this syntax::

      {% load form_helper_bootstrap %}
      <fieldset>
        <legend>Info</legend>
        {{ form.title_field|render_field:"horizontal" }}	
        {{ form.date_field|render_field:"horizontal" }}	
        {{ form.text_field|render_field:"horizontal" }}	
      </fieldset>


