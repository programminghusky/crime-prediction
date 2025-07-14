## Preprocessing ##

1. The code creates a GeoDataFrame (`raw_gdf`) from a regular DataFrame (`raw_df`) by:
   - Using `gpd.GeoDataFrame()` to convert the DataFrame
   - Creating point geometries with `gpd.points_from_xy()` using longitude and latitude columns
   - Setting the coordinate reference system to "EPSG:4326" (standard GPS coordinates)

2. It then performs a spatial join (`gpd.sjoin()`) between:
   - The crime data points (`raw_gdf`)
   - City boundary data (`city_limits`)
   - Using "left" join to keep all crime records
   - With "within" predicate to determine which points fall inside city boundaries

3. For locations outside city boundaries (where 'City' column is NaN), it:
   - Sets both 'Latitude' and 'Longitude' values to None
   - These will apparently be replaced later with sampled locations from the beat

4. It corrects historical data issues by:
   - Replacing offense dates older than 2008 with the report date
   - This handles potentially erroneous historical records

5. Finally, it prints summary statistics about:
   - Total number of records
   - Count of records with missing location data
   - Date range of the offense data