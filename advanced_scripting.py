import os
import json
import shutil
from subprocess import PIPE, run
import sys

GAME_DIR_PATTERN = "_game"
GAME_CODE_EXTENSION = ".go"
GAME_COMPILE_COMMAND = ["go", "build"]
def find_all_game_paths(source):
    game_paths = []
    for root, dirs, files in os.walk(source):
        for dir in dirs:
            if GAME_DIR_PATTERN in dir.lower():
                game_paths.append(os.path.join(source, dir))
                

        break
    return game_paths

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def get_name_from_path(paths, to_strip):
    new_names = []
    for path in paths:
        _, dir_name = os.path.split(path)
        new_dir_name = dir_name.replace(to_strip, "")
        new_names.append(new_dir_name)
    return new_names
def copy_and_overwrite(source, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(source, dest)

def make_json_metadata_file(path, game_dirs):
    data ={
        "gameNames": game_dirs,
        "numberOfGames": len(game_dirs)
    }
    with open(path, "w") as f:
        json.dump(data, f)

def compile_game_code(path):
    code_file_name = None
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(GAME_CODE_EXTENSION):
                code_file_name = file
                break
        break
    if code_file_name == None:
        return
    command = GAME_COMPILE_COMMAND + [code_file_name]
    run_command(command, path)
def run_command(command, path):
    cwd = os.getcwd()
    os.chdir(path)
    result= run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)
    print("compile result", result)
    os.chdir(cwd)

def main(source, target):
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)
    game_paths = find_all_game_paths(source_path)
    print(game_paths)
    new_game_dirs = get_name_from_path(game_paths, GAME_DIR_PATTERN)
    print(new_game_dirs)
    create_dir(target_path)
    for src, dest in zip(game_paths, new_game_dirs):
        dest_path = os.path.join(target_path, dest)
        copy_and_overwrite(src, dest_path)
        compile_game_code(dest_path)
    jsonpath = os.path.join(target_path, "metadata.json")
    make_json_metadata_file(jsonpath, new_game_dirs)
    



if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must have a source and a target directory")
    source, target = args[1], args[2]
    main(source, target)
