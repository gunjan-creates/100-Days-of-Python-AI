"""Uses weak references to cache objects without preventing garbage collection."""
import weakref


class Data:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Data({self.name})"


if __name__ == "__main__":
    cache: weakref.WeakValueDictionary[str, Data] = weakref.WeakValueDictionary()
    item = Data("alpha")
    cache["alpha"] = item
    print("Cached:", list(cache.items()))
    del item
    print("After deletion:", list(cache.items()))
