"""Music class"""
class Song:
    def __init__(self, name: str, genre: str, duration: int):
        self.name = name
        self.genre = genre
        self.durations = duration
    
    def show_info(self):
        min, sec = self.durations // 60, self.durations % 60
        return f"{self.name} <|> {self.genre} <|> {min}.{sec:02}"
    
Rickroll = Song(input(), input(), int(input()))
print(Rickroll.show_info())
