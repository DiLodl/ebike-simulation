# E-Bike Simulation

Python-Anwendung zur Auslegung und Simulation eines E-Bikes auf Basis realer GPS-Daten.
Aus den GPS-Daten werden Geschwindigkeit, Beschleunigung, Steigung, Leistung, Motordrehmoment,
Motorstrom sowie der Ladezustand zweier Akkutypen (LiPo und NMC) berechnet und grafisch dargestellt.

## Installation

```bash
git clone https://github.com/DiLodl/ebike-simulation.git
cd ebike-simulation
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

Unter Windows in Git Bash wird die virtuelle Umgebung mit `source .venv/Scripts/activate` aktiviert.

## Ausführung

```bash
python src/main.py
```

## Projektstruktur

- `src/main.py` – Einstiegspunkt der Anwendung
- `src/gps_data.py` – Einlesen und Auswertung der GPS-Daten
- `src/vehicle.py` – Fahrradmodell, Kräfte, Leistung, Drehmoment, Motorstrom
- `src/battery.py` – Akku-Klassen (LiPo, NMC)
- `src/simulation.py` – Ablauf der Simulation
- `src/plots.py` – grafische Darstellung der Ergebnisse
- `data/` – GPS-Eingangsdaten
- `results/` – erzeugte Diagramme
- `tests/` – Unit-Tests
