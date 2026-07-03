from pathlib import Path

from gps_data import GPSData


def main() -> None:
    data_path = Path(__file__).resolve().parent.parent / "data" / "final_project_input_data.csv"
    gps = GPSData(data_path)
    print(f"{len(gps)} GPS-Punkte geladen.")
    print(f"Zurückgelegte Strecke: {gps.total_distance() / 1000:.2f} km")
    print(f"Benötigte Zeit: {gps.duration() / 60:.1f} min")
    print(f"Durchschnittsgeschwindigkeit: {gps.average_speed() * 3.6:.2f} km/h")
    print(f"Maximale Geschwindigkeit: {max(gps.speeds()) * 3.6:.2f} km/h")
    print(f"Höhenmeter Anstieg: {gps.elevation_gain():.0f} m")
    print(f"Höhenmeter Abstieg: {gps.elevation_loss():.0f} m")


if __name__ == "__main__":
    main()
    