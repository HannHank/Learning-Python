#So das ist mal ein kleines programm um mal ein bisschen die Grundstruktur von Python zu verstehen 

class Person:
  def __init__(self, name, age): #das ist eine init Funktion eine Classe, diese wird immer nur einmal ausgeführt. Das ist manchmal ganz hilfreich wenn man Variablen definieren möchte 
    self.name = name  #hier wird die vaiable "name" in "self.name" gespeichert, somit können andere Funktionen in dieser Classe auf diese Variable zugreifen
    self.age = age  # der selbe spass mit "age"

  def myfunc(self): #es ist ein bisschen verwirrent, aber in Python werden Funktionen in Classen immer mit einem "self" definiert. "self" ist einfach "0"
    print("Hello my name is " + self.name)#hier printen wir den Namen und vor die Variable scheiben wir "self" damit wir den oben definierten Wert bekommen. 
    print("and my Age is ", self.age)

p1 = Person("John", 36)#in dieser Zeile wird ein Object von der Classe Person erzeugt. Und die Werte werden übergeben 
p1.myfunc() #hier wird jetzt die Funktion von dem Object aufgerufen


#Aber warum nutzt man classen und erzeugt Objecte ? 
#Das coole an Classen ist das man sie beliebig oft Objecten zu weisen kann
#Das bedeutet wir können das ganz einfach mit einem anderen Namen und einem anderem alter machen 
#einfach einkommentieren
# p2 = Person("Seb",25)
# p2.myfunc()


#diesen stuff würde man auch mit nur einer Funktion hinbekommen, aber bei großen Programmen nutzt man für die Übersicht immer Classen. 