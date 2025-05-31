# 1. read in all records from starter-records.json
# 2. for each record create a new record for each genre WITH movie title
# 3. for each record create a new reocrd for each review WITH movie title
import json


def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


file_contents = read_json_file("starter-records.json")

# print(f"Total Records: {len(file_contents['records'])}")

junction_table = []

for record in file_contents["records"]:
    movie_title = record["title"]

    movie_dict = {"title": movie_title, "genres": [], "ratings": []}

    for genre in record["genres"]:
        junction_table.append({"genre": genre["name"], "movie_title": movie_title})

    for rating in record["ratings"]:
        junction_table.append(
            {
                "reviewer": rating["reviewer"],
                "score": rating["rating"],
                "movie_title": movie_title,
            }
        )

with open("junction_table.json", "w") as file:
    json.dump({"records": junction_table}, file, indent=4)

print(len(junction_table))
