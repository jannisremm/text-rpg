# Test RPG

Ein experimentelles, terminalbasiertes Rollenspiel (RPG), das nicht nur Spielmechaniken entwickelt, sondern gleichzeitig moderne Software-Entwicklungspraktiken vermittelt.

Dieses Projekt dient zwei Zielen:

1. Ein funktionierendes Minimal-RPG (MVP) entwickeln
2. Saubere, professionelle Entwicklungsprozesse kennenlernen

Das Projekt ist bewusst einfach im Gameplay – aber strukturiert im Engineering.

## Projektziel

Das Ziel des Projekts ist es, ein kleines textbasiertes RPG zu entwickeln, das im Terminal läuft.

Das sogenannte MVP (Minimum Viable Product) soll:

- Einen Spieler erstellen
- Gegner erzeugen
- Kämpfe simulieren
- Eine einfache Spielschleife enthalten

Später können Features wie Items, Level-Systeme, Map-Generierung oder Status-Effekte hinzukommen.

Genauso wichtig wie das Spiel selbst ist jedoch:

- Sauberer Code
- Strukturierte Commits
- Automatische Qualitätsprüfung
- Nachvollziehbare Versionsverwaltung
- Dieses Projekt ist also gleichzeitig Spiel und Lernumgebung.

## Projektstruktur

Das Projekt verwendet eine moderne Python-Struktur mit src/-Ordner:

```bash
terminal-rpg/
│
├── pyproject.toml
├── uv.lock
├── README.md
│
├── src/
│   └── rpg/
│       ├── main.py
│       ├── player.py
│       ├── enemy.py
│       ├── combat.py
│       ├── world.py
│       ├── items.py
│
└── tests/
```

Warum ```src/?```

Diese Struktur verhindert versehentliche Importprobleme und ist Best Practice für installierbare Python-Projekte.

## Installation

Dieses Projekt verwendet uv als Dependency-Manager.

uv ersetzt pip und venv durch ein modernes, schnelleres Tool.

<https://docs.astral.sh/uv/>

### Voraussetzungen

- Python 3.12
- uv installiert

### Projekt einrichten

Im Projektordner ausführen:

```uv sync```

Das erstellt eine virtuelle Umgebung und installiert alle Abhängigkeiten.

- Installiert exakt die Versionen aus uv.lock
- Verhindert „works on my machine“-Probleme
- Macht Builds reproduzierbar

## Projekt starten

```uv run python -m rpg.main```

Warum uv run?

Damit wird garantiert, dass der Code innerhalb der Projektumgebung läuft.

Wenn das nicht funktioniert, muss zuerst das packet lokal installiert werden:

```uv pip install -e .```

danach wird ```rpg``` importierbar.

## Entwicklungsworkflow

Dieses Projekt folgt modernen Team-Standards.

Das bedeutet:

- Kein direktes Pushen auf main
- Jede Änderung läuft über Pull Requests
- Automatische Prüfungen verhindern fehlerhaften Code

### Code-Qualität mit Ruff

Wir verwenden ruff als Linter.

Ein Linter überprüft Code auf:

- Syntaxfehler
- Unbenutzte Variablen
- Formatierungsprobleme
- Import-Fehler

Lokal prüfen:

uv run ruff check .

Installation:
<https://docs.astral.sh/ruff/installation/>

#### Warum ruff?

- Sehr schnell
- Ersetzt mehrere Tools (flake8, isort, etc.)
- Hält Code konsistent

Wichtig:
Ruff läuft automatisch in GitHub Actions.
Wenn ein Pull Request Lint-Fehler enthält, kann er nicht gemerged werden.

### Commit-Regeln (Conventional Commits)

Wir verwenden das Format Conventional Commits.

Übersicht:
<https://www.conventionalcommits.org/en/v1.0.0/>

Für VS-Code:
<https://marketplace.visualstudio.com/items?itemName=vivaxy.vscode-conventional-commits>

Warum?

- Automatische Versionsnummern möglich
- Automatische Changelog-Generierung
- Klar erkennbare Änderungen

Warum ist das wichtig?

Ein Commit sollte erklären:

- Was wurde geändert?
- Warum wurde es geändert?
- Strukturierte Commits machen Projektgeschichte lesbar.

GitHub überprüft automatisch, ob Commits diesem Format entsprechen.

## Branch Protection

Der main-Branch ist geschützt.

Das bedeutet:

- Kein direktes Pushen möglich
- Pull Request erforderlich
  - Sollten nur von dev-Branch kommen
- Automatische Checks müssen erfolgreich sein
- Review kann erforderlich sein

Warum?

Das schützt die Stabilität des Projekts.

```main``` sollte immer lauffähig sein.

## Pull Request Workflow

1. Neues Feature-Branch erstellen von dev-Branch
2. Änderungen machen
3. Saubere Commits schreiben
4. Pull Request öffnen für dev-Branch
5. Automatische Checks bestehen
6. Review
7. Merge
8. Pull Request öffnen für main-Branch
9. Review
10. Merge & Versionsnummer aktualisieren

## Versionierung

Die Version steht in pyproject.toml.

Format:

MAJOR.MINOR.PATCH

Beispiel: 0.1.0

Regeln:

- PATCH → Bugfix
- MINOR → Neues Feature
- MAJOR → Breaking Change

Mit strukturierten Commits kann die Version später automatisch erhöht werden.

Warum Versionierung wichtig ist:

- Releases nachvollziehbar
- Änderungen dokumentiert
- Abhängigkeiten kontrollierbar

## Tests (zukünftig)

Später werden Unit Tests eingeführt.

Tests prüfen:

- Kampflogik
- Schadensberechnung
- Item-Effekte

Warum Tests?

- Verhindern Regressionen
- Dokumentieren erwartetes Verhalten
- Erlauben Refactoring ohne Angst

## Langfristige Vision

Dieses Projekt soll zeigen:

- Wie man ein Python-Projekt strukturiert
- Wie man professionelle Workflows einführt
- Wie man Codequalität automatisiert
- Wie man gemeinsam entwickelt

Das Spiel selbst ist nur der Rahmen.

Die eigentliche Lernkurve liegt im Engineering.

## Mitmachen

1. Branch erstellen
2. Feature implementieren
3. Saubere Commits schreiben
4. Pull Request öffnen
5. Feedback integrieren

Softwareentwicklung ist Teamarbeit.

Saubere Struktur und Automatisierung helfen dabei, dass Zusammenarbeit nicht im Chaos endet.
