588. Design In-Memory File System

https://algo.monster/liteproblems/588

Problem Description
This problem asks you to design an in-memory file system data structure that supports basic file and directory operations.

The file system should support four main operations:

ls(path): List the contents at a given path

If the path points to a file, return a list containing only that file's name
If the path points to a directory, return all files and subdirectories within it in lexicographic (alphabetical) order
mkdir(path): Create a new directory

The path given will not already exist
If intermediate directories in the path don't exist, create them automatically (similar to mkdir -p in Unix)
addContentToFile(filePath, content): Add content to a file

If the file doesn't exist, create it with the given content
If the file already exists, append the new content to the existing content
readContentFromFile(filePath): Read and return all content from a file

The solution uses a Trie (prefix tree) data structure to represent the file system hierarchy. Each node in the Trie can represent either a file or a directory:

Directories contain children (other files or directories)
Files contain content and have a flag marking them as files
The path parsing works by splitting paths on / characters. For example, /a/b/c would be split into components ['', 'a', 'b', 'c'], where the empty string represents the root directory.

Key implementation details:

The insert method navigates through the path components, creating nodes as needed
The search method traverses the Trie to find a specific file or directory
File content is stored as a list of strings that get concatenated when read
Directory listings are automatically sorted to maintain lexicographic order
