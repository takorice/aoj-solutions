import glob
import os
import re
import subprocess
import sys


def renameFiles(problem_id):
    print("1. remove sample files")
    for index, path in enumerate(glob.glob("./{}/sample*".format(problem_id))):
        print("remove {}".format(path))
        os.remove(path)
    print("2. rename aoj I/O files")
    for index, path in enumerate(glob.glob("./{}/*.txt".format(problem_id))):
        renamed_path = re.sub(
            '/([a-z]+)_(\d+).txt', '/sample\\2.\\1.txt', path
        )
        os.rename(path, renamed_path)
        print("{0} -> {1}".format(path, renamed_path))


if __name__ == '__main__':
    problem_id = sys.argv[1]

    print("---- Run aoj-cli ----")
    subprocess.run(
        ["aoj", "gen", problem_id]
    )
    print("---- Run contest-cli ----")
    subprocess.run(
        ["contest-cli", "new", problem_id]
    )
    print("---- Test I/O files setting ----")
    renameFiles(problem_id)
