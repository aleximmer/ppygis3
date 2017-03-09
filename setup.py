"""PPyGIS

Copyright (c) 2011, Bartosz Fabianowski <bartosz@fabianowski.eu>
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of the author nor the names of its contributors may be used
  to endorse or promote products derived from this software without specific
  prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

$Id: setup.py 5 2011-04-13 16:17:20Z plush $
"""
import distutils.core

version='0.2'

long_description = """\
'PPyGIS is an extension to Psycopg_, a PostgreSQL_ database adapter for the
Python_ programming language. PPyGIS adds support for the geometry object
types used by PostGIS_.

PPyGIS has been tested with Python 2.7. It may work with earlier versions as
well. A Python 3 version does not currently exist.

.. _Psycopg: http://initd.org/psycopg/
.. _PostgreSQL: http://www.postgresql.org/
.. _Python: http://www.python.org/
.. _PostGIS: http://postgis.refractions.net/'
"""

distutils.core.setup(
    name='PPyGIS',
    version=version,
    description='PostGIS adapter for Psycopg',
    long_description=long_description,
    author='Bartosz Fabianowski',
    author_email='bartosz@fabianowski.eu',
    url='http://www.fabianowski.eu/projects/ppygis/',
    download_url=
      'http://www.fabianowski.eu/projects/ppygis/releases/' + \
      'PPyGIS-' + version + '.tar.gz',
    packages=[''],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Topic :: Database :: Front-Ends',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules'],
    keywords=['psycopg', 'postgis', 'geometry', 'EWKB'],
    package_dir={'': 'src'})
