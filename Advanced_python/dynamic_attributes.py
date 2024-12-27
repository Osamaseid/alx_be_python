class DynamicAttributes:
    pass

obj = DynamicAttributes()
setattr(obj, 'name', 'Alice')
print(obj.name)