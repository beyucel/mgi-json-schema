#! /usr/bin/env python
import argparse
import json
import os
import pathlib
import jsonref

parser = argparse.ArgumentParser()
parser.add_argument("file", nargs='+')
args = vars(parser.parse_args())

out_directory = os.getcwd()+"/dereferenced-schemas/"
base_uri = pathlib.PurePosixPath(os.getcwd()).as_uri() + os.sep

for file_name_in in args['file']:
    file_name_out = out_directory + file_name_in
    with open(file_name_in) as f:
        json_data_in = json.load(f)
    json_data_out = jsonref.JsonRef.replace_refs(json_data_in, base_uri=base_uri)
    with open(file_name_out, mode='w+') as f:
        f.write(u'%s' % json.dumps(json_data_out,indent=4,separators=(',', ': ')))