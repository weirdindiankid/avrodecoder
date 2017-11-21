# Filename: avro2json.py
# Author: Dharmesh Tarapore <dharmesh@bu.edu>
# Description: Convert avro data files to JSON files
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter
from avro_json_serializer import *

schema_dict = {
  "name": "ModeSEncodedMessage",
  "type": "record",
  "namespace": "org.opensky.avro.v2",
  "fields": [
      {"name": "sensorType",          "type": "string"},
      {"name": "sensorLatitude",      "type": ["double", "null"]},
      {"name": "sensorLongitude",     "type": ["double", "null"]},
      {"name": "sensorAltitude",        "type": ["double", "null"]},
      {"name": "timeAtServer",      "type": "double"},
      {"name": "timeAtSensor",      "type": ["double", "null"]},
      {"name": "timestamp",         "type": ["double", "null"]},
      {"name": "rawMessage",        "type": "string"},
      {"name": "sensorSerialNumber",    "type": "int"},
      {"name": "RSSIPacket",        "type": ["double", "null"]},
      {"name": "RSSIPreamble",        "type": ["double", "null"]},
      {"name": "SNR",           "type": ["double", "null"]},
      {"name": "confidence",        "type": ["double", "null"]}
  ]
}

avro_schema = avro.schema.make_avsc_object(schema_dict, avro.schema.Names())

serializer = AvroJsonSerializer(avro_schema)

FILENAME = './foo.avro'

reader = DataFileReader(open(FILENAME, "rb"), DatumReader())

data = []

for i in reader:  
  json_str = serializer.to_json(i)

  data.append(json_str)

with open('temp.json', 'w') as f:
  for i in data:
    f.write(i)
    f.write('&')
  #f.write(str(data))
  f.close()
