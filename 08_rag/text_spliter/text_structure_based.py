from langchain.text_splitter import RecursiveCharacterTextSplitter

text = """
Space exploration has led to incredible scientific discoveries. From landing on the Moon to exploring Mars, humanity continues to push the boundaries of what’s possible beyond our planet.

These missions have not only expanded our knowledge of the universe but have also contributed to advancements in technology here on Earth. Satellite communications, GPS, and even certain medical imaging techniques trace their roots back to innovations driven by space programs.
"""

# Initialize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
)

# Perform the split
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)


'''
it will split the text into smaller chunks based on the chunk_size and chunk_overlap parameters.
chunk_size: The maximum number of characters in each chunk.
chunk_overlap: The number of overlapping characters between adjacent chunks.

step of splitting:
1. '/n/n' -> paragraph
2. '/n' -> line
3. ' ' -> word
4. '' -> character
'''