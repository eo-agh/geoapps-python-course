## Wstęp

Funkcje pozwalają na organizowanie i strukturyzowanie kodu w logiczne bloki, które można wielokrotnie wywoływać. Dzięki funkcjom możemy **uprościć programy**, **zmniejszyć ilość powtarzającego się kodu**, a także sprawić, że nasze rozwiązania staną się bardziej **modularne** i **łatwiejsze do utrzymania**.

Zalety używania funkcji:

- **Modularność** - dzielisz duży problem na mniejsze części, które są łatwiejsze do zarządzania.

- **Ponowne wykorzystanie** - funkcję można wywoływać wielokrotnie w różnych miejscach programu.

- **Łatwiejsze utrzymanie** - zmiana logiki w jednym miejscu (w funkcji) automatycznie wprowadza zmiany w całym programie.

- **Czytelność** - funkcje pomagają tworzyć bardziej zrozumiały i uporządkowany kod.

```python
import random
def generuj_losowa(seed=None):
    # Ustawienie ziarna (seed) generatora liczb losowych
    if seed is not None:
        random.seed(seed)
    # Generowanie losowej liczby z zakresu od 0 do 100
    return random.randint(0, 100)

liczba = generuj_losowa(seed=42)
print(f"Wygenerowana liczba: {liczba}")
```

Trzy kluczowe elementy każdej funkcji:

1. Słowo kluczowe służace definiowaniu funkcji - `def`

2. Argumenty: definiowanie i podawane wewnątrz `()`

3. Zwracane wartości - słowo kluczowe `return`

## 📝 Zadania

1. Napisz funkcję `zmien_wartosc(arg)`, która przyjmuje jeden argument i próbuje zmodyfikować ten argument w różny sposób w zależności od tego, czy jest on niemutowalny (w tym przypadku integerem) czy mutowalny (w tym przypadku listą).

    - Jeśli jest listą, wykonaj `arg[0] = 'kalafior'`.

    - Jeśli jest integerem, wykonaj `arg = 65482652`.

Wypisz przykłady dla obu przypadków, wypisz wartości przed i po wykonaniu funkcji. Jak się zachowują te obiekty?

!!! tip
    Warto skorzystać z funkcji `isinstance()`.

??? - note "Teoria: mutowalne i niemutowalne obiekty w funkcjach"
    Kiedy zmienne są przekazywane do funkcji jako argumenty, Python nie tworzy ich kopii, lecz przekazuje referencję do oryginalnego obiektu. W związku z tym sposób, w jaki te obiekty zachowują się wewnątrz funkcji, zależy od ich typu – mutowalne lub niemutowalne.

    **Obiekty mutowalne** (np. listy, słowniki):

    Zmienne tego typu mogą być modyfikowane w miejscu. Jeśli zostaną przekazane jako argumenty do funkcji i ich zawartość zostanie zmieniona, zmiana ta wpłynie na oryginalny obiekt, który istnieje poza funkcją.

    **Obiekty niemutowalne** (np. liczby, napisy, krotki):

    Zmienne niemutowalne nie mogą być modyfikowane w miejscu. Każda próba modyfikacji powoduje utworzenie nowego obiektu. Z tego powodu, zmiany wprowadzone wewnątrz funkcji nie wpływają na oryginalny obiekt poza funkcją.

## Dopasowywanie argumentów

Funkcje mogą przyjmować argumenty na różne sposoby, co umożliwia elastyczne przekazywanie danych. Kluczowe elementy to: **argumenty pozycyjne**, **argumenty nazwane**, **wartości domyślne**, oraz specjalne operatory **`*args`** i **`**kwargs`**, które pozwalają na przekazywanie zmiennej liczby argumentów.

```python
# dodanie wartości domyślnych
def dodaj(a = 0, b = 0):
    return a + b

# argumenty pozycyjne przekazywane są w podanej kolejności
print(dodaj(3, 5))

# argumenty nazwane można mieszać
print(b=5, a=3)
```

**`*args` - zmienna liczba argumentów pozycyjnych**

Wszystkie dodatkowe argumenty są zbierane w **krotkę**, dzięki czemu możemy obsłużyć więcej argumentów, niż zdefiniowano w sygnaturze funkcji.

