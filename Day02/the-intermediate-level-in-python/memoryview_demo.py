"""Illustrates memoryview for zero-copy slicing."""

if __name__ == "__main__":
    data = bytearray(b"abcdef")
    view = memoryview(data)
    slice_view = view[2:4]
    print("Before:", data)
    slice_view[:] = b"XY"
    print("After:", data)
