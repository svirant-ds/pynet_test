#!/usr/bin/env python
with open("3lines-ex.txt","r") as f:
  content = f.read()
print(content)
with open("3lines.txt","w") as f:
  f.write("hello\nworld\ngoodbye\n")
with open("3lines.txt","a") as f:
  f.write("one more line\n")
with open("3lines.txt","r") as f:
  content = f.read()
print(content)
