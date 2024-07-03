count = 0
def increment_global():
  global count
  count += 1
increment_global()
print(count) 