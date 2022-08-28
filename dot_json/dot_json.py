import os.path
import json

import magic


def verify_json_file(file_path):
    if os.path.exists(file_path):
        mime = magic.Magic(mime=True)
        mime_type = mime.from_file(file_path)
        if mime_type == "application/json":
            return True
        else:
            print("Not a valid json file")
    else:
        print("File does not exist.")
    return False


def describe_file_content(file_content):
    description = {"type": type(file_content).__name__}
    if isinstance(file_content, dict):
        description["length"] = len(file_content)
        dict_description = {key: describe_file_content(value) for key, value in file_content.items()}

        description["keys"] = dict_description
    elif isinstance(file_content, list):
        description["length"] = len(file_content)
        for data in file_content:
            description["items"] = describe_file_content(data)
    elif isinstance(file_content, str):
        description["length"] = len(file_content)
    else:
        description["type"] = type(file_content).__name__
    return description


def _get_human_readable_size(file_path):
    size_in_bytes = os.path.getsize(file_path)
    if size_in_bytes > (1024 * 1024 * 1024):
        size = size_in_bytes / (1024 * 1024 * 1024), "GB"
    elif size_in_bytes > (1024 * 1034):
        size = size_in_bytes / (1024 * 1024), "MB"
    elif size_in_bytes > 1024:
        size = size_in_bytes / 1024, "KB"
    else:
        size = size_in_bytes, "Bytes"
    return f"{round(size[0], 2)} {size[1]}"


def get_file_stat(file_path):
    return {"name": file_path.split("/")[-1], "size": _get_human_readable_size(file_path)}


def describe_json_file(file_path) -> dict:
    file_is_valid = verify_json_file(file_path)
    if not file_is_valid:
        return {}

    with open(file_path) as json_file:
        try:
            file_content = json.load(json_file)
            description = describe_file_content(file_content)
        except json.decoder.JSONDecodeError as e:
            print(e)
            return {}

    return {"file_info": get_file_stat(file_path), "description": description}
