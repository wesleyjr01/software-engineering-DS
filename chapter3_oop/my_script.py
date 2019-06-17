import first_package

# Create instance of MyClass
my_instance = first_package.MyClass(value="class attribute value")

# Print out class attribute value
print(my_instance.attribute)

# Print tokanization performed by class Document
upper_document = first_package.Document(text="faz isso ai")

print(f"Upper string:{upper_document.upper}")
print(f"Count string:{upper_document.word_counts}")

# Inheritance ChildClass from Document class
child = first_package.ChildClass(text="faz isso ai fiao")

print("\n")
print(f"Upper string:{child.upper}")
print(f"Count string:{child.word_counts}")
print(f"Tokenize string:{child.tokens}")

