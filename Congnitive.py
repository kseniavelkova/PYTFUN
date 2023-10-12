import os
import json
import hcl


cfn = [".json", ".template", ".yaml", ".yml"]
tf = ["tf"]
directory = 'C:\\Users\\Ksenia.Velkova\\PycharmProjects\\pythonProject'


def file_handler(directory):
    for root, dirs, files in os.walk(directory):
        for f in files:
            if f.endswith(tuple(cfn)):
                with open(os.path.join(root, f), 'r') as fin:
                    try:
                        f = fin.read()
                        if "key" in f:
                            dt = json.dumps(f)
                            print(dt)
                    except ValueError as e:
                        raise SystemExit(e)

            elif f.endswith(tuple(tf)):
                with open(os.path.join(root, f), 'r') as file:
                    try:
                        obj = hcl.load(f)
                        data = json.dumps(obj)
                        print(data)
                    except ValueError as e:
                        raise SystemExit(e)

    return dt
##https://stackoverflow.com/questions/47996294/python-refactor-this-function-to-reduce-its-cognitive-complexity-from-19-to-the
##file_handler(directory)
