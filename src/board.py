from typing import List, Optional

class Board:
    """
    3x3の○×ゲーム盤面を管理するクラス。
    """

    def __init__(self):
        # 9マスの盤面をNone（空）で初期化する
        self.cells: List[Optional[str]] = [None] * 9

    def display(self) -> None:
        """
        現在の盤面をCUIに表示する。
        [F-004]: The system shall display the current 3x3 board state in CUI.
        """
        # grid_id (1-9) に対応する形で3x3の形式で表示する
        # 例:
        #  1 | 2 | 3
        # -----------
        #  etc...
        # 埋まっている箇所は 'O' や 'X' を表示し、空は数字を表示する。
        for i in range(0, 9, 3):
            row = []
            for j in range(3):
                cell_value = self.cells[i + j]
                row.append(cell_value if cell_value is not None else str(i + j + 1))
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if i < 6:
                print("-----------")

    def place_mark(self, grid_id: int, mark: str) -> bool:
        """
        指定されたマスにマークを配置する。
        [F-002]: [If a player inputs 1-9], the system shall place their mark on the corresponding grid if it's empty.
        [F-003]: [If the input is invalid or grid is occupied], the system shall display an error and re-prompt.

        Args:
            grid_id: 1~9の整数
            mark: 'O' または 'X'

        Returns:
            bool: 配置に成功した場合はTrue、失敗（既に埋まっている等）はFalse
        """
        # 1. grid_id が 1-9 の範囲内かチェックする
        # 2. 指定されたセル (grid_id - 1) が None かどうかチェックする
        # 3. 空であれば self.cells[index] に mark を代入し True を返す
        # 4. 埋まっていれば何もせず False を返す
        if 1 <= grid_id <= 9:
            index = grid_id - 1
            if self.cells[index] is None:
                self.cells[index] = mark
                return True
        else:
            print("Error: grid_id must be between 1 and 9.")
        return False

    def is_full(self) -> bool:
        """
        全てのマスが埋まっているか確認する。
        """
        # self.cells 内に None が含まれていないか確認する
        return False

    def get_empty_cells(self) -> List[int]:
        """
        空いているマスの grid_id リストを返す（AI用）。
        """
        # None のマスのインデックス+1をリストにして返す
        return []
