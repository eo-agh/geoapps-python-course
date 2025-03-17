## Pętle z licznikami

`range(n)` tworzy sekwencję liczb od `0` do `n-1`. Możemy używać tej funkcji do iteracji w pętli, np. do kontrolowania liczby powtórzeń.

```python
for i in range(6):
    print(f"Licznik: {i}")
```

Funkcja `enumerate()` pozwala jednocześnie uzyskać indeks i wartość z listy.

```python
owoce = ["jabłko", "banan", "wiśnia"]
for idx, owoc in enumerate(owoce):
    print(f"Indeks: {idx}, Owoc: {owoc}")
```

## Skanowanie sekwencji

Skanowanie sekwencji oznacza przechodzenie przez każdy element w liście, krotce, lub innym iterowalnym obiekcie.

```python
owoce = ['jabłko', 'banan', 'pomarańcza']
for owoc in owoce:
    print(owoc)
```

## Przetasowanie sekwencji

`range(len(x))` iteruje po indeksach sekwencji. Może być użyte do manipulacji elementami na podstawie ich indeksów.

```python
owoce = ['jabłko', 'banan', 'pomarańcza']
for i in range(len(owoce)):
    owoce[i] = owoce[i].upper()
print(owoce)
```

## Przechodzenie niewyczerpujące

`range(0, len(x), 2)` lub `x[::2]`

```python
liczby = [1, 2, 3, 4, 5, 6]
for i in range(0, len(liczby), 2):
    print(liczby[i])

# Alternatywnie, z użyciem slicing
print(liczby[::2])
```

## Listy składane

Lista składana to wyrażenie, które pozwala na tworzenie nowych list w zwięzły sposób, zwykle z użyciem pętli.

```python
kwadraty = [x ** 2 for x in range(6)]
print(kwadraty)
```

```python
liczby = [1, 2, 3, 4, 5, 6]
parzystosc = ['parzysta' if liczba % 2 == 0 else 'nieparzysta' for liczba in liczby]
print(parzystosc)
```

## Przechodzenie równoległe

`zip` umożliwia równoległe iterowanie po wielu sekwencjach, a `map` stosuje funkcję do każdego elementu sekwencji.

```python
imiona = ['Anna', 'Jan', 'Piotr']
wieki = [25, 30, 35]
for imie, wiek in zip(imiona, wieki):
    print(f"{imie} ma {wiek} lat")
```

```python
def kwadrat(liczba):
    return liczba ** 2

liczby = [1, 2, 3, 4]
kwadraty = list(map(kwadrat, liczby))
print(kwadraty)
```

## 📝 Zadania

1. Mając dwie listy, `imiona = ['Anna', 'Jan', 'Ewa']` i `oceny = [5, 4, 3]`, użyj `zip` do stworzenia pary każdego imienia z odpowiadającą mu oceną. Następnie, iteruj przez te pary, wyświetlając imię wraz z oceną. Co się stanie, jeśli listy będą miały różne długości?

2. Mając listę `liczby = [1, 2, 3, 4, 5]`, napisz funkcję `kwadrat(x)`, która zwraca kwadrat liczby x. Użyj map z tą funkcją, aby stworzyć nową listę, w której każdy element jest kwadratem odpowiadającego mu elementu z listy liczby. Wyświetl tą listę.

## Iteratory

Iterator to obiekt w Pythonie, który pozwala na sekwencyjne przetwarzanie elementów kolekcji (np. list, krotek, zbiorów) **bez załadowania całej struktury do pamięci**. Iteratory umożliwiają przechodzenie po elementach jeden po drugim, co jest efektywne, szczególnie przy pracy z dużymi zbiorami danych.

Każda pętla `for` działa na iteratorach w tle.

??? - note "Jak działają iteratory?"
    - Każdy obiekt, który ma metodę `__iter__()` i `__next__()`, jest iteratorem.
    - Metoda `__iter__()` zwraca iterator, a `__next__()` zwraca kolejny element. Gdy elementów zabraknie, zgłaszany jest wyjątek `StopIteration`.

??? - note "Po co nam iteratory?"
    - Efektywność pamięciowa: Przetwarzają elementy na bieżąco, nie muszą trzymać całej kolekcji w pamięci.
    - Niekończące się sekwencje: Można tworzyć iteratory, które generują nieskończone sekwencje danych, np. liczby losowe.

```python
liczby = [1, 2, 3]
it = iter(liczby)
print(next(it))
print(next(it))
print(next(it))
```

## 📝 Zadanie dodatkowe

Stwórz własny iterator (klasę) `FibonacciIterator(max_elements)`, który generuje ciąg liczb Fibonacciego. Ciąg Fibonacciego to sekwencja, w której każda kolejna liczba jest sumą dwóch poprzednich, a zaczyna się od 0 i 1.
