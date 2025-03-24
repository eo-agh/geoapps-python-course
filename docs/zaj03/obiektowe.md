
## Programowanie obiektowe - wstęp

Jest to paradygmat programowania, który opiera się na tworzeniu obiektów – elementów, które łączą dane i logikę w spójną całość. Każdy obiekt reprezentuje pewien byt (np. samochód, użytkownik, document) i posiada własne właściwości oraz zachowania.

## Klasa

**Szablon** lub **przepis**, który definiuje strukturę i zachowanie jej instancji. Klasa określa, jakie **atrybuty** (cechy) i **metody** (działania) będą posiadały instancje należące do tej klasy. Przykładowo, klasa `Samochod` może zawierać takie atrybuty, jak `marka`, `model`, `rok`, a także metody jak `przyspiesz()` czy `hamuj()`.

```python
class Samochod:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok
```

Gdy mówimy o **obiektach klasy**, mamy na myśli strukturę (samą definicję), z których można tworzyć instancje.

## Instancja

Konkretny egzemplarz klasy, stworzony na podstawie jej definicji. Instancje posiadają swoje własne wartości atrybutów, choć wszystkie należą do tej samej klasy.

```python
moj_samochod = Samochod('Toyota', 'Corolla', 2020)
```

**Obiekty instancji** (lub po prostu instancje) to konkretne przykłady danej klasy, które istnieją w programie i posiadają własne dane.

## Atrybuty

Przechowują stan obiektu. Każdy atrybut jest częścią obiektu i przechowuje informacje specyficzne dla danej instancji klasy.

Atrybuty można definiować w konstruktorze klasy (metodzie `__init__`), co umożliwia każdej instancji posiadanie indywidualnych wartości.

W naszym przykładzie `marka`, `model` i `rok` to atrybuty.

```python
# Każda instancja posiada swoje własne (inne lub nie; unikatowe lub nie) wartości atrybutów
moj_samochod = Samochod('Toyota', 'Corolla', 2020)
kogos_innego_samochod = Samochod('Ford', 'Focus', 2018)
```

```python
# Dostęp do wartości atrybutów danej instancji klasy
print(moj_samochod.model)
```

## Metody

Funkcje zdefiniowane wewnątrz klasy, które operują na instancjach tej klasy i mogą zmieniać ich stan.

Zwykle w pierwszym argumencie metody umieszcza się `self`, co pozwala na dostęp do atrybutów i innych metod obiektu.

```python
# Rozszerzenie klasy Samochod o metodę przyspiesz
class Samochod:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

    def przyspiesz(self, wartosc: int = 10):
        print(f"{self.marka} {self.model} przyspiesza o {wartosc}!")

moj_samochod.przyspiesz(20)  # wywołanie metody
# Zwraca formatted string: Toyota Corolla przyspiesza o 20!
```

## Po co programować obiektowo?

Programowanie obiektowe (*OOP - ang. object-oriented programming*) jest często stosowane w celu uporządkowania kodu i ułatwienia zarządzania złożonymi projektami.

**Zalety**:

- **Modularność i ponowne wykorzystanie kodu**: OOP sprzyja tworzeniu modułowego kodu, gdzie klasy można wykorzystać wielokrotnie w różnych częściach programu, co zmniejsza ilość powtarzanego kodu i ułatwia modyfikacje.
- **Hermetyzacja**: Dzięki niej można ukryć szczegóły implementacyjne klasy przed użytkownikami, którzy korzystają tylko z interfejsu, co zwiększa bezpieczeństwo kodu i minimalizuje ryzyko przypadkowego naruszenia wewnętrznego stanu obiektu.
- **Dziedziczenie**: Pozwala na tworzenie nowych klas na bazie istniejących, co sprzyja hierarchii i ułatwia rozszerzanie funkcjonalności, redukując potrzebę pisania kodu od podstaw.
- **Polimorfizm**: Dzięki polimorfizmowi różne klasy mogą reagować na te same polecenia w odmienny sposób, co upraszcza zarządzanie różnymi obiektami i zwiększa elastyczność kodu.
- **Lepsze zarządzanie złożonymi systemami**: OOP umożliwia tworzenie struktur, które łatwiej utrzymać w dużych projektach, co jest szczególnie przydatne w złożonych aplikacjach.
- **Łatwość utrzymania i modyfikacji**: Kod obiektowy jest często łatwiejszy do utrzymania, ponieważ klasy i obiekty można modyfikować niezależnie, bez wpływu na inne części systemu.

