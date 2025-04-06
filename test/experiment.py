from pydantic import BaseModel, create_model

class TestA(BaseModel):
    a: int
    b: int = 2
    c: int = 3

TestB = create_model('TestB', a=int, b=(int, 2), c=(int, 3))

print(TestA.__pydantic_fields__)
print(TestB.__pydantic_fields__)

TestA()
TestB()

class TestC(TestB):
    pass

TestC()
