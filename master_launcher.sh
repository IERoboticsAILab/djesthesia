#!/bin/bash

osascript <<'EOF'
-- Open chrome without security
tell application "Terminal"
  activate
  -- Open Chrome
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/chrome.sh"
end tell

-- fft_api.py
tell application "System Events"
  tell process "Terminal"
    keystroke "t" using {command down}
  end tell
end tell
delay 1
tell application "Terminal"
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/color.sh" in selected tab of front window
end tell

-- Send EQ info to Ableton
tell application "System Events"
  tell process "Terminal"
    keystroke "t" using {command down}
  end tell
end tell
delay 1
tell application "Terminal"
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/npx.sh" in selected tab of front window
end tell

-- Ableton connection
tell application "System Events"
  tell process "Terminal"
    keystroke "t" using {command down}
  end tell
end tell
delay 1
tell application "Terminal"
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/ableton_live.sh" in selected tab of front window
end tell

-- Right hand Hydra
tell application "System Events"
  tell process "Terminal"
    keystroke "t" using {command down}
  end tell
end tell
delay 1
tell application "Terminal"
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/hydra_right_hand.sh" in selected tab of front window
end tell

-- Left hand Hydra
tell application "System Events"
  tell process "Terminal"
    keystroke "t" using {command down}
  end tell
end tell
delay 1
tell application "Terminal"
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/hydra_left_hand.sh" in selected tab of front window
end tell

delay 30.0

-- Right hand API
tell application "System Events"
  tell process "Terminal"
    keystroke "t" using {command down}
  end tell
end tell
delay 1
tell application "Terminal"
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/fastapi_right_hand.sh" in selected tab of front window
end tell

-- Left hand API
tell application "System Events"
  tell process "Terminal"
    keystroke "t" using {command down}
  end tell
end tell
delay 1
tell application "Terminal"
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/fastapi_left_hand.sh" in selected tab of front window
end tell

-- main.py
tell application "System Events"
  tell process "Terminal"
    keystroke "t" using {command down}
  end tell
end tell
delay 2
tell application "Terminal"
  do script "source /Users/onosaeka/Uni/Lab/djesthesia/launchers/main.sh" in selected tab of front window
end tell
EOF
