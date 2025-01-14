# Copyright 2023 The Unitary Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from unitary.alpha import QuantumObject, QuantumWorld
from unitary.examples.quantum_chinese_chess.enums import SquareState
from string import ascii_lowercase, digits


# Build quantum objects a0 to i9, and add them to a quantum world.
def init_board() -> QuantumWorld:
    board = {}
    for col in ascii_lowercase[:9]:
        for row in digits:
            board[col + row] = QuantumObject(col + row, SquareState.EMPTY)
    return QuantumWorld(list(board.values()))
