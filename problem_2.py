import os

def find_files(suffix: str, path: str) -> list[str]:
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Parameters:
    -----------
    suffix : str
        The suffix of the files to be found.
    path : str
        The root directory path where the search should begin.

    Returns:
    --------
    list[str]
        A list of file paths that end with the given suffix.
    """
    if not suffix or not path:
        return []
    if not os.path.exists(path):
        return []

    results: list[str] = []

    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isfile(full_path):
            if full_path.endswith(suffix):
                results.append(full_path)
        elif os.path.isdir(full_path):
            results.extend(find_files(suffix, full_path))

    return results


if __name__ == "__main__":
    # Test Case 1: Standard test case with known structure
    print("Test Case 1: Standard directory structure")
    result = find_files(".c", "./testdir")
    print(result)
    # Expected output: ['./testdir/subdir1/a.c', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c']

    # Test Case 2
    result = find_files("", "./testdir")
    assert result == []  # empty suffix returns empty list

    # Test Case 3
    result = find_files(".c", "./no_such_directory")
    assert result == []  # non-existent path returns empty list