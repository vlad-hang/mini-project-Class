from dataclasses import dataclass


@dataclass
class Book:
    id: int
    title: str
    author: str
    year: int
    is_read: bool

    def mark_as_read(self):
        self.is_read = True
        return None

    def mark_as_unread(self):
        self.is_read = False
        return None

    def result(self):
        if self.is_read == False:
            return "не прочитана"
        else:

            return "прочитана"

    def __str__(self):
        return (
            f"[{self.id}] {self.title} - {self.author} ({self.year}) [{self.result()}]"
        )
