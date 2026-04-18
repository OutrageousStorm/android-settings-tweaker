# ⚙️ Android Settings Tweaker

Kotlin Android app that exposes hidden Android settings via Shizuku — no root required.

## Features
- Animation speed (window, transition)
- Pointer speed
- Screen timeout
- Hidden developer options
- Battery saver settings
- Display refresh rate (if available)

## Install
```bash
git clone https://github.com/OutrageousStorm/android-settings-tweaker
cd android-settings-tweaker
./gradlew assembleDebug
adb install app/build/outputs/apk/debug/app-debug.apk
```

## Requirements
- Android 8+
- Shizuku running
- Grant Shizuku permission in app

## Build with GitHub Actions
Pushes release APK automatically on tag.
