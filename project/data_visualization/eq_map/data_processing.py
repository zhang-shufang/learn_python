from asyncore import read
import imp
from pathlib import Path
import json

# Read the data as string and convert to a python object
path = Path("eq_data/eq_data_1_day_m1.geojson")
contents = path.read_text()
all_eq_data = json.loads(contents)

# Convert the data to an easier to read vision
path = Path("eq_data/readable_eq_data4.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)
