import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    with open(input_file_name) as f:
        reader = csv.reader(f)
        # This ensures that no additional newlines are inserted between rows.
        with open(output_file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            Data = OrderedDict()
            for number in range(1000, 10000):
                number_bytes = str(number).encode('utf-8')
                Data[number] = hashlib.sha256(number_bytes).hexdigest()

            for row in reader:
                name = row[0]
                desired_hash = row[1]
                for key, value in Data.items():
                    if value == desired_hash:
                        writer.writerow([name, key])