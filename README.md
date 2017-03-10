## ppygis3
ppygis3 is a port of [PPyGIS](https://pypi.python.org/pypi/PPyGIS/0.2) that works in Python>=3.
PPyGIS is an extension for psycopg2. PPyGIS adds support for PostGIS geometry objects by
translating them between PostGIS EWKB representation and python objects.

### Installation
```
pip install ppygis3
```

### Usage
The module can be used exactly as described in the documentation of PPyGIS for Python2.
Simply use a different import statement, `ppygis3` instead of `PPyGIS`.
The PPyGIS documentation can be found [**here**](http://www.fabianowski.eu/projects/ppygis/)

#### Basic Usage (Read, Write)
Adapted from [the original documentation](http://www.fabianowski.eu/projects/ppygis/). By extending the `psycopg2` module, geometry objects will be
automatically serialized when inserting and transformed to python objects
when loading.

```python
import psycopg2
from ppygis3 import Point, LineString, Geometry

# Connect to an existing spatially enabled database
connection = psycopg2.connect(database='test', user = 'test')
cursor = connection.cursor()

cursor.execute('CREATE TABLE test(geometry GEOMETRY)')

# Insert a point into the table
cursor.execute('INSERT INTO test VALUES(%s)', (Point(1.0, 2.0),))

# Retrieve the point from the table and print it
cursor.execute('SELECT * FROM test')
point = cursor.fetchone()[0]
print(point)

# Create a line and insert it into the table
geometry = LineString((point, Point(4.0, 5.0, 6.0)))
cursor.execute('INSERT INTO test VALUES(%s)', (geometry,))

# Retrieve the table contents and print it
cursor.execute('SELECT * FROM test')
for row in cursor:
    print(row[0])

# Disconnect from the database
cursor.close()
connection.close()
```

#### COPY FROM/TO

`COPY FROM` and `TO` allow for bulk uploads and downloads. The following shows example usage of this functionality.

```python
import psycopg2
from ppygis3 import Point, LineString, Geometry
from io import BytesIO

# Connect to an existing spatially enabled database
connection = psycopg2.connect(database='test', user = 'test')
cursor = connection.cursor()

cursor.execute('CREATE TABLE test(geometry GEOMETRY)')

buffer = BytesIO()
buffer.write(Point(1.0, 2.0).write_ewkb() + b'\n')
buffer.write(LineString((Point(1.0, 2.0), Point(3.0, 4.0))).write_ewkb() + b'\n')
buffer.seek(0)

# Perform a bulk upload of data to the table
cursor.copy_from(buffer, 'test')

# Retrieve the table contents and print it
cursor.execute('SELECT * FROM test')
for row in cursor:
    print(row[0])

# Perform a bulk download of data from the table
buffer = BytesIO()
cursor.copy_to(buffer, 'test')
buffer.seek(0)

# Print the data
for line in buffer:
    print(Geometry.read_ewkb(line.strip()))

# Disconnect from the database
    cursor.close()
    connection.close()
```
