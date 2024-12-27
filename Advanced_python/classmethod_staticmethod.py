class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @staticmethod
    def is_even(num):
        return num % 2 == 0

MyClass.increment_count()
print(MyClass.count)
print(MyClass.is_even(10))