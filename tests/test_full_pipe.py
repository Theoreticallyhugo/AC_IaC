from pathlib import Path

from AC_IaC.inference.full_pipe import main


def test_rebuilt_filestructure():
    main(
        Path("./tests/test_in_structure"),
        Path("./tests/test_out_structure"),
        "aa",
        "bb",
        False,
        True,
    )
    assert Path("./tests/test_out_structure/").is_dir()
    assert Path("./tests/test_out_structure/S.txt").is_file()
    assert Path("./tests/test_out_structure/a/").is_dir()
    assert Path("./tests/test_out_structure/a/AA.txt").is_file()
    assert Path("./tests/test_out_structure/b/").is_dir()
    assert Path("./tests/test_out_structure/b/bb/").is_dir()
    assert Path("./tests/test_out_structure/b/bb/BBB.txt").is_file()


def test_single_file_dry():
    main(
        Path("./tests/test_in_file/A.txt"),
        Path("./tests/test_out_file/"),
        "aa",
        "bb",
        False,
        True,
    )
    assert Path("./tests/test_out_file/").is_dir()
    assert Path("./tests/test_out_file/A.txt").is_file()
    assert Path("./tests/test_out_file/A.ann").is_file()
