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

def main():
  lala = Login()
  listpemain = PlayerList()
  p_aktif = None
  while True:
    if not p_aktif:
      print("\n=== BATTLE ARENA (PROGRES 20%) ===")
      print("1. Login\n2. Register\n3. Keluar Game")
      opsi = int(input("Pilih menu: "))
      if opsi == 1:
        user = input('username:')
        pas = input('password: ')
        if lala.cek(user, pas):
          p_aktif = listpemain.get_pemain(user)
          if p_aktif:
            print(f'\nLogin sukses. Welcome {p_aktif.nama}')
        else:
          print('Login gagal')

      elif opsi == 2:
        user_baru = input('Username:')
        pas_baru = input('Password: ')
        while True:
            try:
              print('Pilih role:\n' \
              '1. fighter\n' \
              '2. tank\n' \
              '3. marksman\n')
              t = int(input('Pilih: '))
              if t == 1:
                role = 'fighter'
                break
              elif t == 2:
                role = 'tank'
                break
              elif t == 3:
                role = 'marksman'
                break
              else:
                print('Pilih antara 1/2/3!!')
            except ValueError:
              print('Masukkan angka 1/2/3')
        new_player = Player(user_baru, role)
        lala.register(user_baru, pas_baru)
        listpemain.tambah_pemain(new_player)
        print('Registrasi berhasil')

      elif opsi == 3:
        print("Keluar")
        break
    
    else:
      print(f"\n=== MAIN MENU | Player: {p_aktif.nama} ({p_aktif.role}) ===")
      print("1. Battle (Tahap Pengembangan)")
      print("2. Toko (Tahap Pengembangan)")
      print("3. Logout")

      opsi = int(input('Pilih: '))
      if opsi == 1:
        print('Belum selesai')
      elif opsi == 2:
        print('Belum selesai')
      elif opsi == 3:
        p_aktif = None
        print('Logout')

if __name__ == "__main__":
    main()


