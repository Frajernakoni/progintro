
import sys
sys.path.insert(0, "text-project")

from textkit.core import normalize_whitespace, count_words # type: ignore

text1 = "  Ahoj\n  světe  "
text2 = "Python je super"
text3 = "  Učím se   programovat.  "

print(normalize_whitespace(text1))
print(count_words(text1))

print(normalize_whitespace(text2))
print(count_words(text2))

print(normalize_whitespace(text3))
print(count_words(text3))
