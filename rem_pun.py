
s = "bay?y!a.n,ah"
text=""
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for item in s :
    if item not in punctuations:
        text+=item

print(text)