**Wady**:

- **Wymaga poprzedzającego planowania koncepcyjnego**: Tworzenie kodu obiektowego wymaga wcześniejszego przemyślenia architektury, co może być czasochłonne, zwłaszcza w mniejszych projektach.
- **Złożoność**: Programowanie obiektowe może wydawać się skomplikowane, szczególnie dla początkujących, przez co trudniej nauczyć się i wdrożyć OOP w prostych aplikacjach.
- **Ukrywanie stanu**: Chociaż hermetyzacja jest zaletą, czasem może być wadą – nie zawsze mamy pełny dostęp do informacji o obiekcie, co może ograniczać elastyczność kodu.
- **Wydajność**: Obiektowy kod jest zazwyczaj cięższy i wolniejszy niż podejście proceduralne, co może mieć znaczenie w aplikacjach wymagających wysokiej wydajności.
- **Nadmierna abstrakcja**: Nadmierne stosowanie obiektów i klas może prowadzić do abstrakcji, które nie zawsze są intuicyjne i mogą utrudniać zrozumienie kodu.
- **Nie zawsze najlepsze dopasowanie do przypadków użycia**: W niektórych przypadkach, zwłaszcza przy przetwarzaniu danych, podejście proceduralne jest bardziej efektywne niż OOP, co sprawia, że stosowanie klas i obiektów może być zbędne.

## Dziedziczenie

Kluczowa cecha programowania obiektowego, **pozwala na tworzenie nowych klas na bazie istniejących**. Umożliwia to wykorzystanie już zdefiniowanych atrybutów i metod w nowej klasie, co sprzyja oszczędności kodu i ułatwia jego zarządzanie.

???+ warning "Uwaga"
    Zwróć uwagę w poniższym przykładzie jak wygląda wywoływanie konstruktorów klas nadrzędnych.

```python
class Pojazd:  # Klasa bazowa
    def __init__(self, marka):
        self.marka = marka

    def uruchom(self):
        print(f"{self.marka} jest uruchamiany.")

class Samochod(Pojazd):  # Klasa pochodna
    def __init__(self, marka, model):
        super().__init__(marka)  # Wywołanie konstruktora klasy bazowej
        self.model = model
```

### Wyszukiwanie dziedziczenia

Gdy obiekt wywołuje metodę lub uzyskuje dostęp do atrybutu, Python rozpoczyna process wyszukiwania tego elementu zgodnie z tzw. **MRO** (**Method Resolution Order**) – to algorytm wyszukiwania dziedziczenia:

1. Najpierw sprawdzana jest klasa, do której należy dany obiekt (czyli klasa pochodna).
2. Następnie sprawdzane są klasy bazowe (superklasy) w kolejności od najbliższej do najdalszej.
3. Jeśli Python znajdzie odpowiedni element w pierwszej napotkanej klasie, kończy poszukiwanie.

Klasy mogą także dziedziczyć po więcej niż jednej klasie - nazywamy to **dziedziczeniem wielokrotnym**. W takim wypadku wyszukiwanie z pkt. 2 odbywa się od najbliższej klasy bazowej (wymieniona jako pierwsza przy definiowaniu dziedziczenia) do najdalszej.

```python
class Pojazd:
    def uruchom(self):
        print("Pojazd jest uruchamiany.")

class Silnik:
    def uruchom(self):
        print("Silnik jest uruchamiany.")

class Samochod(Pojazd, Silnik):
    pass

moj_samochod = Samochod()
moj_samochod.uruchom()

## Zwraca: Pojazd jest uruchamiany.
```

Aby sprawdzić kolejność MRO, można użyć metody `.__mro__` lub funkcji `help()`:

```python
print(Samochod.__mro__)
```

Jeśli metoda lub atrybut nie istnieje ani w klasie pochodnej, ani w żadnej z klas bazowych, Python zgłasza błąd, np. `AttributeError`.

### Nadpisywanie (*overriding*)

Process, w którym klasa pochodna definiuje własną wersję metody o tej samej nazwie, co metoda w klasie bazowej. Dzięki temu klasa pochodna może zmienić lub rozszerzyć działanie odziedziczonej metody, dostosowując ją do własnych potrzeb.

