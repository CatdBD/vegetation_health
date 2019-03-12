"""
The lookup values for the GLOBMAP landcover classes
 (defined in ee_extract_landcover.js)
"""
globmap_lookup = {
11 : "Post-flooding or irrigated croplands",
14 : "Rainfed croplands",
20 : "Mosaic cropland (50-70%) / vegetation (grassland, shrubland, forest) (20-50%)",
30 : "Mosaic vegetation (grassland, shrubland, forest) (50-70%) / cropland (20-50%)",
40 : "Closed to open (>15%) broadleaved evergreen and/or semi-deciduous forest (>5m)",
50 : "Closed (>40%) broadleaved deciduous forest (>5m)",
60 : "Open (15-40%) broadleaved deciduous forest (>5m)",
70 : "Closed (>40%) needleleaved evergreen forest (>5m)",
90 : "Open (15-40%) needleleaved deciduous or evergreen forest (>5m)",
100 : "Closed to open (>15%) mixed broadleaved and needleleaved forest (>5m)",
110 : "Mosaic forest-shrubland (50-70%) / grassland (20-50%)",
120 : "Mosaic grassland (50-70%) / forest-shrubland (20-50%)",
130 : "Closed to open (>15%) shrubland (<5m)",
140 : "Closed to open (>15%) grassland",
150 : "Sparse (>15%) vegetation (woody vegetation, shrubs, grassland)",
160 : "Closed (>40%) broadleaved forest regularly flooded - Fresh water",
170 : "Closed (>40%) broadleaved semi-deciduous and/or evergreen forest regularly flooded - saline water",
180 : "Closed to open (>15%) vegetation (grassland, shrubland, woody vegetation) on regularly flooded or waterlogged soil",
190 : "Artificial surfaces and associated areas (urban areas >50%) GLOBCOVER 2009",
200 : "Bare areas",
210 : "Water bodies",
220 : "Permanent snow and ice",
230 : "Unclassified",
}

globmap_lookup_tommy = {
11 : "irrigated croplands",
14 : "Rainfed croplands",
20 : "cropland/vegetation",
30 : "vegetation/cropland",
40 : "broad-leaved evergreen/semi-deciduous forest",
50 : "broad-leaved deciduous forest",
60 : "broad-leaved deciduous forest",
70 : "needle-leaved evergreen forest",
90 : "needle-leaved deciduous / evergreen forest",
100 : "broad-leaved / needleleaved forest",
110 : "forest-shrubland / grassland",
120 : "Mosaic grassland / forest-shrubland",
130 : "shrubland",
140 : "grassland",
150 : "Sparse vegetation",
160 : "forest regularly flooded - Fresh water",
170 : "forest regularly flooded - saline water",
180 : "vegetation on flooded soil",
190 : "Artificial",
200 : "Bare areas",
210 : "Water bodies",
220 : "Permanent snow and ice",
230 : "Unclassified",
}


globmap_lookup2 = {
# np.nan : "NA",
11 : "cropland",
14 : "cropland",
20 : "cropland",
30 : "cropland",
40 : "forest",
50 : "forest",
60 : "forest",
70 : "forest",
90 : "forest",
100 : "forest",
110 : "shrubland/grassland",
120 : "shrubland/grassland",
130 : "shrubland",
140 : "grassland",
150 : "Sparse vegetation",
160 : "flooded",
170 : "flooded",
180 : "flooded",
190 : "Artificial",
200 : "Bare areas",
210 : "Water bodies",
220 : "Permanent snow and ice",
230 : "Unclassified",
}

remap_to_int_dict = {
# "NA": 1,
"cropland": 2,
"forest": 3,
"shrubland/grassland": 4,
"shrubland": 5,
"grassland": 6,
"Sparse vegetation": 7,
"flooded": 8,
"Artificial": 9,
"Bare areas": 10,
"Water bodies": 11,
"Permanent snow and ice": 12,
"Unclassified": 13,
}

globmap_lookup3 = dict(zip(remap_to_int_dict.values(), remap_to_int_dict.keys()))
