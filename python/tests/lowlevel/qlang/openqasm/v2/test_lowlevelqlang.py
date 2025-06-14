from __future__ import annotations

from hhat_lang.core.code.ir import InstrIRFlag, TypeIR
from hhat_lang.core.code.utils import InstrStatus
from hhat_lang.core.data.core import CoreLiteral, Symbol
from hhat_lang.core.memory.core import MemoryManager, Stack
from hhat_lang.dialects.heather.code.simple_ir_builder.ir import (
    FnIR,
    IRArgs,
    IRBlock,
    IRInstr,
)
from hhat_lang.dialects.heather.interpreter.classical.executor import Evaluator
from hhat_lang.low_level.quantum_lang.openqasm.v2.instructions import QNot
from hhat_lang.low_level.quantum_lang.openqasm.v2.qlang import LowLeveQLang


def test_gen_program_single_empty_redim() -> None:
    code_snippet = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[1];
creg c[1];

h q[0];
measure q -> c;
"""

    qv = Symbol("@v")

    mem = MemoryManager(5)
    mem.idx.add(qv, 1)
    mem.idx.request(qv)

    ex = Evaluator(mem, TypeIR(), FnIR())

    block = IRBlock()
    block.add_instr(IRInstr(Symbol("@redim"), IRArgs(), InstrIRFlag.CALL))

    qlang = LowLeveQLang(Symbol("@v"), block, mem.idx, ex, Stack())
    res = qlang.gen_program()

    assert res == code_snippet


def test_gen_program_single_q0_redim() -> None:
    code_snippet = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg c[3];

x q[0];
x q[2];
h q[0];
h q[1];
h q[2];
measure q -> c;
"""

    mem = MemoryManager(5)
    mem.idx.add(Symbol("@v"), 3)
    mem.idx.request(Symbol("@v"))

    ex = Evaluator(mem, TypeIR(), FnIR())

    block = IRBlock()
    block.add_instr(
        IRInstr(
            name=Symbol("@redim"),
            args=IRArgs(CoreLiteral(Symbol("@5").value, "@u3")),
            flag=InstrIRFlag.CALL,
        )
    )

    qlang = LowLeveQLang(Symbol("@v"), block, mem.idx, ex, Stack())
    res = qlang.gen_program()
    print(res)
    # assert res == code_snippet


def test_gen_program_single_bool_not() -> None:
    code_snippet = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[1];
creg c[1];

x q[0];
measure q -> c;
"""

    qv = Symbol("@v")

    mem = MemoryManager(5)
    mem.idx.add(qv, 1)
    mem.idx.request(qv)

    ex = Evaluator(mem, TypeIR(), FnIR())

    block = IRBlock()
    block.add_instr(IRInstr(Symbol("@not"), IRArgs(), InstrIRFlag.CALL))

    qlang = LowLeveQLang(Symbol("@v"), block, mem.idx, ex, Stack())
    res = qlang.gen_program()

    assert res == code_snippet


def test_gen_program_single_u2_not() -> None:
    code_snippet = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[2];
creg c[2];

x q[0];
x q[1];
measure q -> c;
"""

    qv = Symbol("@v")

    mem = MemoryManager(5)
    mem.idx.add(qv, 2)
    mem.idx.request(qv)

    ex = Evaluator(mem, TypeIR(), FnIR())

    block = IRBlock()
    block.add_instr(IRInstr(Symbol("@not"), IRArgs(), InstrIRFlag.CALL))

    qlang = LowLeveQLang(Symbol("@v"), block, mem.idx, ex, Stack())
    res = qlang.gen_program()

    assert res == code_snippet


def test_gen_program_single_u3_not() -> None:
    code_snippet = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[3];
creg c[3];

x q[0];
x q[1];
x q[2];
measure q -> c;
"""

    qv = Symbol("@v")

    mem = MemoryManager(5)
    mem.idx.add(qv, 3)
    mem.idx.request(qv)

    ex = Evaluator(mem, TypeIR(), FnIR())

    block = IRBlock()
    block.add_instr(IRInstr(Symbol("@not"), IRArgs(), InstrIRFlag.CALL))

    qlang = LowLeveQLang(Symbol("@v"), block, mem.idx, ex, Stack())
    res = qlang.gen_program()

    assert res == code_snippet


def test_gen_program_single_u4_not() -> None:
    code_snippet = """OPENQASM 2.0;
include "qelib1.inc";
qreg q[4];
creg c[4];

x q[0];
x q[1];
x q[2];
x q[3];
measure q -> c;
"""

    qv = Symbol("@v")

    mem = MemoryManager(5)
    mem.idx.add(qv, 4)
    mem.idx.request(qv)

    ex = Evaluator(mem, TypeIR(), FnIR())

    block = IRBlock()
    block.add_instr(IRInstr(Symbol("@not"), IRArgs(), InstrIRFlag.CALL))

    qlang = LowLeveQLang(Symbol("@v"), block, mem.idx, ex, Stack())
    res = qlang.gen_program()

    assert res == code_snippet