???+ warning "Uwaga"
    Zwróć uwagę w poniższym przykładzie jak wygląda specjalizacja odziedziczonych metod.

```python
class Pojazd:
    def uruchom(self):
        print("Pojazd jest uruchamiany.")

class Samochod(Pojazd):
    def uruchom(self):  # Nadpisywanie metody uruchom
        print("Samochód jest uruchamiany szybciej!")
        super().uruchom()  # Wywołanie oryginalnej metody klasy bazowej

moj_samochod = Samochod()
moj_samochod.uruchom()
```

## Przeciążanie operatorów

Technika, która pozwala definiować, jak klasy będą odpowiadać na standardowe operacje, takie jak np. dodawanie, porównywanie czy wyświetlanie reprezentacji tekstowej.

W Pythonie przeciążanie odbywa się przez definiowanie w klasie specjalnych metod (tzw. *dunder methods* – od *double underscore methods*), które zaczynają i kończą podwójnym podkreśleniem (np. `__init__`, `__add__` czy `__str__`).

```python
class Wektor:
    # Ta metoda odpowiada za inicjalizację
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Metoda przeciążająca operator +
    # Definiuje dodawanie wiektora do wektora
    def __add__(self, inny_wektor):
        return Wektor(self.x + inny_wektor.x, self.y + inny_wektor.y)

    # Metoda przeciążająca operator <
    def __lt__(self, inny_wektor):
        return (self.x**2 + self.y**2) < (inny_wektor.x**2 + inny_wektor.y**2)

    # Definiuje tekstową reprezentację obiektu
    def __str__(self):
        return f"Wektor({self.x}, {self.y})"

wektor1 = Wektor(2, 3)
wektor2 = Wektor(1, 1)
suma = wektor1 + wektor2
print(suma)
print(wektor1 < wektor2)
```

??? - "Rozszerzona lista metod do przeciążania operatorów"
    | Metoda                                                     | Przeciąża                         | Wywoływana dla                                                                                                                |
    | ---------------------------------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
    | `__init__`                                                 | Konstruktor                       | Tworzenie obiektu - `x = Klasa(args)`                                                                                         |
    | `__del__`                                                  | Destructor                        | Zwolnienie obiektu `x`                                                                                                        |
    | `__add__`                                                  | Operator `+`                      | `x + y`, `x += y`, jeśli nie ma `__iadd__`                                                                                    |
    | `__or__`                                                   | Operator \`                       | \` (OR poziomu bitowego)                                                                                                      |
    | `__repr__`, `__str__`                                      | Wyświetlanie, konwersje           | `print(x)`, `repr(x)`, `str(x)`                                                                                               |
    | `__call__`                                                 | Wywołanie funkcji                 | `x(*args, **kargs)`                                                                                                           |
    | `__getattr__`                                              | Odczytanie atrybutu               | `x.niezdefiniowany_atrybuty`                                                                                                  |
    | `__setattr__`                                              | Przypisanie atrybutu              | `x.atrybut = wartosc`                                                                                                         |
    | `__delattr__`                                              | Usuwanie atrybutu                 | `del x.atrybut`                                                                                                               |
    | `__getattribute__`                                         | Przechwytywanie atrybutu          | `x.atrybut`                                                                                                                   |
    | `__getitem__`                                              | Indeksowanie, wycinanie, iteracje | `x[klucz]`, `x[i:j]`, pętle `for` oraz inne iteracje, jeśli nie ma `__iter__`                                                 |
    | `__setitem__`                                              | Przypisanie indeksu i wycinka     | `x[klucz] = wartosc`, `x[i:j] = sekwencja`                                                                                    |
    | `__delitem__`                                              | Usuwanie indeksu i wycinka        | `del x[klucz]`, `del x[i:j]`                                                                                                  |
    | `__len__`                                                  | Długość                           | `len(x)`, testy prawdziwości, jeśli nie ma `__bool__`                                                                         |
    | `__bool__`                                                 | Testy logiczne                    | `bool(x)`, testy prawdziwości                                                                                                 |
    | `__lt__`, `__gt__`, `__le__`, `__ge__`, `__eq__`, `__ne__` | Porównania                        | `x < y`, `x > y`, `x <= y`, `x >= y`, `x == y`, `x != y`                                                                      |
    | `__radd__`                                                 | Prawostronny operator `+`         | `nieinstancja + x`                                                                                                            |
    | `__iadd__`                                                 | Dodawanie w miejscu (rozszerzone) | `x += y`                                                                                                                      |
    | `__iter__`, `__next__`                                     | Konteksty iteracyjne              | `i = iter(x)`, `next(i)`; pętle `for`, jeśli nie ma `__contains__`, testy `in`, wszystkie listy składanie, funkcje `map(f,x)` |
    | `__contains__`                                             | Test przynależności               | `item in x` (dowolny iterator)                                                                                                |
    | `__index__`                                                | Wartość całkowita                 | `hex(x)`, `bin(x)`, `oct(x)`, `o[x]`, `o[x:]`                                                                                 |
    | `__enter__`, `__exit__`                                    | Menedżer konktekstu               | `with obj as var:`                                                                                                            |
    | `__get__`, `__set__`, `__delete__`                         | Atrybuty deskryptorów             | `x.attr`, `x.attr = value`, `del x.attr`                                                                                      |
    | `__new__`                                                  | Tworzenie instancji               | Tworzenie instancji, przed `__init__`                                                                                         |

## Tworzenie klas - przykład

## 📝 Zadanie

Wejdź do repozytorium, zapoznaj się z gotowym kodem w pliku `main_zajecia03.py` oraz modułami w folderze `geoapps/zajecia03`.

Zwróć uwagę na:

- Tworzenie konstruktorów - `__init__`,
- Dodawanie metod,
- Tekstową reprezentację klas - `__str__` oraz `__repr__` (jak przykład przeciążania operatorów),
- Dostosowywanie klas poprzez klasy podrzędne.

## Narzędzia introspekcji

Introspekcja pozwala na dynamiczne badanie obiektów, ich struktur oraz cech w czasie działania programu.

**`__class__`**

Atrybut ten pozwala na sprawdzenie klasy, do której należy dany obiekt.

```python
class Zwierze:
    pass

