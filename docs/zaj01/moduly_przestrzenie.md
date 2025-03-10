## Wprowadzenie
W Pythonie moduły i przestrzenie nazw odgrywają kluczową rolę w organizacji kodu. Moduły pozwalają na podzielenie kodu na mniejsze, łatwiejsze w zarządzaniu części, a przestrzenie nazw pomagają uniknąć konfliktów pomiędzy nazwami zmiennych, funkcji czy klas.

---

## Moduły w Pythonie

### Czym jest moduł?
Moduł w Pythonie to plik `.py`, który zawiera zmienne, funkcje i klasy. Dzięki nim można podzielić kod na niezależne sekcje, co ułatwia jego ponowne użycie oraz utrzymanie.

#### Tworzenie i używanie modułu
Załóżmy, że chcemy stworzyć moduł do operacji matematycznych. Tworzymy plik `matematyka.py`:
```python
def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b
```
Teraz możemy zaimportować go w innym skrypcie:
```python
import matematyka

wynik = matematyka.dodaj(5, 3)
print(f'Wynik dodawania: {wynik}')
```

Możemy też importować tylko wybrane funkcje:
```python
from matematyka import odejmij

wynik = odejmij(10, 4)
print(f'Wynik odejmowania: {wynik}')
```

---

## Przestrzenie nazw

Przestrzeń nazw to mechanizm pozwalający unikać konfliktów między zmiennymi i funkcjami. Python organizuje przestrzenie nazw w hierarchiczny sposób:
1. **Lokalna** – zmienne wewnątrz funkcji,
2. **Globalna** – zmienne zadeklarowane w module,
3. **Wbudowana** – standardowe funkcje Pythona jak `print()`.

#### Przykład użycia przestrzeni nazw
```python
x = 10  # Zmienna globalna

def funkcja():
    x = 5  # Zmienna lokalna
    print(f'Wartość x wewnątrz funkcji: {x}')

funkcja()
print(f'Wartość x na poziomie globalnym: {x}')
```

## Podsumowanie
1. **Moduły** pomagają organizować kod i unikać powielania funkcji.
2. **Przestrzenie nazw** zapobiegają konfliktom nazw i organizują zmienne w hierarchii.

Dzięki tym mechanizmom Python zapewnia elastyczność w organizacji kodu i jego efektywne zarządzanie!

## 📝 Zadania

  1. Z pakietu `os` zaimportuj funkcję `getcwd`
     ```python
     from os import getcwd
     ```
  2. Wywołaj funkcję i przypisz wynik do zmiennej `current_path`
  3. Wypisz wartość zmiennej `current_path`
  4. Stwórz plik `czas.py`
  5. W pliku `czas.py` dodaj zmienną `aktualny_czas`:
     ```python
     from datetime import datetime
     aktualny_czas = datetime.now()
     ```
  6. Zaimportuj moduł `czas` w `skrypt1.py`
  7. Wypisz wartość zmiennej `aktualny_czas`
  8. Zaimportuj pakiet `time` i dodaj opóźnienie:
     ```python
     import time
     time.sleep(20)
     ```
  9. Ponownie wypisz wartość zmiennej `aktualny_czas`
  10. Przeładuj moduł `czas` (`importlib.reload()`)
  11. Po raz trzeci wypisz wartość zmiennej `aktualny_czas`

Zwróć uwagę na to, kiedy zmieniła się wartość zmiennej. Zastanów się, kiedy inicjowana jest zmienna `aktualny_czas`. 