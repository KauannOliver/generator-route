# Route and Map Generator

A desktop workflow that reads route records from Excel, requests routing data, and exports interactive Folium maps with distance and travel-time details.


## Workflow

1. Select a route record from the workbook.
2. Resolve origin and destination coordinates.
3. Request directions from OpenRouteService.
4. Render and save an interactive HTML map.

## Configuration

Copy `.env.example` to `.env`, set an authorized OpenRouteService key and the local workbook path, then run the desktop app.

## Stack

Python, Flet, Pandas, OpenRouteService, Folium, and Geopy.

## Run locally

Requires Python, the dependencies in `requirements.txt`, a desktop session, an input workbook, and an OpenRouteService API key supplied locally. Run `pip install -r requirements.txt` and `python main.py`.


## Snapshot review

Setup and capabilities are based on the included code. External services and operating-system-specific integrations were not exercised during this publication review. Use synthetic data in a separate local environment.

Git-triggered Vercel deployment is disabled in the included web configurations. This update publishes source and documentation only.

## License

No new distribution license is granted for this corporate source edition. Public visibility does not grant reuse rights; obtain permission from the relevant rights holder. Existing third-party notices remain applicable.

## Verification record

See [snapshot checks and remaining limitations](docs/VERIFICATION.md).
