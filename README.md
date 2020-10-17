# The Caribbean Coffee Company ![](./.common/logo.png?raw=true)
by Joel Mussman<br/>
original project concept by Joel Mussman and Justin Poole 

The Caribbean Coffee Company (TC3) is a cafe-operations project that was developed as the basis for demonstrations
and classwork for almost every software development technology that you can work with, from databases through devices.
All participants can identify with the cafe scenario and have a feel for how it must work.
The core environment is kept simple: products, employees, and customers.
<br>
<br>

# TC3-Product-Images

## History

2020-10-16 - Bundled the product images into this separate project.

## Overview

This project contains the source and edited product images for the products defined in the sample data (see
any of the database projects). The sources for these images have been carefully selected so that they may be
included in a demonstration or course lab, even if used in a commercial setting.
See the [image attribution spreadsheet](image-attribution.xlsx) for the provenance of each graphic.

## Project Setup

These images may be added to the assets of a web project for serving the files directly to a client, or they
may be inserted as BLOB data into the database and served through queries.

The images are organized in three folders: *images-by-name* contains all of the product images by name,
*images-large-by-product-id* holds all the large images (500x500) named by product id, and
*images-small-by-product-id* has all the small images (150x150).
Copy the files you want to use to appropriate asset folders in a web service or web application.
These product ids match the product ids from the sample data loaded in the databases.

There are Python 3 script files in this project to add the BLOB data to different types of databases using
the product ids as the primary key.
Execute the python scripts in the form "python load-images-sqlite3.py \<path to SQLite3 database\>" inside of
this project folder (the image locations are hard-wired).

## Related Projects

Look at the TC3 database projects.

## License

The project code (the Python scripts) is licensed under the [MIT license](./.common/LICENSE.md).

The images are provided under various licenses from their sources.
They have been carefully selected so that they may be included in examples or course labs without worry, even
if used in a commercial setting.
See the image attribution spreadsheet for the provenance of each graphic, and the license requirements that
you may have to follow when you use them.
Adobe Photoshop copies of the original images have been placed in the *original-images* folder and
are redistributed under their original licenses.

Some product images have been constructed from original images as a base.
All of the images have been altered with a circular border for a consistent format across
all of the TC3 products.
All of the images have been modified under the terms of their respective licenses.

Sources for the altered images are in the folder *original-altered*.
Altered images must be released under the same or an equivalent license, and these altered images are released under
their respective licenses.

Make sure that you provide the correct attribution in any project where you use these, along with
attribution to this project.

## Project Details

This is part of of the larger Caribbean Coffee Company suite of components using different technologies and programming languages that fit into the TC3 project.
Learn more at [https://gitlab.com/tc3-project](https://gitlab.com/tc3-project).

## Support

If you found this project helpful, and and you would like to see more free projects like this,
then please consider
a contribution to *Joel's Coffee Fund* at **Smallrock Internet** to help keep the good stuff coming :)<br />

[![Donate](./.common/Donate-Paypal.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=XPUGVGZZ8RUAA)

<hr>
Copyright © 2019-2020 Joel A Mussman. All rights reserved.