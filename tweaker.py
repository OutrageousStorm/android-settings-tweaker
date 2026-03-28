#!/usr/bin/env python3
"""tweaker.py -- Batch Android settings modifier with presets"""
import subprocess, argparse, sys

def adb(cmd):
    r = subprocess.run(f"adb shell {cmd}", shell=True, capture_output=True, text=True)
    return r.returncode == 0

PRESETS = {
    "gaming": {
        "desc": "Gaming optimized — high fps, no animations, screen always on",
        "global": {
            "animator_duration_scale": 0,
            "transition_animation_scale": 0,
            "window_animation_scale": 0,
            "screen_off_timeout": 3600000,
            "haptic_feedback_enabled": 0,
        },
        "system": {
            "screen_brightness": 240,
            "screen_brightness_mode": 0,
        }
    },
    "battery": {
        "desc": "Maximum battery life — dim, aggressive doze, restricted background",
        "global": {
            "screen_off_timeout": 120000,
            "wifi_scan_always_enabled": 0,
            "ble_scan_always_enabled": 0,
        },
        "system": {
            "screen_brightness": 80,
            "screen_brightness_mode": 0,
        },
        "secure": {
            "location_mode": 0,
        }
    },
    "privacy": {
        "desc": "Privacy hardened — tracking off, location off, permissions tightened",
        "global": {
            "limit_ad_tracking": 1,
            "location_mode": 0,
            "wifi_scan_always_enabled": 0,
        },
        "secure": {
            "location_mode": 0,
        }
    },
    "performance": {
        "desc": "High performance — disable visual effects, maximize throughput",
        "global": {
            "animator_duration_scale": 0.5,
            "transition_animation_scale": 0.5,
            "window_animation_scale": 0.5,
            "debug_app": "",
        }
    },
}

def apply_preset(name):
    if name not in PRESETS:
        print(f"Unknown preset: {name}")
        list_presets()
        return
    p = PRESETS[name]
    print(f"\n⚙️  Applying preset: {name}")
    print(f"    {p['desc']}\n")
    
    count = 0
    for ns in ['global', 'system', 'secure']:
        settings = p.get(ns, {})
        for key, val in settings.items():
            ok = adb(f"settings put {ns} {key} {val}")
            icon = "✓" if ok else "✗"
            print(f"  {icon} {ns}/{key} = {val}")
            if ok: count += 1
    print(f"\n✅ Applied {count} settings")

def set_single(key, val):
    parts = key.split('/')
    if len(parts) == 2:
        ns, k = parts
        ok = adb(f"settings put {ns} {k} {val}")
        print(f"{'✓' if ok else '✗'} {ns}/{k} = {val}")
    else:
        print("Format: namespace/key (e.g. global/screen_brightness)")

def list_presets():
    print("\nAvailable presets:\n")
    for name, p in PRESETS.items():
        print(f"  {name:<15} {p['desc']}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--preset", help="Apply a preset")
    parser.add_argument("--set", help="Set single value: namespace/key")
    parser.add_argument("--value", help="Value for --set")
    parser.add_argument("--list", action="store_true", help="List presets")
    args = parser.parse_args()

    if args.list:
        list_presets()
    elif args.preset:
        apply_preset(args.preset)
    elif args.set and args.value:
        set_single(args.set, args.value)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