```python
def suma(*liczby):
    return sum(liczby)

print(suma(1, 2, 3))
print(suma(10, 20))
```

**`**kwargs` – zmienna liczba argumentów nazwanych**

Argumenty są zbierane w **słownik**, co umożliwia przekazanie większej liczby argumentów nazwanych, niż przewidziano w sygnaturze funkcji.

```python
def przedstaw_sie(**dane):
    for klucz, wartosc in dane.items():
        print(f"{klucz}: {wartosc}")

przedstaw_sie(imie="Jan", wiek=30, miasto="Kraków")
```

??? - danger "Mieszane użycie argumentów nie zawsze jest możliwe"
    Ważne jest, aby przestrzegać kolejności: **najpierw argumenty pozycyjne, potem domyślne, następnie `*args`, a na końcu `**kwargs`**.

    ```python
    def funkcja_mieszana(a, b=10, *args, **kwargs):
        print(f"a: {a}, b: {b}")
        print(f"Argumenty dodatkowe (args): {args}")
        print(f"Argumenty nazwane (kwargs): {kwargs}")

    funkcja_mieszana(1, 2, 3, 4, imie="Ania", wiek=25)
    ```

    Oraz kilka niepoprawnych wywołań:

    ```python
    funkcja_mieszana()
    funkcja_mieszana(1, 2, 3, 4, 5, a=6)
    funkcja_mieszana(1, 2, 3, imie="Jan")
    funkcja_mieszana(a=1, 20)
    ```

    Sama definicja również może być niepoprawna:

    ```python
    def funkcja_mieszana(a=10, b):
        print(f"a: {a}, b: {b}")
    ```

## 📝 Zadania

1. Napisz funkcję `zamowienie_produktu`, która przyjmuje jeden obowiązkowy argument pozycyjny `nazwa_produktu` i dwa obowiązkowe argumenty nazwane: `cena` i `ilosc`. Funkcja powinna zwracać text podsumowujący zamówienie, zawierające nazwę produktu, łączną cenę (cena * ilość) oraz ilość zamówionego produktu.

    - Stwórz pustą listę, do której wstawisz wartości zwracane przez funkcję dla 3 różnych produktów.

    - Przeiteruj po wypełnionej liście, wyświetl teksty.

    - Zmodyfikuj funkcję tak, żeby oprócz tekstu podsumowującego zwracała także wartość zamówienia.

    - Na koniec wyświetl sumaryczną wartość zamówień (sumę z każdego zamówionego produktu).

    - Dodaj wartość domyślną dla argumentu `ilosc` równą 1.

!!! warning "Ważna informacja"
    Wykorzystaj poniższy początek definicji i go nie modyfikuj. Wymusi to podawanie argumentów po gwiazdce jedynie w formie nazwanej.

    ```python
    def zamowienie_produktu(nazwa_produktu, *, cena, ilosc):
    ```

1. Napisz funkcję `stworz_raport`, która przyjmuje dowolną liczbę argumentów pozycyjnych (`*args`) i nazwanych (`**kwargs`). Argumenty pozycyjne powinny reprezentować numery ID produktów, a argumenty nazwane - informacje o tych produktach (np. nazwa, cena). Funkcja powinna tworzyć i wyświetlać raport, w którym dla każdego ID produktu podane są szczegółowe informacje na jego temat.

Wywołanie funkcji powinno wyglądać następująco:

```python
stworz_raport(101, 102, nazwa_101="Kubek termiczny", cena_101="45.99 zł", nazwa_102="Długopis", cena_102="4.99 zł")
```

## Funkcje - praktyczne porady

1. Funkcje powinny być niezależne od otoczenia - argumenty jako input, return jako output.
2. Unikamy zmiennych globalnych.
3. Nie modyfikujemy argumentów mutowalnych.
4. Funkcja ma być mała i mieć jeden cel.
5. Nie zmieniamy wartości zmiennych z innych modułów.

## Atrybuty

Każdy obiekt w Pythonie może mieć swoje atrybuty. Służą one przechowywaniu dodatkowych informacji na ich temat lub umożliwiają dostęp do ich stanów wewnętrznych.

