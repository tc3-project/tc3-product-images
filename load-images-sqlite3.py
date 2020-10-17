# load-images-sqlite3.py
# Copyright © 2020 Joel A. Mussman. All rights reserved.
#
# Invoke this as "python load-images.sqlite3.py <path_to_sqlite3_database_file>" in this project folder.
#
# This module will create the product_images table in the database and load it with the images. The script is
# designed to run in this folder and find the images in the sub-folders "images-large-by-product-id" and
# "images-small-by-product-id".
#
# The product_images table primary key is constructed from the product_id (foreign to the products table) and
# the type of image, small or large.
#

import sys
from os import walk
import re
import sqlite3

def closeDatabase(sqliteConnection):
    if sqliteConnection:
        sqliteConnection.commit()
        sqliteConnection.close()
    print("Closed sqlite3 database")

def createProductImagesTable(cursor):
    sqlite_drop_table_query = "DROP TABLE IF EXISTS product_images;"
    cursor.execute(sqlite_drop_table_query)
    sqlite_create_table_query = """CREATE TABLE product_images (
                                    product_id INTEGER REFERENCES products(product_id) NOT NULL,
                                    small_image BOOLEAN NOT NULL,
                                    image BLOB,
                                    PRIMARY KEY (
                                       product_id,
                                       small_image
                                    )
                                );"""
    cursor.execute(sqlite_create_table_query)
    print("Created product_images table")

def insertBLOB(cursor, product_id, fileData, small_image):
    sqlite_insert_blob_query = """ INSERT INTO product_images
                              (product_id, image, small_image) VALUES (?, ?, ?)"""
    cursor.execute(sqlite_insert_blob_query, (product_id, fileData, small_image))
    print("Image and file inserted successfully as a BLOB into a table")

def loadBinaryData(filename):
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def openDatabase(filename):
    sqliteConnection = sqlite3.connect(filename)
    cursor = sqliteConnection.cursor()
    print("Connected to SQLite")
    return (sqliteConnection, cursor)

def loadImages(folder, small_image, cursor):
    for (dirpath, dirnames, filenames) in walk(folder):
        for filename in filenames:
            product_id = re.search('\d+', filename)[0]
            path = folder + "/" + filename;
            print("Inserting", "small" if small_image else "large", "image for", product_id, "from", path)
            insertBLOB(cursor, product_id, loadBinaryData(path), small_image)

def main():
    try:
        print(sys.argv[1]);
        (sqliteConnection, cursor) = openDatabase(sys.argv[1])
        createProductImagesTable(cursor)
        loadImages("./images-large-by-product-id", False, cursor)
        loadImages("./images-small-by-product-id", True, cursor)

    except sqlite3.Error as error:
        print(error)

    finally:
        closeDatabase(sqliteConnection)

main()