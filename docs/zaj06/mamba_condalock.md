# Tworzenie środowiska z użyciem mamba i conda-lock

## Wstęp

W tym przewodniku przejdziemy krok po kroku po tym jak stworzyć i zarządzać środowiskiem wirtualnym przy użyciu `mamba` i `conda-lock`. Będziemy bazować na plikach `env.yml` oraz `env-dev.yml`, które razem zawierają wszystkie niezbędne zależności dla środowiska deweloperskiego.


## Przygotowanie środowiska wirtualnego

!!! danger "Praca w Dockerze"
    
    Ponieważ pracujemy w oparciu o moje repozytorium, proszę nie wykonywać kroków oznaczonych ❌. Te kroki zostały już niejako "dostarczone" w ramach moich zmian.

### ❌ Krok 1: Przygotowanie plików definicji

!!! info "Co to jest `env-dev.yml`?"

    Pliki `env.yml` oraz `env-dev.yml` to konfiguracja środowiska, która określa:

    - Jakie pakiety Python są potrzebne,
    - Z jakich źródeł (channels) pobierać pakiety,
    - Jakie wersje pakietów są wymagane.

    W przypadku pliku z `dev`, mamy tam dodatkowe narzędzia deweloperskie, potrzebne tylko przy rozwoju naszego projektu.

Stwórz plik `env.yml` z następującą zawartością w głównym katalogu projektu:

```yaml
name: geoapps-env
platforms:
  - linux-64
  - win-64
  - osx-64
  - osx-arm64
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.11
  - pip
  - numpy
  - geopandas >= 1.0
  - matplotlib
  - scikit-learn
```

Stwórz plik `env-dev.yml` z następującą zawartością w głównym katalogu projektu:

```yaml
name: geoapps-env
category: dev
platforms:
  - linux-64
  - win-64
  - osx-64
  - osx-arm64
channels:
  - conda-forge
  - defaults
dependencies:
  - jupyter
  - ipykernel
  - pytest
```

!!! tip "Instalowanie poprzez `pip`"
    
    Istnieje także możliwość dodania sekcji instalowanej przez `pip` w ramach `dependencies`:

    ```yaml
    dependencies:
        - python=3.11
        - pip
        - numpy
        - pip:
          - coverage
          - pre-commit < 4.0
    ```

### ❌ Krok 2: Generowanie plików blokady

Najpierw należy się upewnić, że `conda-lock` jest zainstalowane w środowisku bazowym:

```bash
mamba install -c conda-forge conda-lock
```

!!! info "Co to jest `conda-lock`?"

    `conda-lock` to narzędzie, które:
    
    - Zapewnia reprodukowalność środowiska,
    - Generuje dokładne wersje wszystkich zależności,
    - Gwarantuje, że środowisko będzie identyczne na różnych maszynach.

Używając `conda-lock`, wygeneruj plik blokady dla środowiska deweloperskiego:

```bash
conda-lock --mamba -f env.yml -f env-dev.yml --lockfile conda-lock-dev.yml
```

A także dla środowiska produkcyjnego:

```bash
conda-lock --mamba -f env.yml --lockfile conda-lock.yml
```

### ✅ Krok 3: Stworzenie środowiska wirtualnego

Stwórz środowisko wirtualne oparte o plik blokady:

```bash
conda-lock install --mamba -n geoapps-env conda-lock-dev.yml
```

Aktywuj stworzone środowisko wirtualne:

```bash
mamba activate geoapps-env
```

### ✅ Krok 4: Instalacja pakietu lokalnego

Podobnie jak wcześniej, zainstaluj pakiet lokalny w trybie edytowalnym:

```bash
pip install -e .
```

### ✅ Krok 5: Weryfikacja środowiska

Zweryfikuj czy zainstalowane zostały wymagane biblioteki:

```bash
# Lista zainstalowanych pakietów
mamba list

# Sprawdzenie wersji Pythona
python --version
```

## Aktualizacja środowiska wirtualnego

!!! info "Kiedy aktualizować środowisko?"
    
    Aktualizacja jest potrzebna, gdy:

    - Potrzebne są nowe biblioteki,
    - Występują problemy z bezpieczeństwem,
    - Pojawiają się nowe funkcje w bibliotekach,
    - Konieczne są poprawki błędów.

1. Zmodyfikuj ręcznie odpowiednio plik `env.yml` lub `env-dev.yml`,
2. Ponownie wygeneruj odpowiedni plik blokady,
3. Aktywuj środowisko bazowe, usuń środowisko wirtualne i stwórz je ponownie na podstawie nowych plików blokady.

!!! warning "Nawet w przypadku pracy w kontenerze, musimy samodzielnie modyfikować pliki z definicją oraz regenerować pliki blokady!"

## Dobre praktyki

1. **Zawsze używaj plików blokady** - gwarantują one reprodukowalność środowiska,
2. **Regularnie aktualizuj zależności** - ale rób to świadomie i testuj zmiany,
3. **Używaj mamba zamiast conda** - szybsze rozwiązywanie zależności,
4. **Dokumentuj zmiany** - szczególnie przy aktualizacji wersji pakietów,
5. **Testuj środowisko** - po każdej większej zmianie w zależnościach.

## Przydatne linki

- [Dokumentacja mamba](https://mamba.readthedocs.io/)
- [Dokumentacja conda-lock](https://conda.github.io/conda-lock/)
- [Miniforge](https://github.com/conda-forge/miniforge)

## 📝 Zadania

1. Dodaj nową zależność `geopandas >= 1.0` do pliku `env.yml`.
2. Wygeneruj ponownie pliki blokady dla środowiska deweloperskiego i produkcyjnego.
3. Usuń poprzednio stworzone środowisko wirtualne i stwórz je wykorzystując nowe pliki blokady, zainstaluj pakiet lokalny w trybie edytowalnym.