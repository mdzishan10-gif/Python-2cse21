Perform basic operations on string 
1. Concatenation 
2. Slicing 
3. Indexing 
4. Searching 
5. Splitting

s1 = "Hello"
s2 = "World"

concat = s1 + " " + s2
print(concat)

slice_part = concat[0:5]
print(slice_part)

index_char = concat[1]
print(index_char)

search_pos = concat.find("World")
print(search_pos)

split_str = concat.split(" ")
print(split_str)
