# implement unix find command as an api , the api will support findings;
# files that have given certain requirements
# files with a certain naming patterns focus on 2 uses cases at first
# find al files over 5 MB somewhere under directory
#https://www.youtube.com/watch?v=efgmeiMaT2c

"""
✅ High-Level Design Approach
Use the Strategy Pattern or Filter Pattern:

Write a reusable FileFinder class to traverse directories

Accept pluggable filter functions (e.g., by size, name, extension)

Support future filters like creation time, permissions, etc.

📦 Directory Traversal Options
Python offers two main ways:

os.walk() – Recursive generator

Path.rglob() – Convenient but slower for fine control

We'll go with os.walk() for flexibility and performance.
"""
import os
from typing import List, Callable

class FileFinder:
    def __init__(self, root_dir: str):
        self.root_dir = root_dir

    def find(self, filter_func: Callable[[str], bool]) -> List[str]:
        matched_files = []
        for dirpath, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                if filter_func(full_path):
                    matched_files.append(full_path)
        return matched_files

# --------------------
# Filter Functions
# --------------------

def filter_by_size(min_size_mb: int) -> Callable[[str], bool]:
    def _filter(path: str) -> bool:
        try:
            return os.path.getsize(path) > min_size_mb * 1024 * 1024
        except OSError:
            return False
    return _filter

def filter_by_extension(extension: str) -> Callable[[str], bool]:
    def _filter(path: str) -> bool:
        return path.lower().endswith(extension.lower())
    return _filter

# --------------------
# Usage Examples
# --------------------

if __name__ == "__main__":
    finder = FileFinder("/your/target/directory")

    # Use case 1: Find all files over 5 MB
    large_files = finder.find(filter_by_size(5))
    print("Large files (>5MB):")
    print("\n".join(large_files))

    # Use case 2: Find all XML files
    xml_files = finder.find(filter_by_extension(".xml"))
    print("\nXML files:")
    print("\n".join(xml_files))


### https://leetcode.com/discuss/post/609070/amazon-ood-design-unix-file-search-api-b-b8py/
# Specification Pattern 
from abc import ABC, abstractmethod
from collections import deque
from typing import List

# File
# - no need to implement different files & directories as that will not be used in this system


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.children = []
        self.is_directory = False if '.' in name else True
        self.children = []
        self.extension = name.split(".")[1] if '.' in name else ""

    def __repr__(self):
        return "{"+self.name+"}"

# Filters


class Filter(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def apply(self, file):
        pass


class MinSizeFilter(Filter):
    def __init__(self, size):
        self.size = size

    def apply(self, file):
        return file.size > self.size


class ExtensionFilter(Filter):
    def __init__(self, extension):
        self.extension = extension

    def apply(self, file):
        return file.extension == self.extension


# LinuxFindCommand

class LinuxFind():
    def __init__(self):
        self.filters: List[Filter] = []

    def add_filter(self, given_filter):
        # validate given_filter is a filter
        if isinstance(given_filter, Filter):
            self.filters.append(given_filter)

    def apply_OR_filtering(self, root):
        found_files = []

        # bfs
        queue = deque()
        queue.append(root)
        while queue:
            # print(queue)
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                for filter in self.filters:
                    if filter.apply(curr_root):
                        found_files.append(curr_root)
                        print(curr_root)
                        break
        return found_files

    def apply_AND_filtering(self, root):
        found_files = []

        # bfs
        queue = deque()
        queue.append(root)
        while queue:
            curr_root = queue.popleft()
            if curr_root.is_directory:
                for child in curr_root.children:
                    queue.append(child)
            else:
                is_valid = True
                for filter in self.filters:
                    if not filter.apply(curr_root):
                        is_valid = False
                        break
                if is_valid:
                    found_files.append(curr_root)
                    print(curr_root)

        return found_files


f1 = File("root_300", 300)

f2 = File("fiction_100", 100)
f3 = File("action_100", 100)
f4 = File("comedy_100", 100)
f1.children = [f2, f3, f4]

f5 = File("StarTrek_4.txt", 4)
f6 = File("StarWars_10.xml", 10)
f7 = File("JusticeLeague_15.txt", 15)
f8 = File("Spock_1.jpg", 1)
f2.children = [f5, f6, f7, f8]

f9 = File("IronMan_9.txt", 9)
f10 = File("MissionImpossible_10.rar", 10)
f11 = File("TheLordOfRings_3.zip", 3)
f3.children = [f9, f10, f11]

f11 = File("BigBangTheory_4.txt", 4)
f12 = File("AmericanPie_6.mp3", 6)
f4.children = [f11, f12]


greater5_filter = MinSizeFilter(5)
txt_filter = ExtensionFilter("txt")

my_linux_find = LinuxFind()
my_linux_find.add_filter(greater5_filter)
my_linux_find.add_filter(txt_filter)

print(my_linux_find.apply_OR_filtering(f1))
print(my_linux_find.apply_AND_filtering(f1))