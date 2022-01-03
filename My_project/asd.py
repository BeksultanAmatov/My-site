import random
import string


class Sort():
  def make_sort(self,arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if len(arr[i]) > len(arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr


class GenPassword(Sort):
    def __init__(self):
      self.l = []
      self.lower = string.ascii_lowercase
      self.upper = string.ascii_letters
      self.digit = string.digits
    def gen_password(self):
      while True:
        num = int(input("enter a lenght of password: "))
        geneartors = [lambda: random.choice(self.lower),
            lambda: random.choice(self.upper),
            lambda: random.choice(self.digit)]
        passw = "".join([x() for x in geneartors])[:num]
        print(passw)

        self.l.append(passw)

        make_end = input("Do you want to repeate?: ")
        if make_end =="yes" or make_end=="y":
          continue
        if make_end=="no" or make_end=="n":
          break
        if make_end=="check":
          print(self.l)
        if make_end == "diff":
          diff_sort = self.make_sort(self.l)
          print(diff_sort)


class Diff(Sort):
    def make_diff(self):
      while True:
        num = input("enter your password: ")
        d = {"e":"3","i":"1","a":"@","o":"0","b":"6","m":"w","s":"$","8":"&","l":"L","t":"7","w":"W","r":"R"} 
        passw = "".join(d[i] if i in d else i for i in num)
        print(passw)
        self.l.append(passw)
        make_end = input("Do you want to repeate?: ")
        if make_end =="yes" or make_end=="y":
          continue
        elif make_end=="no" or make_end=="n":
          break
        elif make_end=="check":
          print(self.l)
        elif make_end == "diff":
          diff_sort = self.make_sort(self.l)
          print(diff_sort)


class Main(Diff,GenPassword):
    def diff_get(self):
        d = self.make_diff()
    def gen_get(self):
        g = self.gen_password()


main=Main()
choice = int(input("""Number 1)Write your password and the programe will make it more difficult
Number 2) Write a lenght of password and the programe will generate your new password
>>>>Make your choice(1/2): """))
if choice== 1:
  main.diff_get()
elif choice==2:
  main.gen_get()



