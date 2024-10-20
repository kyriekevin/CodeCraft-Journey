import os
import re
from collections import defaultdict


def count_problems(directory):
    count = defaultdict(lambda: defaultdict(int))
    for root, _, files in os.walk(directory):
        if "solution" in "".join(files):
            parts = root.split(os.sep)
            if len(parts) >= 3:
                platform = parts[1]
                category = parts[2]
                count[platform][category] += 1
                count[platform]["total"] += 1

    return count


def update_readme(stats):
    with open("README.md", "r") as file:
        content = file.read()

    # Total problems solved
    tot_problems = sum(stats[platform]["total"] for platform in stats)
    content = re.sub(
        r"(<!-- STATS:TOTAL_PROBLEMS -->)[\s\S]*?(<!-- STATS:TOTAL_PROBLEMS:END -->)",
        r"\1\n- Total problems solved: {}\n\2".format(tot_problems),
        content,
    )

    # LeetCode stats
    leetcode_stats = "- Easy: {}\n- Medium: {}\n- Hard: {}".format(
        stats["LeetCode"]["Easy"],
        stats["LeetCode"]["Medium"],
        stats["LeetCode"]["Hard"],
    )
    content = re.sub(
        r"(<!-- STATS:LEETCODE -->)[\s\S]*?(<!-- STATS:LEETCODE:END -->)",
        r"\1\n{}\n\2".format(leetcode_stats),
        content,
    )

    with open("README.md", "w") as file:
        file.write(content)


if __name__ == "__main__":
    stats = count_problems(".")
    update_readme(stats)