Do atrybutów odwołujemy się za pomocą notacji kropkowej, np. `obiekt.atrybut`. Funkcje, tak samo jak inne obiekty, mogą mieć swoje atrybuty.

```python
def sample_function():
    return "Hello, world!"

sample_function.description = "To jest przykładowa funkcja."  # Dodanie niestandardowego atrybutu
print(sample_function.description)
```

## Adnotacje

Jest to sposób na dodawanie informacji o typach danych używanych w kodzie. Choć Python jest językiem dynamicznie typowanym i nie wymaga jawnego określania typów, adnotacje dają programiście możliwość wskazania, jakie typy danych powinny być używane, co poprawia czytelność i ułatwia pracę w zespołach.

??? - note "Idea adnotacji"
    Adnotacje stanowią coś w rodzaju "podpowiedzi" dla innych programistów oraz narzędzi analizujących kod (np. linterów, IDE), które mogą je wykorzystać do ułatwienia debugowania, uzupełniania kodu, czy znajdowania potencjalnych błędów.

W poniższym przykładzie argument `name` ma być typu `str`, tak samo zwracana przez funkcję wartość.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

Zmienne także mogą posiadać swoje adnotacje.

```python
age: int = 25
name: str = "Alice"
```

Zaawansowane typy importuje się z modułu `typing`.

```python
from typing import List, Optional, Dict

def get_user_info(user_id: int) -> Optional[Dict[str, str]]:
    if user_id == 1:
        return {"name": "Hubert", "email": "hubert@example.com"}
    return None  # Funkcja może zwrócić słownik lub None
```

## Funkcje anonimowe – lambda

Są to **krótkie, anonimowe funkcje**, które można definiować bez nadawania im nazwy. Służą one głównie do wykonywania prostych operacji, zwłaszcza wtedy, gdy funkcja jest potrzebna tylko w jednym, konkretnym miejscu. Zamiast stosować pełną definicję funkcji z def, używamy słowa kluczowego lambda, aby szybko stworzyć funkcję w jednej linii.

```python
# Tak wygląda standardowo zdefiniowana funkcja
def add(x, y):
    return x + y
print(add(3, 5))

# A tak lambda
add = lambda x, y: x + y
print(add(3, 5))
```

## 📝 Zadania

1. Masz daną listę słowników reprezentujących informacje o książkach w bibliotece. Każdy słownik zawiera klucze: `tytul`, `autor` oraz `rok_wydania`.

```python
ksiazki = [
    {"tytul": "Władca Pierścieni", "autor": "J.R.R. Tolkien", "rok_wydania": 1954},
    {"tytul": "Harry Potter i Kamień Filozoficzny", "autor": "J.K. Rowling", "rok_wydania": 1997},
    {"tytul": "Duma i uprzedzenie", "autor": "Jane Austen", "rok_wydania": 1813},
    {"tytul": "Rok 1984", "autor": "George Orwell", "rok_wydania": 1949},
    {"tytul": "Zbrodnia i kara", "autor": "Fiodor Dostojewski", "rok_wydania": 1866},
    {"tytul": "Mistrz i Małgorzata", "autor": "Michaił Bułhakow", "rok_wydania": 1967},
    {"tytul": "Hobbit", "autor": "J.R.R. Tolkien", "rok_wydania": 1937},
    {"tytul": "Sto lat samotności", "autor": "Gabriel García Márquez", "rok_wydania": 1967},
    {"tytul": "Imię róży", "autor": "Umberto Eco", "rok_wydania": 1980},
    {"tytul": "Solaris", "autor": "Stanisław Lem", "rok_wydania": 1961},
]
```

Twoim zadaniem jest napisanie kodu, który wykonuje następujące operacje przy użyciu funkcji lambda:

- Sortowanie książek według roku wydania: Posortuj listę książek w kolejności rosnącej według roku ich wydania.

- Filtracja książek wydanych po 2000 roku: Utwórz nową listę zawierającą tylko te książki, które zostały wydane po roku 2000.

- Transformacja listy do listy tytułów: Przekształć oryginalną listę książek w listę zawierającą tylko tytuły książek.

Wykorzystaj funkcje `sorted()`, `filter()` oraz `map()` w połączeniu z funkcjami lambda do realizacji zadania.

## Generatory

