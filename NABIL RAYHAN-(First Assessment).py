import os
import json

# Scenario 1: Convert JSON to the standard format
def convert_json(input_path, output_path):
    with open(input_path, 'r') as file:
        data = json.load(file)

    formatted_data = {
        "filename": os.path.basename(input_path).replace('.json', ''),
        "objects": []
    }

    if "vehicle" in data:
        formatted_data["objects"].append({
            "class": "car",
            "presence": data["vehicle"]
        })

    if "license plate" in data:
        formatted_data["objects"].append({
            "class": "number",
            "presence": data["license plate"]
        })

    with open(output_path, 'w') as file:
        json.dump(formatted_data, file, indent=4)

# Scenario 2: Combine and update class names
def combine_jsons(input_folder, output_path):
    combined_data = {"objects": []}

    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        with open(file_path, 'r') as file:
            data = json.load(file)

        for obj in data["objects"]:
            if obj["class"] == "vehicle":
                obj["class"] = "car"
            elif obj["class"] == "license plate":
                obj["class"] = "number"

        combined_data["objects"].extend(data["objects"])

    with open(output_path, 'w') as file:
        json.dump(combined_data, file, indent=4)

# Scenario 1: Convert JSON to the standard format
input_file = "pos_0.png.json"
output_file = "formatted_pos_0.png.json"
convert_json(input_file, output_file)

# Scenario 2: Combine and update class names
input_folder = "json_folder"
output_file = "combined_json.json"
combine_jsons(input_folder, output_file)
