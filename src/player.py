import random
from typing import List
from src.board import Board

class Player:
    """
    プレイヤーの基底クラス。
    """
    def __init__(self, mark: str):
        self.mark = mark

    def get_move(self, board: Board) -> int:
        """
        次の手を決定する（サブクラスで実装）。
        """
        raise NotImplementedError

class HumanPlayer(Player):
    """
    人間（ユーザー）プレイヤー。
    """
    def get_move(self, board: Board) -> int:
        """
        [F-002/F-003]: ユーザーから1-9の入力を受け取る。
        """
        # 1. ユーザーに対して `f"Player {self.mark}, enter your move (1-9): "` と入力案内を出す
        # 2. 入力が数値でない、または 1-9 の範囲外であれば再入力を促す
        # 3. 入力された grid_id を返す
        return 0

class AIPlayer(Player):
    """
    ランダムAIプレイヤー。
    """
    def get_move(self, board: Board) -> int:
        """
        [F-007]: During AI's turn, the system shall pick an empty grid randomly.
        """
        # 1. board.get_empty_cells() を呼び出して空いているマスのリストを取得する
        # 2. リストから random.choice で一つ選ぶ
        # 3. 選んだ grid_id を返す
        return 0
