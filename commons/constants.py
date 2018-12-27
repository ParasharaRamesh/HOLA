HAVER_SINE_FORMULA = (
    "111.045 * DEGREES(ACOS(COS(RADIANS({latitude})) * COS(RADIANS(ST_Y(\"geoLocation\"))) * COS(RADIANS({longitude}) "
    "- RADIANS(ST_X(\"geoLocation\"))) + SIN(RADIANS({latitude})) * SIN(RADIANS(ST_Y(\"geoLocation\")))))"
)
SEARCH_RADIUS = 2
