class Player:
  def __init__(self, name, team):
    self.name = name
    self.xp = 1500
    self.team = team

  def introduce(self):
    print(f"Hello! I'm {self.name} and I play for {self.team}")

class Team:
  def __init__(self, team_name):
    self.team_name = team_name
    self.players = []

  def show_players(self):
    for player in self.players:
      print(player.name)
      print(player.xp)

  def add_player(self, name):
    new_player = Player(name, self.team_name)
    self.players.append(new_player)

  def del_player(self, name):
    for player in self.players:
      if player.name == name:
        self.players.remove(player)

  def total_xp(self):
    total_xp = 0
    for player in self.players:
      total_xp += player.xp
    print(f"{self.team_name} has {total_xp} total XP")
    

team_x = Team("Team X")
team_x.add_player("nico")
team_x.add_player("now")

team_blue = Team("Team Blue")
team_blue.add_player("lynn")

#team_x.show_players()
#team_x.del_player("nico")
team_x.show_players()

team_x.total_xp()
team_blue.total_xp()