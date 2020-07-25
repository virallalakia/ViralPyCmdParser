import pytest

from viralpycmdparser.cmdparser import CmdParser
from viralpycmdparser.result.cmdparserresult import CmdParserResult


@pytest.mark.parametrize(
    "ip, op",
    [
        pytest.param("cmd", CmdParserResult("cmd"), id="Cmd without args"),
        pytest.param("cmd arg1", CmdParserResult("cmd", ["arg1"]), id="Cmd with 1 arg"),
    ],
)
def test_hello_world(ip: str, op: CmdParserResult) -> None:
    result = CmdParser().parse(ip)
    assert result.cmd == op.cmd
    for i in range(len(result.args)):
        assert result.args[i] == op.args[i]
