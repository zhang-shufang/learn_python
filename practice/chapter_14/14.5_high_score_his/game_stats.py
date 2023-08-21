from mailbox import NoSuchMailboxError
from pathlib import Path
import json
        
    
class GameStats:
    """跟踪游戏的统计信息"""
    def __init__(self, game) -> None:
        """初始化统计信息"""
        self.settings = game.settings
        self.reset_stats()

        self.file_name = "high_score.json"
        
        # 若有最高分数据，则读取最高分数据
        try: 
            path = Path(self.file_name)
            contents_readed = json.loads(path.read_text())
            self.high_score = int(contents_readed['high_score'])
        except FileNotFoundError:
            self.high_score = 0
        else:
            print(self.high_score)

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def save_high_score(self):
        """储存最高分数据"""
        path = Path(self.file_name)
        contents_write = json.dumps({'high_score': self.high_score})
        path.write_text(contents_write)
        # try: 
            
        # except:
        #     self.high_score = 0
        # else:
        #     self.high_score = path.read_text()
        #     print(self.high_score)