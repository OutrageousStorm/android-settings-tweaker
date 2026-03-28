# ⚙️ Android Settings Tweaker

Batch modify Android settings with presets — gaming, battery, privacy, UI.

## Usage

```bash
python3 tweaker.py --preset gaming    # apply gaming preset
python3 tweaker.py --preset battery   # battery optimization
python3 tweaker.py --preset privacy   # privacy hardening
python3 tweaker.py --set display_brightness 200  # single setting
python3 tweaker.py --list             # show all available presets
```

## Presets

| Preset | What it does |
|--------|-------------|
| gaming | High fps, disable animations, lock screen off timeout |
| battery | Dim display, disable background data, aggressive doze |
| privacy | Location off, ad tracking off, clipboard access blocked |
| performance | Disable visual effects, max memory allocation |
| gaming_extreme | Above + disable Wi-Fi, lock GPU freq, 90fps min |
