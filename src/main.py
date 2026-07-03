from pathlib import Path

from gps_data import GPSData


def main() -> None:
    data_path = Path(__file__).resolve().parent.parent / "data" / "final_project_input_data.csv"
    gps = GPSData(data_path)
    print(f"{len(gps)} GPS-Punkte geladen.")
    print(f"Zurückgelegte Strecke: {gps.total_distance() / 1000:.2f} km")


if __name__ == "__main__":
    main()