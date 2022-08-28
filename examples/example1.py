import os.path
import sys

sys.path.append("./")
from dot_json import describe_json_file

FILE_PATH = "examples/files/sample_json_file.json"


def main():
    file_path = os.path.abspath(FILE_PATH)
    result = describe_json_file(file_path)
    print(result)


if __name__ == "__main__":
    main()
