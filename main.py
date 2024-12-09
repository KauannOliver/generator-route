import flet as ft
import pandas as pd
import openrouteservice
import webbrowser
import folium
from geopy.geocoders import Nominatim

### cfg openrouteservice e geolocator ###
client = openrouteservice.Client(key='SUA_API_KEY')
geolocator = Nominatim(user_agent="rotas_protheus")

### caminho do excel ###
caminho_excel = r"S:\Custos\Kauan\Rotas.xlsx"

### carregar dados excel ###
def carregar_dados_excel(caminho):
    df = pd.read_excel(caminho)
    return df

### gerar html do mapa ###
def gerar_mapa_html(municipio_origem, uf_origem, municipio_destino, uf_destino, codigo_rota):
    ### buscar coords origem e destino ###
    coords_origem = geolocator.geocode(f"{municipio_origem}, {uf_origem}, Brasil")
    coords_destino = geolocator.geocode(f"{municipio_destino}, {uf_destino}, Brasil")

    if not coords_origem or not coords_destino:
        return None, "Erro ao obter coordenadas para os municípios fornecidos."

    ### converter coords ###
    coords_origem_reversed = (coords_origem.longitude, coords_origem.latitude)
    coords_destino_reversed = (coords_destino.longitude, coords_destino.latitude)

    ### solicitar rota ###
    rota = client.directions(
        coordinates=[coords_origem_reversed, coords_destino_reversed],
        profile='driving-car',
        format='geojson'
    )

    ### extrair geom, dist e duração ###
    geometry = rota['features'][0]['geometry']['coordinates']
    distance_km = rota['features'][0]['properties']['segments'][0]['distance'] / 1000
    duration_min = rota['features'][0]['properties']['segments'][0]['duration'] / 60

    ### criar mapa ###
    mapa = folium.Map(location=[coords_origem.latitude, coords_origem.longitude], zoom_start=6)
    folium.Marker([coords_origem.latitude, coords_origem.longitude], popup="Origem").add_to(mapa)
    folium.Marker([coords_destino.latitude, coords_destino.longitude], popup="Destino").add_to(mapa)
    folium.PolyLine(locations=[[lat, lon] for lon, lat in geometry], color="blue", weight=5).add_to(mapa)

    ### render html ###
    mapa_html = mapa.get_root().render()

    ### painel info ###
    painel_informacoes = f"""
    <div style="width: 300px; height: 100%; border-radius: 0; background-color: #fff; padding: 20px; box-shadow: -4px 0 10px rgba(0, 0, 0, 0.1); display: flex; flex-direction: column; gap: 15px; position: fixed; top: 0; right: 0; z-index: 9999;">
        <h3 style="text-align: center; font-size: 1.2em; color: #333;">Informações - {codigo_rota}</h3>
        <div style="display: flex; flex-direction: column; gap: 5px;">
            <label style="font-weight: bold; color: #555;">Município Origem:</label>
            <span style="color: #777;">{municipio_origem}</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 5px;">
            <label style="font-weight: bold; color: #555;">UF Origem:</label>
            <span style="color: #777;">{uf_origem}</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 5px;">
            <label style="font-weight: bold; color: #555;">Município Destino:</label>
            <span style="color: #777;">{municipio_destino}</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 5px;">
            <label style="font-weight: bold; color: #555;">UF Destino:</label>
            <span style="color: #777;">{uf_destino}</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 5px;">
            <label style="font-weight: bold; color: #555;">Distância em Km:</label>
            <span style="color: #777;">{distance_km:.2f} km</span>
        </div>
        <div style="display: flex; flex-direction: column; gap: 5px;">
            <label style="font-weight: bold; color: #555;">Tempo Gasto:</label>
            <span style="color: #777;">{duration_min:.2f} minutos</span>
        </div>
        <center><img src="logoen1.png" alt="Mapa da rota" style="width: 80%; display: block; margin-top: 160px;"></center>
    </div>
    """

    ### combinar mapa e painel ###
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{
                margin: 0;
                overflow: hidden;
            }}
            #map {{
                position: absolute;
                top: 0;
                bottom: 0;
                left: 0;
                right: 0;
            }}
        </style>
    </head>
    <body>
        <div id="map">{mapa_html}</div>
        {painel_informacoes}
    </body>
    </html>
    """
    return html, None

### função principal ###
def main(page: ft.Page):
    page.title = "Rotas do Protheus"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_width = 600
    page.window_height = 500

    ### carregar excel e definir opcoes dropdown ###
    df = carregar_dados_excel(caminho_excel)
    codigos_rota = df.iloc[:, 0].tolist()

    ### criar campos e botao ###
    dropdown = ft.Dropdown(label="Código da Rota", width=505, options=[ft.dropdown.Option(codigo) for codigo in codigos_rota], on_change=lambda e: carregar_dados_rota(e.control.value))
    municipio_origem = ft.TextField(label="Município Origem", width=360)
    uf_origem = ft.TextField(label="UF Origem", width=140)
    municipio_destino = ft.TextField(label="Município Destino", width=360)
    uf_destino = ft.TextField(label="UF Destino", width=140)
    button = ft.FilledButton("Gerar Rota", width=505, on_click=lambda _: visualizar_rota())

    ### carregar dados ao escolher codigo ###
    def carregar_dados_rota(codigo):
        if codigo:
            linha = df[df.iloc[:, 0] == codigo].iloc[0]
            municipio_origem.value = linha[1]
            uf_origem.value = linha[2]
            municipio_destino.value = linha[3]
            uf_destino.value = linha[4]
            page.update()

    ### gerar e abrir rota ###
    def visualizar_rota():
        codigo = dropdown.value
        if not codigo:
            page.snack_bar = ft.SnackBar(ft.Text("Selecione um código de rota!"))
            page.snack_bar.open = True
            return

        html, erro = gerar_mapa_html(
            municipio_origem.value,
            uf_origem.value,
            municipio_destino.value,
            uf_destino.value,
            codigo
        )
        if erro:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {erro}"))
            page.snack_bar.open = True
            return

        ### salvar html e abrir no navegador ###
        with open(f"rota_{codigo}.html", "w", encoding="utf-8") as f:
            f.write(html)

        page.snack_bar = ft.SnackBar(ft.Text("Rota gerada com sucesso!"))
        webbrowser.open(f"rota_{codigo}.html")
        page.snack_bar.open = True

    ### layout ###
    page.add(
        ft.Column(
            [
                ft.Text("Rotas do Protheus", size=20, weight=ft.FontWeight.BOLD),
                dropdown,
                ft.Row([municipio_origem, uf_origem], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([municipio_destino, uf_destino], alignment=ft.MainAxisAlignment.CENTER),
                button
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main, view=ft.WEB_BROWSER)
