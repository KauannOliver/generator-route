# **Protheus Route Planner**

This project was developed to optimize logistics planning and route visualization using data from Excel files. By integrating OpenRouteService and Folium, it provides a seamless way to generate maps and analyze routes directly from a user-friendly interface built with the Flet framework.

---

## **KEY FEATURES**

### 1. **Excel Data Integration**
   - Reads route data directly from Excel files.
   - Simplifies the process of selecting routes using a dropdown linked to Excel records.

### 2. **Dynamic Map Generation**
   - Uses OpenRouteService API to generate routes with precise distances and travel times.
   - Creates dynamic HTML maps using Folium, displaying origin, destination, and the complete route.

### 3. **Geolocation with Nominatim**
   - Retrieves geographical coordinates for cities and states using the Nominatim geocoding service.
   - Ensures accurate mapping of origin and destination points.

### 4. **Interactive Route Visualization**
   - Displays route details such as origin, destination, distance (in kilometers), and estimated travel time.
   - Provides an embedded HTML-based information panel for detailed route data.

### 5. **HTML Export**
   - Saves generated routes as standalone HTML files.
   - Enables easy sharing and visualization of routes in any web browser.

### 6. **Real-Time User Feedback**
   - Includes error handling for invalid or incomplete data.
   - Provides notifications for successful or unsuccessful route generation.

---

## **TECHNOLOGIES USED**

### 1. **Flet**
   - Framework used to build an intuitive and responsive user interface.

### 2. **Python**
   - Core language powering the application logic and integrations.

### 3. **Pandas**
   - Handles reading and processing of Excel data efficiently.

### 4. **OpenRouteService**
   - Generates detailed routes, including distances and travel times.

### 5. **Folium**
   - Creates interactive maps with markers and route visualization.

### 6. **Geopy**
   - Provides geolocation services to fetch coordinates of cities and states.

### 7. **Webbrowser**
   - Opens the generated HTML files for immediate route visualization.

---

## **CONCLUSION**

The **Protheus Route Planner** streamlines logistics and route planning by integrating powerful APIs and tools into a cohesive system. It is ideal for businesses aiming to enhance operational efficiency through automated map generation, data visualization, and real-time route insights. With its accessible and interactive design, it offers a robust solution for route management and planning.
