import json


# Read and parse the JSON file
def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


# Example usage
file_path = "starter-records.json"
fileContents = read_json_file(file_path)


def format_movie_insertions():
    print("INSERT INTO movie (title, year, rated) VALUES")
    for record in fileContents["records"]:
        print(f'("{record["title"]}", {record["year"]}, "{record["rated"]}"),')


def is_genre_known(current_unique_genre, genre_name):
    for genre in current_unique_genre:
        if genre["name"] == genre_name:
            return True
    return False


def format_genre_insertions():
    unique_genres = []

    for record in fileContents["records"]:
        for genre_record in record["genres"]:
            genre_known = is_genre_known(unique_genres, genre_record["name"])

            if not genre_known:
                unique_genres.append(
                    {"name": genre_record["name"], "level": genre_record["level"]}
                )

    for genre in unique_genres:
        print(f'("{genre["name"]}", {genre["level"]}),')

    print(f"\ntotal genre records {len(unique_genres)}")


# format_movie_insertions()
# format_genre_insertions()

print(fileContents["records"][3])

# print the number of records in the json file
print(f"\nTotal Records: {len(fileContents['records'])}")
