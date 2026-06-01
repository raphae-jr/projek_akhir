#====================================================================

# CLASS PLAYER, ENEMY, ITEM, SKILL
class Entitas:
  def __init__(self, nama, hp=100, attack=10):
    self.nama = nama
    self.hp = hp
    self.max_hp = hp
    self.attack = attack

class NodeSkill:
  def __init__(self, nama_skill):
    self.nama = nama_skill
    self.left = None
    self.right = None

class Player(Entitas):
  def __init__(self, nama, role='fighter'):
    super().__init__(nama)
    self.exp = 0
    self.score = 0
    self.level = 1
    self.role = role
    self.gold = 0
    self.inventory = Inventory()
    self.skill_tree = NodeSkill('Lvl 1: Tebasan Pedang')
    self.buruan = set()

    if role == 'tank':
      self.hp = 150
      self.max_hp = 150
      self.attack = 5
      self.skill_tree = NodeSkill('Lvl 1: Hantaman Perisai')
    elif role == 'marksman':
      self.hp = 80
      self.max_hp = 80
      self.attack = 15
      self.skill_tree = NodeSkill('Lvl 1: Panah Kilat')

class Enemy(Entitas):
  def __init__(self, nama, hp, attack, reward_gold):
    super().__init__(nama, hp, attack)
    self.reward_gold = reward_gold

class Item:
  def __init__(self, nama, jenis, power, harga):
    self.nama = nama
    self.jenis = jenis
    self.power = power
    self.harga = harga

class Inventory:
  def __init__(self):
    self.items = []

  def tambah_item(self, item):
    self.items.append(item)

  def tampilkan_item(self):
    if not self.items:
      return False
    for i, item in enumerate(self.items):
      print(f'{i+1}. {item.nama}: {item.jenis} + {item.power}')
    return True

  def hapus_item(self, index):
    if 0 < index <= len(self.items):
      return self.items.pop(index-1)
    return None

toko = [
  Item('heal potion', 'heal', 30, 30),
  Item('attack potion', 'buff', 10, 30)
]

#================================================

# CLASS UNTUK LEADERBOARD ENEMY
class NodeEnemy: # BINARY SEARCH TREE
  def __init__(self, enemy):
    self.enemy = enemy
    self.left = None
    self.right = None

class BountyBoard: # BINARY SEARCH TREE
  def __init__(self):
    self.root = None

  def insert(self, enemy):
    if self.root is None:
      self.root = NodeEnemy(enemy)
    else:
      self.rekursif_insert(self.root, enemy)

  def rekursif_insert(self, node, enemy):
    if enemy.reward_gold < node.enemy.reward_gold:
      if node.left is None:
        node.left = NodeEnemy(enemy)
      else:
        self.rekursif_insert(node.left, enemy)
    elif enemy.reward_gold > node.enemy.reward_gold:
      if node.right is None:
        node.right = NodeEnemy(enemy)
      else:
        self.rekursif_insert(node.right, enemy)

  def tampilkan_board(self, node, nomor = None):
    if nomor is None:
      nomor = [1]
    if node:
      self.tampilkan_board(node.right, nomor)
      print(f"{nomor[0]}. {node.enemy.nama} | HP: {node.enemy.hp} | Atk: {node.enemy.attack} | Hadiah: {node.enemy.reward_gold} Gold") 
      nomor[0] += 1
      self.tampilkan_board(node.left, nomor)
  
  def search_target(self, node, target_gold):
    if node is None or node.enemy.reward_gold == target_gold:
      return node
    if target_gold < node.enemy.reward_gold:
      return self.search_target(node.left, target_gold)
    return self.search_target(node.right, target_gold)
#===================================================================================================================================

# CLASS UNTUK DATA PEMAIN
class NodePlayer(): #single linked list
  def __init__(self, player):
    self.player = player
    self.next = None

class PlayerList(): # SINGLE LINKED LIST
  def __init__(self):
    self.head = None

  def tambah_pemain(self, player):
    new = NodePlayer(player)
    new.next = self.head
    self.head = new
  
  def get_pemain(self, user):
    temp = self.head
    while temp:
      if temp.player.nama == user:
        return temp.player
      temp = temp.next
    return None
#================================================================================================