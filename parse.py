import re
import json

def parse(input_file, source):
    with open(input_file) as f:
        results = []
        indent_size = 0
        desc = ""
        title = ""
        for line in f:
            if re.match("\d+. +\w", line):
                desc = ""
                indent_size = len(re.match("\d+. +", line).group(0))
                title = re.match("\d+. +(.+)", line).group(1)
            else:
                if indent_size > 0 and re.match(" " * indent_size + "\w", line):
                    desc = desc + line.strip() + "\n"
                elif indent_size > 0:
                    indent_size = -1
                    results.append({
                        "title" : title,
                        "description": desc,
                        "source": source
                    })

    return results

#results = parse("data/18254.txt", "source")