Generatory to specjalne obiekty, które generują wyniki na żądanie – jeden po drugim – zamiast tworzyć i przechowywać całą serię wyników od razu. Dzięki temu generatory są wydajniejsze w pracy z dużymi zestawami danych, ponieważ zużywają mniej pamięci.

Generatory działają na zasadzie *lazy evaluation*, co oznacza, że nie obliczają wszystkich wyników od razu, lecz tylko wtedy, gdy są potrzebne.

??? - notes "Czym generatory różnią się od iteratorów?"
    Różnią się w sposobie ich tworzenia:

    - **Iteratory** mogą być tworzone z dowolnej kolekcji iterowalnej (np. listy, krotki, słownika) przez wywołanie `iter()`, albo przez definiowanie klasy z metodą `__iter__()` i `__next__()`.

    - **Generatory** są tworzone przy użyciu funkcji z yield lub jako wyrażenia generatorów. Są to specjalne, uproszczone iteratory, które automatycznie obsługują stan i logikę __next__().

    Różnią się w sposobie przechowywania stanu:

    - **Iteratory** muszą ręcznie przechowywać stan między kolejnymi wywołaniami `__next__()`, co wymaga więcej kodu i zarządzania.

    - **Generatory** automatycznie zapamiętują stan wewnętrzny przy każdym wywołaniu `yield`, dzięki czemu są prostsze do implementacji.

    Różnią się w sposobie przechodzenia przez dane:

    - **Iteratory** zazwyczaj są jednorazowe, ale jeśli iterator działa na strukturze danych, jak lista, można go ponownie utworzyć przez `iter()`.

    - **Generatory** są jednorazowego użytku – po przeiterowaniu przez wszystkie wartości kończą się, i nie można ich wznowić od początku.

    Przykład:

    ```python
    # Niestandardowy iterator, który iteruje od 1 do podanej liczby:
    class CountUpTo:
        def __init__(self, max_value):
            self.max_value = max_value
            self.current = 1

        def __iter__(self):
            return self

        def __next__(self):
            if self.current > self.max_value:
                raise StopIteration
            else:
                self.current += 1
                return self.current - 1

    counter = CountUpTo(3)
    for number in counter:
        print(number)
    ```

    ```python
    # Analogiczny generator z yield
    def count_up_to(max_value):
        current = 1
        while current <= max_value:
            yield current
            current += 1

    for number in count_up_to(3):
        print(number)
    ```

### Funkcje generatorów

Tworzymy je tak samo jak zwykłe funkcje, ale zamiast `return` używamy `yield`, który zwraca wartość, a następnie "zawiesza" działanie funkcji. Gdy po raz kolejny wywołujemy `next()` na generatorze, funkcja kontynuuje od miejsca, w którym ostatnio się zatrzymała.

```python
def count_up_to(n):
    count = 1
    while count <= n:
        yield count  # Zwraca wartość, ale kontynuuje działanie po wywołaniu next()
        count += 1

# Tworzymy generator
counter = count_up_to(5)

print(next(counter))  # 1
print(next(counter))  # 2
# Możemy też przeiterować przez cały generator w pętli
for number in counter:
    print(number)  #  3, 4, 5
```

### Wyrażenia generatorów

To bardziej zwięzły sposób na tworzenie generatorów, podobny do list składanych. Różnią się jednak nawiasami: zamiast nawiasów kwadratowych `[]` (jak w listach składanych) używamy nawiasów okrągłych `()`.

```python
gen = (x ** 2 for x in range(5))

# Kolejne wartości możemy uzyskać wywołując next()
print(next(gen))  # 0
print(next(gen))  # 1

# Lub iterując po generatorze w pętli
for value in gen:
    print(value)  # 4, 9, 16
```

## 📝 Zadania

1. Napisz generator, który iteracyjnie zwraca nazwy dni tygodnia: od poniedziałku do niedzieli. Następnie, użyj tego generatora w pętli, aby wyświetlić każdy dzień tygodnia. Dodatkowo, zademonstruj, jak można użyć tego generatora do pobrania tylko pierwszych trzech dni tygodnia bez konieczności iterowania przez cały tydzień.

???+ tip
    To zadanie można wykonać zarówno funkcją jak i wyrażeniem.
