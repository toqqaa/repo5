ultralytics==8.0.23
import os


def replace_text_in_file(file_path, old_text, new_text):
    with open(file_path, "r", encoding="utf-8") as file:
        file_content = file.read()

    updated_content = file_content.replace(old_text, new_text)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(updated_content)


def process_text_files(folder_path, old_text, new_text):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            replace_text_in_file(file_path, old_text, new_text)


# Specify the folder path and the texts to replace
folder_path = r"D:\Lecturs\Machine Vision\Machine_vision_code\OIDv4_ToolKit-master\OID\Dataset\train\Human body\Labels\train"
old_text_to_replace = "Human body"
new_text = "0"

# Call the function to replace text in all text files in the specified folder
process_text_files(folder_path, old_text_to_replace, new_text)