class Pies(Zwierze):
    pass

reksio = Pies()
print(reksio.__class__)  # <class '__main__.Pies'>
print(reksio.__class__.__name__)  # Pies
```

**`__dict__`**

Atrybut ten to słownik, który przechowuje wszystkie atrybuty instancji obiektu. Dzięki __dict__ można dynamicznie uzyskać dostęp do atrybutów obiektu, modyfikować je, dodawać now lub iterować po nich.

```python
class Samochod:
    def __init__(self, marka, model, rok):
        self.marka = marka
        self.model = model
        self.rok = rok

moj_samochod = Samochod("Toyota", "Corolla", 2020)
print(moj_samochod.__dict__) # {'marka': 'Toyota', 'model': 'Corolla', 'rok': 2020}
```

## Abstrakcyjne klasy nadrzędne

Są to klasy służące jako szablony, które definiują strukturę i wymuszone metody dla klas pochodnych, ale same nie mogą być inicjalizowane. Używają dekoratora `@abstractmethod` do oznaczenia metod, które muszą być zaimplementowane w klasach pochodnych.

??? - tip "Korzyści wynikające z wykorzystywania abstrakcyjnych klas nadrzędnych"
    - **Spójność** – wymusza implementację określonych metod.
    - **Reużywalność** – pozwala dzielić metody między klasami.
    - **Polimorfizm** – umożliwia jednolite używanie różnych klas.

```python
from abc import ABC, abstractmethod

class Zwierze(ABC):
    # Ta metoda jest abstrakcyjna,
    # wymagana jest jej implementacja w klasach pochodnych
    @abstractmethod
    def wydaj_dzwiek(self):
        pass

class Pies(Zwierze):
    def wydaj_dzwiek(self):
        return "Hau hau!"

class Kot(Zwierze):
    def wydaj_dzwiek(self):
        return "Miau miau!"
```

## Atrybuty pseudoprywatne

Atrybuty, których nazwy zaczynają się od dwóch podkreślników, np. `__nazwa`. Taka konwencja nazw powoduje, że Python stosuje *name mangling* – czyli zmienia nazwę atrybutu w taki sposób, że jest trudniej dostępna z zewnątrz klasy, ale nie jest całkowicie prywatna. Jest to bardziej forma ochrony, niż pełne ukrycie atrybutów.

```python
class MojaKlasa:
    def __init__(self):
        self.__ukryty_atrybut = "tajne"

    def pokaz_ukryty(self):
        return self.__ukryty_atrybut

