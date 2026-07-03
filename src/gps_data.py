from __future__ import annotations

import csv
from datetime import datetime
from math import radians, sin, cos, asin, sqrt
from pathlib import Path 

def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    radius = 6371000.0
    phi1 = radians(lat1)
    phi2 = radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
    return 2 * radius * asin(sqrt(a))

class GPSData:
    def __init__(self, csv_path: str | Path) -> None:
        self.csv_path = Path(csv_path)
        self.latitudes: list[float] = []
        self.longitudes: list[float] = []
        self.elevations: list[float] = []
        self.times: list[datetime] = []
        self.temperatures: list[float] = []
        self._load()

    def _load(self) -> None:
        with open(self.csv_path, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                self.latitudes.append(float(row["lat"]))
                self.longitudes.append(float(row["lon"]))
                self.elevations.append(float(row["ele"]))
                self.times.append(
                    datetime.fromisoformat(row["time"].replace("Z", "+00:00"))
                )
                self.temperatures.append(float(row["temperature"]))
    
    def __len__(self) -> int:
        return len(self.times)
    
    def distances(self) -> list[float]:
        result = [0.0]
        for i in range(1, len(self)):
            result.append(
                haversine(
                    self.latitudes[i - 1],
                    self.longitudes[i - 1],
                    self.latitudes[i],
                    self.longitudes[i],
                )
            )
        return result
    
    def total_distance(self) -> float:
        return sum(self.distances())