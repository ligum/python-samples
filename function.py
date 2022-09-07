from re import M


def main():
    myname = "XXXXX"
    print(myname)
main()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()
myfunc()

xa = 300
def dudu():
  xa = 200
  print(xa)
dudu()
print(xa)

xyz = 300
def myfunc():
  global xyz
  xyz = 200
myfunc()
print(xyz)