from book import Book
from display_strategy import DisplayStrategy, ConsoleDisplayStrategy, ReverseDisplayStrategy
from print_strategy import PrintStrategy, ConsolePrintStrategy, ReversePrintStrategy
from serialize_strategy import SerializeStrategy, JsonSerializer, XmlSerializer


def main(book: Book, commands: list[tuple[str, str]]) -> None | str:
    display_strategies = {
        "console": ConsoleDisplayStrategy(),
        "reverse": ReverseDisplayStrategy(),
    }

    print_strategies = {
        "console": ConsolePrintStrategy(),
        "reverse": ReversePrintStrategy(),
    }

    serialize_strategies = {
        "json": JsonSerializer(),
        "xml": XmlSerializer(),
    }

    for cmd, method_type in commands:
        if cmd == "display":
            strategy: DisplayStrategy = display_strategies.get(method_type)
            if strategy:
                strategy.display(book.content)
            else:
                raise ValueError(f"Unknown display type: {method_type}")
        elif cmd == "print":
            strategy: PrintStrategy = print_strategies.get(method_type)
            if strategy:
                strategy.print_book(book.title, book.content)
            else:
                raise ValueError(f"Unknown print type: {method_type}")
        elif cmd == "serialize":
            strategy: SerializeStrategy = serialize_strategies.get(method_type)
            if strategy:
                return strategy.serialize(book.title, book.content)
            else:
                raise ValueError(f"Unknown serialize type: {method_type}")


if __name__ == "__main__":
    sample_book = Book("Sample Book", "This is some sample content.")
    print(main(sample_book, [("display", "reverse"), ("serialize", "xml")]))
