#!/bin/bash

# App name
APP_NAME="Kloudfarm Client"
DMG_NAME="KloudfarmClient"

# Remove any existing DMG
rm -f "dist/${DMG_NAME}.dmg"

# Create DMG
create-dmg \
  --volname "${APP_NAME} Installer" \
  --volicon "icon.icns" \
  --window-pos 200 120 \
  --window-size 660 400 \
  --icon-size 100 \
  --icon "${APP_NAME}.app" 180 170 \
  --hide-extension "${APP_NAME}.app" \
  --app-drop-link 480 170 \
  --no-internet-enable \
  --format UDZO \
  "dist/${DMG_NAME}.dmg" \
  "dist/${APP_NAME}.app"
