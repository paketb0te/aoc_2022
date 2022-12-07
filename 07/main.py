from collections import defaultdict
from pprint import pprint
from typing import Callable

INPUT_FILE = "test_input.txt"
# INPUT_FILE = "input.txt"

MAX_SMALL_DIR_SIZE = 100000
SMALL_DIRS_SUM = 0


def node():
    return defaultdict(node)


ROOT = node()
CWD: list[str] = []


def get_cwd() -> defaultdict:
    node = ROOT
    for elem in CWD:
        node = node[elem]
    return node


###############################################################################
# COMMAND HANDLER FUNCTIONS
###############################################################################


def handle_cd(arg: str, **kwargs):
    if arg == "/":
        CWD.clear()
    elif arg == ".":
        pass
    elif arg == "..":
        CWD.pop()
    else:
        CWD.append(arg)


def handle_ls(output_lines: list[str], **kwargs):
    cwd = get_cwd()
    for line in output_lines:
        add_file_from_line(cwd=cwd, line=line)


CMD_MAP = {"cd": handle_cd, "ls": handle_ls}


def get_cmd_from_line(line: str) -> tuple[Callable, str]:
    lst = line.split(maxsplit=2)
    cmd_str = lst[1]
    try:
        arg_str = lst[2]
    except IndexError:
        arg_str = ""

    return CMD_MAP[cmd_str], arg_str


def add_file_from_line(cwd: defaultdict, line: str):
    size, name = tuple(line.split(maxsplit=1))
    # Add new node only if it does not exist yet.
    # This is to prevent changes when traversing a dir multiple times.
    if size == "dir" and name not in cwd:
        cwd[name] = node()
    else:
        cwd[name] = int(size)


def get_size(node: defaultdict | int) -> int:
    if not isinstance(node, defaultdict):
        return node
    return sum(get_size(child) for child in node.values())


def sum_small_child_nodes(node: defaultdict[str, defaultdict | int]) -> None:
    global SMALL_DIRS_SUM
    for child in node.values():
        if not isinstance(child, defaultdict):
            continue

        size = get_size(node=child)
        if size <= MAX_SMALL_DIR_SIZE:
            SMALL_DIRS_SUM += size

        sum_small_child_nodes(node=child)


with open(INPUT_FILE, mode="r") as infile:
    lines = [line.strip() for line in infile]

lines.reverse()

next_line = lines.pop()
while lines:
    current_line = next_line
    handle_current_cmd, arg = get_cmd_from_line(line=current_line)
    output: list[str] = []

    next_line = lines.pop()
    while not next_line.startswith("$"):
        output.append(next_line)
        try:
            next_line = lines.pop()
        except IndexError:
            break

    handle_current_cmd(arg=arg, output_lines=output)


sum_small_child_nodes(node=ROOT)

TOTAL_SPACE = 70000000
NEEDED_SPACE = 30000000
UNUSED_SPACE = TOTAL_SPACE - get_size(node=ROOT)
NEED_TO_DELETE = NEEDED_SPACE - UNUSED_SPACE


print(f"Part 1: {SMALL_DIRS_SUM}")
print(f"Part 2: {2}")
