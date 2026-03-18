# tic-tac-toe-spec.md

## 1.0 Document Control
- **Created**: 2026-03-18 22:15
- **Revision**: 1.0 (Initial Release)

## 1.0.5 Specification Hearing
- **Status**: Completed.
- **Key Clarifications**: 1-9 grid input, immediate exit after winner display, randomized turn order.

## 1.1 Core Intent
- シンプルなCUI環境で○×ゲーム（Tic-Tac-Toe）の楽しさを提供する。
- Pythonの基本構文とpytestを用いたテスト駆動開発（TDD）の学習。
- ランダムAIとの対戦を通じたロジック分離の理解。

## 1.2 Glossary
- **ANMS**: Advanced Narrative Meta-Specification (AI駆動設計手法)
- **EARS**: Easy Approach to Requirements Syntax
  - `[Trigger], the [System] shall [Response]`
- **Grid ID**: 1~9の整数。1-3(上段), 4-6(中段), 7-9(下段)を指す。

## 1.3 Technical Constraints & Directory
- **Language**: Python 3.10+
- **Test Framework**: pytest
- **Library**: Standard libraries only (random)
- **Directory Structure**:
```text
tic-tac-toe/
├── src/
│   ├── main.py        # Entry point
│   ├── board.py       # Board logic
│   ├── player.py      # Player/AI logic
│   └── game.py        # Game loop/Judge
├── tests/
│   ├── test_board.py
│   └── test_game.py
└── tic-tac-toe-spec.md
```

## 1.4 Requirements (F-XXX / NF-XXX)
- **F-001**: [When the game starts], the system shall determine the starting player (Man or AI) randomly.
- **F-002**: [If a player inputs 1-9], the system shall place their mark on the corresponding grid if it's empty.
- **F-003**: [If the input is invalid or grid is occupied], the system shall display an error and re-prompt.
- **F-004**: [After every turn], the system shall display the current 3x3 board state in CUI.
- **F-005**: [When three marks align], the system shall declare the winner and terminate.
- **F-006**: [When all grids are filled without alignment], the system shall declare a draw and terminate.
- **F-007**: [During AI's turn], the system shall pick an empty grid randomly.

## 1.5 Data & Interface Schema
- **Board State**: List of 9 strings (null, "X", "O")
- **Interface**:
  - `Board.place_mark(grid_id: int, mark: str) -> bool`
  - `Game.check_winner() -> Optional[str]`
  - `AI.get_move(board: List[str]) -> int`

## 1.6 Phase Strategy
- **v1 (MVP)**: Basic game loop, random AI, winner detection.
- **v2 (Future)**: Minimax AI, GUI support.
