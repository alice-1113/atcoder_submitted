import os
import sys

dir_path = os.path.dirname(sys.argv[0])
dir_name = "abc{}"
diff = ["a", "b", "c"]
file = "{}.py"
for i in range(200, 300):
    mkdir_name = dir_name.format(i)
    if not os.path.exists(mkdir_name):
        os.mkdir(mkdir_name)
    for d in diff:
        path = os.path.join(mkdir_name, file.format(d))
        with open(path, "w", encoding="UTF-8") as f:
            pass