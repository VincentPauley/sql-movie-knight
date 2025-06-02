import json


def read_json_file(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        return data
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None


genre_ids = [
    ["06b60879-1327-48f1-82ca-76deee936203", "Fantasy"],
    ["0a2e1786-e3b5-43b3-a116-6f405b270b9d", "Satire"],
    ["0f3713c6-84ec-48d2-a14b-b6a20796f576", "Drama"],
    ["1629939b-055e-452f-8336-e38e8210d7ad", "Action"],
    ["1da308b2-7bdc-4327-ae38-d1b38952097f", "Disaster"],
    ["3a906625-ee25-46a1-916f-1b407532e2ad", "Family"],
    ["3e715bce-a53c-4ae5-aec5-f4d9ecbef458", "Slasher"],
    ["4592ca1b-3787-4796-baf2-9a89ff5cc0ba", "Monster"],
    ["4733699b-d1ed-410f-afa7-eadd3972de35", "Teen"],
    ["4ea7b728-07a5-4488-ac74-92e9fbf8387f", "Adventure"],
    ["6195989e-edcb-4146-a8d2-f13d671c37d0", "Coming of Age"],
    ["6f240a94-3e2e-4835-a163-1e39b1e0f57a", "Noir"],
    ["730d012e-7c9d-449e-9b08-b028cc8f9d3a", "Raunchy"],
    ["75690588-adff-48e1-ae49-1c7d6de8a3be", "Biographical"],
    ["7621b34b-f354-4e86-9ed3-23e1d1c5497b", "Western"],
    ["7db6eb86-15c1-48d4-ad44-0b59f6b8f272", "Historical"],
    ["8882caf7-6992-480f-9749-16317afbceaa", "Musical"],
    ["88c18939-389d-485c-8b25-9150c7a4b321", "Thriller"],
    ["94d1a3af-4a88-4765-8396-ef35429df398", "Cars/Racing"],
    ["a1c2245a-b9dd-4e26-b296-4120f2f1981d", "Mystery"],
    ["adbf8775-cc9c-4ca7-9b9a-ff55e031c47a", "Survival"],
    ["ba07b109-4d2e-46fd-8598-274526b30b4c", "Epic"],
    ["bf23cda5-e34e-4b01-bcb2-8424118d5de9", "Sports"],
    ["c433f828-aed8-4ee9-84c7-7b9da608b93d", "Spy"],
    ["c9de397a-a370-4a25-9d53-a63b3d4dc23b", "Kids"],
    ["cea933f8-adad-433d-b88e-8c04769fc4d4", "War"],
    ["d80badaf-38ac-4ae4-a1ae-223d9d390089", "Light-Hearted"],
    ["d95b256c-3abc-4fcd-a35d-16281ac3cb29", "Romance"],
    ["df3d5d58-9be9-4f8c-ad86-2288ff13b9f1", "Comedy"],
    ["dfc2613c-376e-461e-ba43-22a4197ac2e6", "Crime"],
    ["e039c39e-a152-41bc-a648-cd09b901ff59", "Super Hero"],
    ["e21dd9bb-9659-4cd8-866e-06e5066c072d", "Dark Comedy"],
    ["e2ea5872-a4a3-49de-b21e-ab1401554278", "Romantic Comedy"],
    ["e48c8f03-322a-4b09-9f11-9d21b597282c", "Science Fiction"],
    ["ecd0345b-68c7-4500-a527-07cef9e55108", "Animation"],
    ["f937208d-1f44-44ba-a0f3-53fb577ba590", "Horror"],
]

junction_contents = read_json_file("junction_table-2.json")

print(f"Total Records: {len(junction_contents['records'])}")

genre_records = 0

expanded_records = []

for record in junction_contents["records"]:
    if "genre" in record:
        genre_records = genre_records + 1
        # print(record)

        genre_match = None

        for genre_id in genre_ids:
            if record["genre"] == genre_id[1]:
                genre_match = genre_id[0]
                # print(genre_id[1])

        expanded_records.append({**record, "genre_id": genre_match})

print(f"Total (Expanded) Records: {len(expanded_records)}")


with open("junction_table-3.json", "w") as file:
    json.dump({"records": expanded_records}, file, indent=4)