obiekt = MojaKlasa()
print(obiekt.pokaz_ukryty())  # Poprawne: "tajne"
print(obiekt._MojaKlasa__ukryty_atrybut)  # Dostęp poprzez name mangling: "tajne"
```

??? - tip "Po co używać atrybutów pseudoprywatnych?"
    - **Ochrona przed przypadkowym nadpisaniem** – przy dziedziczeniu klasy istnieje mniejsze ryzyko, że klasa pochodna przypadkowo nadpisze atrybut o tej samej nazwie.
    - **Czytelność** – pokazują, że atrybut nie jest przeznaczony do bezpośredniego użytku z zewnątrz klasy.

## Rozszerzanie typów wbudowanych

Może być przydatne, gdy chcemy dodać dodatkową funkcjonalność lub dostosować zachowanie istniejących typów (np. `list`, `dict`, `str`) do specyficznych potrzeb projektu.

### Za pomocą osadzania (kompozycja)

Poprzez utworzenie nowej klasy, która wewnętrznie przechowuje instancję typu wbudowanego jako atrybut.

W ten sposób klasa ta może wykorzystywać typ wbudowany i rozszerzać jego funkcjonalność, delegując operacje na ten typ, ale nie dziedziczy jego metod bezpośrednio. Osadzanie jest przydatne, gdy chcemy dodać now funkcje bez ingerencji w istniejące metody typu wbudowanego.

```python
class MojaLista:
    def __init__(self, elementy):
        self._lista = elementy  # Osadzenie typu wbudowanego list

    def suma(self):
        return sum(self._lista)

    def dodaj(self, element):
        self._lista.append(element)

    def __str__(self):
        return str(self._lista)

moja_lista = MojaLista([1, 2, 3])
moja_lista.dodaj(4)
print(moja_lista)        # [1, 2, 3, 4]
print(moja_lista.suma()) # 10
```

### Za pomocą klas podrzędnych (dziedziczenia)

Poprzez utworzenie klasy podrzędnej, która dziedziczy po typie wbudowanym. Dzięki temu klasa podrzędna automatycznie przejmuje wszystkie metody i atrybuty typu bazowego, co pozwala na łatwe dodanie nowych funkcji lub nadpisanie istniejących metod.

```python
class MojaLista(list):
    def suma(self):
        return sum(self)

moja_lista = MojaLista([1, 2, 3, 4])
print(moja_lista)         # [1, 2, 3, 4]
print(moja_lista.suma())  # 10
```

??? - tip "Za i przeciw dla obu sposobów"
    |               | Za                                                                                                                                                                                                                                   | Przeciw                                                                                                                                                                                                                                                                                                                                |
    | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | Osadzanie     | Daje pełną kontrolę nad metodami, które są dostępne dla użytkownika klasy. Izoluje funkcjonalność rozszerzonego typu od interfejsu klasy bazowej, co może zwiększyć bezpieczeństwo i ułatwić utrzymanie kodu.                        | Wymaga ręcznego implementowania delegacji metod, jeśli potrzebujemy pełnego dostępu do funkcji typu wbudowanego. Może być mniej wydajne i bardziej czasochłonne niż dziedziczenie, jeśli chcemy używać większości metod typu wbudowanego.                                                                                            |
    | Dziedziczenie | Klasa pochodna automatycznie przejmuje wszystkie metody typu wbudowanego, co ułatwia tworzenie nowych funkcji. Jest bardziej ekonomiczne i intuicyjne w implementacji, szczególnie gdy potrzebujemy tylko kilku dodatkowych funkcji. | Trudniej jest zmodyfikować sposób działania niektórych metod w typach wbudowanych, ponieważ metody te mogą wywoływać bezpośrednie operacje na strukturze danych. Dziedziczenie może prowadzić do problemów z nieoczekiwanym zachowaniem, jeśli metody typu wbudowanego nie są dobrze przystosowane do nowych funkcji klasy pochodnej. |

## Sloty

Specjalny mechanizm, który pozwala na optymalizację pamięci obiektów klasy, poprzez ograniczenie listy atrybutów, które można dodać do instancji danej klasy.

```python
class Osoba:
    __slots__ = ['imie', 'wiek']  # Ograniczamy atrybuty tylko do 'imie' i 'wiek'

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

