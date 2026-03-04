import CSP_6_03_Writing_to_files

from CSP_6_03_Writing_to_files import writeFile, sortNames, highScore


def test_writeFile():

        test_data = [1, 2, 3]
        file_name = "test.txt"

        writeFile(test_data, file_name)

        with open(file_name, 'r') as file:
            contents = file.read()

        assert contents == "1\n2\n3\n"







def test_high_score():
    assert False
