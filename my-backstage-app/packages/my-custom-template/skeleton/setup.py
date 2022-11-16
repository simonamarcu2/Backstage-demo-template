from distutils.core import setup

setup(name='${{ values.component_id }}',
      version='1.0',
      description='${{ vales.description }}',
      author='${{ values.authorEmail }}',
      {% if values.authorEmail %}
      author_email='${{ values.authorEmail }}',
      It is true
      {% endif %}
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['${{ values.component_id }}'],
     )
