# Route Planning and Map Export Tool

A desktop workflow that reads route records from Excel, requests routing data, and exports interactive Folium maps with distance and travel-time details.

> Private repository: route identifiers and generated maps may reveal operational locations. Remove real route data and use authorized API credentials only.

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
