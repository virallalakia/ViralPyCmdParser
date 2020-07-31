import pytest

from viralpycmdparser.cmdparser import CmdParser
from viralpycmdparser.result.cmdparserresult import CmdParserResult


@pytest.mark.parametrize(
    "delim, ip, op",
    [
        pytest.param(None, "cmd", CmdParserResult("cmd"), id="Cmd without args"),
        pytest.param(
            None, "cmd arg1", CmdParserResult("cmd", ["arg1"]), id="Cmd with 1 arg"
        ),
        pytest.param(
            None,
            "cmd arg1 arg2 arg3",
            CmdParserResult("cmd", ["arg1", "arg2", "arg3"]),
            id="Cmd with 3 args",
        ),
        pytest.param(
            None,
            "  cmd   arg1   arg2    arg3    ",
            CmdParserResult("cmd", ["arg1", "arg2", "arg3"]),
            id="Cmd with 3 args and extra spaces",
        ),
        pytest.param(
            ",",
            "cmd",
            CmdParserResult("cmd"),
            id="Cmd without args but with custom delimiter",
        ),
        pytest.param(
            ",",
            "cmd,arg1",
            CmdParserResult("cmd", ["arg1"]),
            id="Cmd with 1 arg and custom delimiter",
        ),
        pytest.param(
            "__",
            "cmd__arg1 with space__arg2",
            CmdParserResult("cmd", ["arg1 with space", "arg2"]),
            id="Cmd with 2 args, with space and custom delimiter",
        ),
    ],
)
def test_hello_world(delim: str, ip: str, op: CmdParserResult) -> None:
    cmdparser = CmdParser(delim) if delim else CmdParser()
    result = cmdparser.parse(ip)
    assert result.cmd == op.cmd
    for i in range(len(result.args)):
        assert result.args[i] == op.args[i]
