from pathlib import Path

from gps_data import GPSData

def main() -> None:
    data_path = Path(__file__).resolve().parent.parent / "data" / "final_project_input_data.csv"
    gps = GPSData(data_path)
    speeds = gps.speeds()
    slopes = gps.slopes()
    print(f"{len(gps)} GPS-Punkte geladen.")
    print(f"Zurückgelegte Strecke: {gps.total_distance() / 1000:.2f} km")
    print(f"Maximale Geschwindigkeit: {max(speeds) * 3.6:.2f} km/h")
    print(f"Steigung: {min(slopes) * 100:.1f} % bis {max(slopes) * 100:.1f} %")

if __name__ == "__main__":
    main()

    

