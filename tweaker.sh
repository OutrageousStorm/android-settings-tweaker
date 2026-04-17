#!/bin/bash
# tweaker.sh -- Quick Android settings tweaker menu
# Usage: ./tweaker.sh [profile]
# Profiles: gaming, privacy, battery, default

set -e

RED='\033[0;31m'; GREEN='\033[0;32m'; CYAN='\033[0;36m'; NC='\033[0m'

check_device() {
    if ! adb devices | grep -q "device$"; then
        echo -e "${RED}❌ No device connected${NC}"; exit 1
    fi
}

adb_put() {
    adb shell settings put $1 $2 $3 2>/dev/null && echo -e "${GREEN}✓${NC} $2 = $3" || echo -e "${RED}✗${NC} $2 failed"
}

profile_gaming() {
    echo -e "${CYAN}⚡ Gaming Profile${NC}"
    adb_put global screen_brightness_mode 0          # manual brightness
    adb_put system screen_brightness 255              # max brightness
    adb_put global low_power 0                       # disable battery saver
    adb_put secure doze_always_on 0                  # disable doze
    adb_put global adaptive_sleep 0                  # no adaptive sleep
    adb_put system stay_on_while_plugged_in 3        # stay on when plugged
    adb shell settings put system animator_duration_scale 0.5  # faster animations
}

profile_privacy() {
    echo -e "${CYAN}🔐 Privacy Profile${NC}"
    adb_put global limit_ad_tracking 1               # disable ad tracking
    adb_put secure location_mode 0                   # disable location
    adb_put global wifi_scan_always_enabled 0        # no passive WiFi scan
    adb_put global ble_scan_always_enabled 0         # no BLE scan
    adb shell pm revoke com.facebook.katana android.permission.ACCESS_FINE_LOCATION 2>/dev/null
    adb shell pm revoke com.instagram.android android.permission.ACCESS_FINE_LOCATION 2>/dev/null
    adb_put secure send_action_app_error 0           # don't send crash reports
}

profile_battery() {
    echo -e "${CYAN}🔋 Battery Saver Profile${NC}"
    adb_put global low_power 1                       # enable battery saver
    adb_put system screen_brightness 100             # dim screen
    adb_put global adaptive_sleep 1                  # adaptive sleep
    adb_put secure doze_always_on 1                  # aggressive doze
    adb_put global wifi_scan_always_enabled 0        # no WiFi scan
    adb_put global screen_off_timeout 120000         # 2 min screen timeout
}

profile_default() {
    echo -e "${CYAN}↩️  Default Profile${NC}"
    adb_put system screen_brightness 128             # medium brightness
    adb_put global low_power 0                       # disable battery saver
    adb_put secure doze_always_on 0                  # normal doze
    adb_put global screen_off_timeout 600000         # 10 min timeout
}

main() {
    check_device
    PROFILE="${1:-default}"
    
    case "$PROFILE" in
        gaming)  profile_gaming ;;
        privacy) profile_privacy ;;
        battery) profile_battery ;;
        default) profile_default ;;
        *)
            echo "Available profiles: gaming, privacy, battery, default"
            echo "Usage: $0 [profile]"
            exit 1
            ;;
    esac
    
    echo -e "\n${GREEN}✅ Profile applied${NC}"
}

main "$@"
