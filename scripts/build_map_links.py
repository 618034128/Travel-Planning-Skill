#!/usr/bin/env python3
"""Build shareable route URLs (Google Maps / Amap / Baidu) from an ordered list of stops.

Use this in Phase 2 of the travel-planning-skill skill when no interactive
maps/places tool is available in the agent. It emits a directions URL that opens
the full route, with every stop as a waypoint in visiting order.

Stops may be plain names ("Liji Islamic Restaurant, Qinhuai, Nanjing") or
coordinates ("32.0293,118.7797"). Coordinate order on input is always lat,lng
(Google convention); the script flips to lng,lat where the provider needs it.

Examples
--------
# International trip, Google Maps, walking
python build_map_links.py --provider google --mode walking \
    --stops "Fushimi Inari, Kyoto" "Nishiki Market, Kyoto" "Kiyomizu-dera, Kyoto"

# Mainland China, let the script pick Amap+Baidu, transit
python build_map_links.py --provider auto --city Nanjing --mode transit \
    --stops "新街口" "老门东" "夫子庙"

# With coordinates (lat,lng)
python build_map_links.py --provider google --mode driving \
    --stops "32.0293,118.7797" "32.0114,118.7871"
"""
import argparse
import sys
from urllib.parse import quote

GOOGLE_MODES = {"walking", "transit", "driving", "bicycling"}
AMAP_MODES = {"walking": "walk", "transit": "bus", "driving": "car", "bicycling": "ride"}
BAIDU_MODES = {"walking": "walking", "transit": "transit", "driving": "driving", "bicycling": "riding"}


def is_coord(s):
    parts = s.split(",")
    if len(parts) != 2:
        return False
    try:
        float(parts[0]); float(parts[1])
        return True
    except ValueError:
        return False


def flip_latlng(s):
    """'lat,lng' -> 'lng,lat' for providers that want lng first."""
    lat, lng = s.split(",")
    return f"{lng.strip()},{lat.strip()}"


def google_url(stops, mode):
    origin, dest = stops[0], stops[-1]
    waypoints = stops[1:-1]
    q = [f"origin={quote(origin)}", f"destination={quote(dest)}", f"travelmode={mode}"]
    if waypoints:
        q.append("waypoints=" + quote("|".join(waypoints)))
    return "https://www.google.com/maps/dir/?api=1&" + "&".join(q)


def amap_url(stops, mode, city):
    amode = AMAP_MODES.get(mode, "car")
    def seg(s):
        if is_coord(s):
            return f"{flip_latlng(s)},stop"
        return f"name:{quote(s)}"
    frm, to = seg(stops[0]), seg(stops[-1])
    url = f"https://uri.amap.com/navigation?from={frm}&to={to}&mode={amode}&policy=1&src=itinerary&coordinate=gaode"
    # Amap web URI does not take intermediate waypoints reliably; note them for the user.
    return url


def baidu_url(stops, mode, city):
    bmode = BAIDU_MODES.get(mode, "walking")
    origin, dest = stops[0], stops[-1]
    region = city or ""
    return (
        "https://api.map.baidu.com/direction?"
        f"origin={quote(origin)}&destination={quote(dest)}"
        f"&mode={bmode}&region={quote(region)}&output=html&src=itinerary"
    )


def main():
    p = argparse.ArgumentParser(description="Build route URLs for Google Maps / Amap / Baidu.")
    p.add_argument("--stops", nargs="+", required=True, help="Ordered stops: names or 'lat,lng'.")
    p.add_argument("--provider", default="auto", choices=["auto", "google", "amap", "baidu"],
                   help="auto = Google for international, Amap+Baidu when --city is in mainland China.")
    p.add_argument("--mode", default="walking", choices=sorted(GOOGLE_MODES),
                   help="Travel mode.")
    p.add_argument("--city", default="", help="City name; required for Baidu and for China auto-detection.")
    p.add_argument("--china", action="store_true", help="Force mainland-China providers (Amap + Baidu).")
    args = p.parse_args()

    if len(args.stops) < 2:
        print("Need at least 2 stops (an origin and a destination).", file=sys.stderr)
        sys.exit(1)

    china = args.china
    provider = args.provider

    print("# Route (in visiting order):")
    for i, s in enumerate(args.stops, 1):
        print(f"#  {i}. {s}")
    print()

    waypoints = args.stops[1:-1]

    if provider == "google" or (provider == "auto" and not china):
        print("Google Maps:")
        print(google_url(args.stops, args.mode))
    if provider in ("amap", "baidu") or china or (provider == "auto" and china):
        print("Amap (高德):")
        print(amap_url(args.stops, args.mode, args.city))
        print("Baidu (百度):")
        print(baidu_url(args.stops, args.mode, args.city))
        if waypoints:
            print("\n# Note: Amap/Baidu web links route origin→destination only.")
            print("# Intermediate stops to add manually in the app:")
            for w in waypoints:
                print(f"#   - {w}")


if __name__ == "__main__":
    main()
