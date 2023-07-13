class Ebook:
    def __init__(self, path, words_num: int):
        self.path = path
        self.pages: dict[int: str] = {}
        with open(path, 'r') as fh:
            content = fh.read()
        all_words: list[str] = content.split()
        page_num = 1
        for i in range(0, len(all_words), words_num):
            page_words = all_words[i : i+words_num]
            self.pages[page_num] = " ".join(page_words)
            page_num += 1
        self.__book_marks: dict[str:str] = {}

    def get_pages_amount(self):
        return len(self.pages)

    def read_page(self, num: int):
        if num not in self.pages:
            return None
        return self.pages[num]

    def bookmark_save(self, page_num: int, mark_name: str):
        self.__book_marks[mark_name] = self.pages[page_num]
        print(f"Bookmark {mark_name} Saved Successfully")

    def go_to_bookmark(self, bookmark: str):
        if bookmark not in self.__book_marks:
            print("Bookmark Doesn't exist")
            return None
        return self.__book_marks[bookmark]

    def delete_bookmark(self, bookmark: str):
        if bookmark in self.__book_marks:
            del self.__book_marks[bookmark]

    def delete_all_bookmarks(self):
        self.__book_marks = {}
        print("Deletion complete")

    def display_bookmarks(self):
        for bookmark in self.__book_marks:
            print(bookmark, end=",")

if __name__ == "__main__":
    path = "C:\\Users\mishl\PycharmProjects\Practicing\\alice_in_wonderland.txt"
    book = Ebook(path, 1000)
    book.bookmark_save(2, "Nice1")
    book.bookmark_save(3, "Nice2")
    book.bookmark_save(4, "Nice3")
    book.delete_all_bookmarks()
    print(book.go_to_bookmark("Nice2"))
    book.bookmark_save(4, "Nice3")
    book.bookmark_save(3, "Nic2")
    book.bookmark_save(3, "Ni422")
    book.display_bookmarks()

