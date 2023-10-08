from dataclasses import dataclass

@dataclass
class Data:
    value: int
    name: str

    @staticmethod
    def static_method():
        print("taticmethod.")

    @classmethod
    def class_method(cls):
        print("class method.")
