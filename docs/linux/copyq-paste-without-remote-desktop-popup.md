# CopyQ: paste without the "Remote Desktop" pop-up

Fixed on 14 November 2026, on Ubuntu 26.04 (GNOME, Wayland) with CopyQ 13.0.0 and ydotool 1.0.4.

## The problem

After every login, the first time you press **Alt+V** and pick an item in CopyQ, GNOME shows a
**Remote Desktop** pop-up with an "Allow Remote Interaction" switch and **Cancel** / **Share** buttons.

## Why it happens

1. CopyQ runs as an X11 app inside **Xwayland**: its autostart sets `QT_QPA_PLATFORM=xcb`.
2. When you pick an item, CopyQ pastes by faking **Ctrl+V** with the X11 function `XTestFakeKeyEvent`.
3. Xwayland runs with `-enable-ei-portal`, so it turns fake X11 keypresses into a
   **Remote Desktop** permission request to GNOME. That's the pop-up.
4. GNOME forgets the permission at logout, so it asks again after every login.

How it was proved: in `journalctl --user`, every pop-up (`xdg-desktop-portal-gnome: Failed to
associate portal window`) came about 3.5 seconds after `Started app-gnome-copyq-….scope -
Application launched by gsd-media-keys`, which is the Alt+V shortcut.

## The fix

Make CopyQ press Ctrl+V through **ydotool** instead. ydotool fakes keys through the kernel's
virtual input device (`/dev/uinput`), below GNOME, so GNOME never asks.

!!! note "Trade-off"
    Members of the `input` group can fake keyboard input, so any program you run can too.
    Fine on a personal laptop.

### 1. Install ydotool and allow access to /dev/uinput

```bash
sudo apt install ydotool
echo 'KERNEL=="uinput", GROUP="input", MODE="0660", OPTIONS+="static_node=uinput"' | sudo tee /etc/udev/rules.d/80-uinput.rules
sudo usermod -aG input "$USER"
sudo udevadm control --reload && sudo udevadm trigger --name-match=uinput
```

### 2. Reboot

**Reboot. Logging out is not enough.** GNOME Shell runs under the systemd user manager, which can
survive a logout. Group membership is inherited when a process starts, so until a reboot the
desktop still has the old group list.

Check after the reboot (all three must pass):

```bash
id -nG | tr ' ' '\n' | grep -x input                                  # prints: input
awk '/^Groups/' /proc/$(pgrep -o -x gnome-shell)/status              # list includes the input group's id
ls -l /dev/uinput                                                    # crw-rw---- root input
```

### 3. Start the ydotool service at every login

The package ships a systemd **user** unit (`/usr/lib/systemd/user/ydotool.service`, with
`Restart=always`):

```bash
systemctl --user enable --now ydotool.service
systemctl --user is-active ydotool.service      # active
ydotool type ''; echo "exit=$?"                 # exit=0 means the client reaches the service
```

### 4. Make CopyQ paste with ydotool

Add a **script command** that replaces CopyQ's `paste()` function. If ydotool fails (for
example, the service isn't running), it falls back to CopyQ's normal paste, so pasting never
silently stops.

Save this as `copyq-paste.js`:

```js
var cmd = [
  "// Paste with ydotool (kernel uinput) instead of X11 XTest,",
  "// so Xwayland never asks GNOME for Remote Desktop access.",
  "var builtinPaste = global.paste;",
  "global.paste = function() {",
  "  sleep(100);",
  "  var r = execute('ydotool', 'key', '29:1', '47:1', '47:0', '29:0');",
  "  if (!r || r.exit_code !== 0) builtinPaste();",
  "};"
].join(String.fromCharCode(10));
var cs = commands().filter(function(c) { return c.name !== 'Paste with ydotool'; });
cs.push({ name: 'Paste with ydotool', isScript: true, cmd: cmd });
setCommands(cs);
```

Then load it:

```bash
copyq eval "$(cat copyq-paste.js)"
```

`29` is the Linux key code for Left Ctrl and `47` is V; `:1` means press, `:0` release.

!!! warning "Don't write `\n` in `copyq eval`"
    CopyQ turns `\n` in command-line arguments into a real line break, which breaks the
    JavaScript with `SyntaxError: Expected token ')'`. That's why the script uses
    `String.fromCharCode(10)`.

To check it's there: CopyQ → **Commands** (Ctrl+F6) shows "Paste with ydotool", or:

```bash
copyq eval 'commands().map(function(c){return c.name}).join(" | ")'
```

### 5. Test

Open any text box, press **Alt+V**, pick an item. It pastes, and no pop-up appears.

## For reference

- The Alt+V shortcut is a GNOME custom shortcut: Settings → Keyboard → Custom Shortcuts →
  "CopyQ", command `copyq menu '&clipboard' 20 735 260`.
- CopyQ's own options: `activate_pastes=true` and `paste_selected_items=ctrl+v` in
  `~/.config/copyq/copyq.conf`.
- **Alternative without ydotool:** turn off auto-paste (`copyq config activate_pastes false` and
  `copyq config tray_item_paste false`) and press Ctrl+V yourself after picking an item.
- **To undo the fix:** delete the "Paste with ydotool" command in CopyQ, then run
  `systemctl --user disable --now ydotool.service`, `sudo gpasswd -d "$USER" input`,
  `sudo rm /etc/udev/rules.d/80-uinput.rules`, and `sudo apt remove ydotool`.
