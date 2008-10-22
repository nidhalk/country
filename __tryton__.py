#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
{
    "name" : "Country",
    "version" : "0.1",
    "author" : "B2CK",
    'email': 'info@b2ck.com',
    'website': 'http://www.tryton.org/',
    "category" : "Generic",
    "description": "Define countries and subdivisions.",
    "depends" : ["ir", "res"],
    "xml" : [
        "country.xml",
    ],
    'translation': [
        'fr_FR.csv',
        'de_DE.csv',
        'es_ES.csv',
   ],
}