osoba = Osoba("Jan", 30)
print(osoba.imie)  # Jan
print(osoba.wiek)  # 30

# Próba dodania nowego atrybutu zgłosi błąd
osoba.address = "Warszawa"  # AttributeError: 'Osoba' object has no attribute 'address'
```

Python przestaje używać dynamicznego słownika `__dict__` do przechowywania atrybutów obiektu, co ogranicza możliwość dodawania nowych atrybutów poza tymi zdefiniowanymi w `__slots__`, ale jednocześnie zmniejsza ilość zużywanej pamięci.

## Rodzaje metod w klasach

### Metody instancji

Domyślny sposób działania, jako pierwszy argument przyjmują `self`, który odnosi się do instancji.

!!! tip "Zastosowanie: operacje na instancji"

### Metody klasy

Deklarowane za pomocą dekoratora `@classmethod`. Przyjmują jako pierwszy argument `cls`, który odnosi się do samej klasy, a nie jej instancji.

```python
class Pracownik:
    liczba_pracownikow = 0  # Atrybut klasy

    def __init__(self, imie, stanowisko):
        self.imie = imie
        self.stanowisko = stanowisko
        Pracownik.liczba_pracownikow += 1

    @classmethod
    def z_nazwiska(cls, nazwisko):
        # Alternatywny konstruktor
        return cls(nazwisko, 'Nieznane stanowisko')

    @classmethod
    def ustaw_liczbe_pracownikow(cls, liczba):
        cls.liczba_pracownikow = liczba

# Tworzenie instancji za pomocą metody klasy
nowy_pracownik = Pracownik.z_nazwiska('Kowalski')
print(nowy_pracownik.imie)           # Kowalski
print(nowy_pracownik.stanowisko)     # Nieznane stanowisko
```

!!! tip "Zastosowanie: operacje na klasie, alternatywne konstruktory"

### Metody statyczne

Deklarowane za pomocą dekoratora `@staticmethod`. Nie przyjmują żadnego specjalnego pierwszego argumentu i nie mają dostępu ani do instancji (`self`), ani do klasy (`cls`).

```python
class Kalkulator:
    @staticmethod
    def dodaj(a, b):
        return a + b

    @staticmethod
    def odejmij(a, b):
        return a - b

# Wywoływanie metod statycznych
print(Kalkulator.dodaj(5, 3))     # 8
print(Kalkulator.odejmij(10, 4))  # 6
```

!!! tip "Zastosowanie: funkcje pomocnicze powiązane tematycznie"

### Zadanie

Zapoznaj się z metodami w klasie z `src.zajecia04.fleet.ambulance`.

## Zadania

Dodaj następujące funkcjonalności do programu przedstawionego jako przykład. Dla wszystkich dodanych funkcjonalności stwórz przykładowy kod potwierdzający, że działają (rozbudowując kod w `run_zajecia04.py`).

1. Zmodyfikuj każdą klasę tak, żeby posiadała atrybut `__max_id`, który będzie wykorzystywany do nadawania identyfikatorów kolejnym stworzonym instancjom (zamiast podawania go jako argument przy inicjalizacji).

2. Rozbuduj klasę Incident o priorytet zdarzenia, czas zgłoszenia i informacje o zgłaszającym.

3. Zaprojektuj w ramach subpakietu `fleet` klasę `Station`, każda stacja ma posiadać identyfikator, lokalizację, karetkę, kierowcę i 1 dodatkowego pracownika. Napisz metodę, która sprawdza czy karetka jest na miejscu (czy zgadzają się lokalizacje).

4. Rozbuduj aplikację (w tym zaprojektuj logikę, ale także elementy, które trzeba dodać w różnych klasach (niekoniecznie istniejących) o możliwość zarządzania incydentami – przydzielanie karetek do zgłaszanych zdarzeń. Te funkcjonalności muszą uwzględniać:

    - Priorytet i czas, który upłynął od zgłoszenia,
    - Aktualny stan, w którym znajduje się karetka,
    - Odległość karetki od zdarzenia.