1)Start
2)Define a function with file path, key, and new value as parameters.
3)Open the configuration file in read (r) mode.
4)Read all lines and store them in a list.
5)Open the same file in write (w) mode.
6)Traverse each line in the list.
7)Check if the line contains the specified key.
8)If the key is found:
    Update the line with the new value.
    Write the updated line to the file.
9)Otherwise:
    Write the original line to the file.
10)Display a success message when the value is updated.
11)End.