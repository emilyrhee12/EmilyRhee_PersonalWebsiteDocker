import os
import tempfile
from DAL import DAL


def test_dal_add_and_get():
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    try:
        dal = DAL(path)
        # ensure no projects initially
        rows = dal.get_all_projects()
        assert rows == []
        # add a project
        pid = dal.add_project("T1", "Desc", "img.png")
        assert isinstance(pid, int)
        rows = dal.get_all_projects()
        assert len(rows) == 1
        assert rows[0][1] == "T1"
    finally:
        os.remove(path)
