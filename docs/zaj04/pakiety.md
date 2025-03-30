## Wstęp

???- note "PRZYPOMNIENIE - czym jest moduł?"

    Moduł w Pythonie to plik z rozszerzeniem `.py`, który zawiera kod – może to być pojedyncza funkcja, klasa, a nawet cały zestaw narzędzi. Moduły pozwalają nam na przechowywanie kodu w osobnych plikach i łatwe jego importowanie oraz używanie w innych miejscach.

Kiedy używamy instrukcji `import`, Python próbuje znaleźć odpowiedni moduł w określonych lokalizacjach, które są przechowywane w zmiennej `sys.path`. Lista tych ścieżek obejmuje:

- Bieżący katalog roboczy – katalog, z którego uruchamiamy skrypt.
- Katalogi standardowe Pythona – ścieżki z bibliotekami standardowymi.
- Katalogi specyficzne dla instalacji – katalogi, które mogą zawierać dodatkowe moduły lub pakiety, np. zainstalowane za pomocą `pip`.

U siebie możemy to zobaczyć używając:

```python
import sys
print(sys.path)
```

## Wprowadzenie do pakietów

Pakiet w Pythonie to katalog (**folder**) zawierający moduły. Pakiety pozwalają na hierarchiczne organizowanie kodu, co jest szczególnie użyteczne w większych projektach. **Każdy pakiet jest katalogiem**, który powinien zawierać plik **`__init__.py`**, aby Python mógł go rozpoznać jako pakiet.

Pakiety mogą być zagnieżdżane w innych pakietach, tworząc strukturę drzewiastą. Przykładowa struktura pakietu `geoapps` mogłaby wyglądać tak:

```css
nasz-projekt/
├── geoapps/
│   ├── __init__.py
│   └── zajecia01/
│          ├── __init__.py
│          ├── dodawanie.py
│          ├── odejmowanie.py
│          └── dzielenie.py
├── docs/
└── tests/
```

## Pliki `__init__.py`

Jak widzimy w przykładowej strukturze powyżej, każdy katalog, który ma być rozpoznawany jako część pakietu, posiada ten plik. Początkowo, w starszych wersjach Pythona, ten plik był obowiązkowy; obecnie w Pythonie 3.x nadal jest używany, ale jego obecność nie jest wymagana do rozpoznania katalogu jako pakietu. Jednak `__init__.py` nadal ma ważne funkcje:

- **Inicjalizacja pakietu** – plik `__init__.py` jest uruchamiany przy pierwszym importowaniu pakietu, więc można w nim umieścić kod, który zostanie wykonany na początku.
- **Kontrolowanie importów** – możemy zdefiniować listę `__all__` w `__init__.py`, aby kontrolować, które moduły zostaną zaimportowane, gdy użyjemy `from pakiet import *`.

Przykładowy plik `__init__.py` znajdujący się w `zajęcia01`:

```python
__all__ = ["dodawanie", "odejmowanie"]
```

Dzięki temu przy `from zajecia01 import *` zostaną zaimportowane tylko moduły `dodawanie` i `odejmowanie`, podczas gdy `dzielenie` zostanie pominięte.

## Importowanie modułów

Mamy 2 główne typy importu:

- **Import bezwzględny** – polega na podaniu pełnej ścieżki do modułu lub pakietu, np.:
    - `from geoapps import *`,
    - `from geoapps.zajecia01 import dodawanie`,
    - `from geoapps.zajecia01.dodawanie import suma`,
    - `import geoapps.zajecia01.dodawanie as dod`.
- **Import względny** – używany jest wewnątrz pakietów i bazuje na kropkach wiodących:
    - Jedna kropka `.` oznacza bieżący pakiet.
    - Dwie kropki `..` oznaczają pakiet nadrzędny.

???+ danger
    **Import względny działa tylko wtedy, gdy jesteśmy w kontekście pakietu, np. podczas importowania modułów wewnątrz innego modułu tego samego pakietu.**

??? - "Przykład - importowanie bezwzględne"
    ```python
    from zajecia01 import dodawanie, odejmowanie

    print(dodawanie.dodaj(5, 3))  # Użycie funkcji dodaj z modułu dodawanie
    print(odejmowanie.odejmij(5, 3))  # Użycie funkcji odejmij z modułu odejmowanie
    ```

??? - "Przykład - importowanie względne - WEWNĄTRZ PAKIETU"
    Będąc w pliku `zajecia01/mnozenie.py`

    ```python
    from .dodawanie import dodaj  # Import z bieżącego pakietu

    def mnoz(a, b):
        wynik = 0
        for _ in range(b):
            wynik = dodaj(wynik, a)  # Użycie funkcji dodaj
        return wynik
    ```

## 📝 Zadania

1. Stwórz strukturę pakietu `geoapps` i przenieś do niego stworzone do tej pory skrypty (z wszystkich zajęć). Można użyć struktury z przykładu, czyli subpakiety odpowiadające konkretnym zajęciom np. `zajecia01`.

    !!! tip
        Nie zapomnij dodać plików `__init__.py` wewnątrz pakietów, a także opcjonalnie list `__all__` w tych plikach.

1. Wykorzystując pakiet `geoapps`, stwórz w głównym katalogu plik `run_geoapps.py`, zaimportuj do niego wybrane funkcje / klasy i wywołaj przykładowy kod z ich użyciem.
