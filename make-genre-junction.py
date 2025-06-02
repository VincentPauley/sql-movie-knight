import json


def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


contents = read_json_file("junction_table-3.json")

# VALUES
#     ("e48c8f03-322a-4b09-9f11-9d21b597282c", "Science Fiction", 1),

for record in contents["records"]:
    print(f'("{record["movie_id"]}", "{record["genre_id"]}"),')
