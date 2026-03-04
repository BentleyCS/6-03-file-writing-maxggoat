import CSP_6_03_Writing_to_files

from CSP_6_03_Writing_to_files import writeFile, sortNames, highScore


def test_writeFile():

        test_data = [1, 2, 3]
        file_name = "test.txt"

        writeFile(test_data, file_name)

        with open(file_name, 'r') as file:
            contents = file.read()

        assert contents == "1\n2\n3\n"


def test_sortNames():

    writeFile(["3\n", "2\n", "1\n"], "source.txt")


    sortNames("source.txt", "target.txt")

    with open("target.txt") as file:
        sorted_names = [line.strip() for line in file]

    assert sorted_names == ["1", "2", "3"]






def test_high_score():
    assert False
