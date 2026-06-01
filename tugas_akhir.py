class Entitas:
  def __init__(self, nama, hp = 100, attack = 10):
    self.nama = nama
    self.hp = hp
    self.max_hp = hp
    self.attack = attack

class Player(Entitas):
  def __init__(self, nama, role = 'fighter'):
    super().__init__(nama)
    self.nama = nama
    self.exp = 0
    self.level = 1
    self.role = role
    self.gold = 0
    self.inventory = None

    if role == 'tank':
      self.hp =  150
      self.attack = 5
    elif role == 'marksman':
      self.hp = 80
      self.attack = 15

class Enemy(Entitas):
  def __init__(self, nama, hp, attack, reward):
    super().__init__(nama, hp, attack)
    self.reward = reward

class Item:
  def __init__(self, nama, jenis, power, harga):
    self.nama = nama
    self.jenis = jenis
    self.power = power
    self.harga = harga

toko = [
  Item('heal potion', 'heal', 30, 30),
  Item('attack potion', 'buff', 10, 30)
]

class Login(): #hash table
  def __init__(self, size = 10):
    self.size = size
    self.table = [None] * size

  def hash(self, key):
    jumlah = 0
    for i in key:
      jumlah += ord(i)
    return jumlah % self.size

  def register(self, username, pw):
    index = self.hash(username)
    self.table[index] = pw

  def cek(self, username, pw):
    index = self.hash(username)
    return self.table[index] == pw
  
class NodePlayer(): #single linked list
  def __init__(self, player):
    self.player = player
    self.next = None

class PlayerList(): # single linked list
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


