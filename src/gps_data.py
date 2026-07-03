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

    def time_deltas(self) -> list[float]:
        result = [0.0]
        for i in range(1, len(self)):
            result.append((self.times[i] - self.times[i - 1]).total_seconds())
        return result

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

    def speeds(self) -> list[float]:
        distances = self.distances()
        deltas = self.time_deltas()
        result = [0.0]
        for i in range(1, len(self)):
            if deltas[i] <= 0:
                result.append(result[-1])
            else:
                result.append(distances[i] / deltas[i])
        return result

    def accelerations(self) -> list[float]:
        speeds = self.speeds()
        deltas = self.time_deltas()
        result = [0.0]
        for i in range(1, len(self)):
            if deltas[i] <= 0:
                result.append(0.0)
            else:
                result.append((speeds[i] - speeds[i - 1]) / deltas[i])
        return result

    def slopes(self) -> list[float]:
        distances = self.distances()
        result = [0.0]
        for i in range(1, len(self)):
            if distances[i] <= 0:
                result.append(0.0)
            else:
                result.append(
                    (self.elevations[i] - self.elevations[i - 1]) / distances[i]
                )
        return result

    def duration(self) -> float:
        return (self.times[-1] - self.times[0]).total_seconds()

    def average_speed(self) -> float:
        return self.total_distance() / self.duration()

    def elevation_gain(self) -> float:
        gain = 0.0
        for i in range(1, len(self)):
            diff = self.elevations[i] - self.elevations[i - 1]
            if diff > 0:
                gain += diff
        return gain

    def elevation_loss(self) -> float:
        loss = 0.0
        for i in range(1, len(self)):
            diff = self.elevations[i] - self.elevations[i - 1]
            if diff < 0:
                loss += -diff
        return loss
    
    