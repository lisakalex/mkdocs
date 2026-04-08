# IntelliJ scrolling

**Yeah, this is a super common complaint on Ubuntu** — native GTK apps like the default GNOME Text Editor (or gedit)
scroll buttery smooth because they play nice with GNOME’s compositor, but **IntelliJ (and other JetBrains IDEs)** use
their own Java/Swing rendering, which often feels jerky, stuttery, or “stepped” in comparison.

Here are the fixes that actually work for most people (in order of easiest → more involved):

### 1. Quickest fix: Switch away from the “Islands” theme (especially if you’re on IntelliJ 2025.x or newer)

Recent versions introduced the fancy **Island Dark / Island Light** themes and they absolutely destroy scrolling/UI
performance on Linux.

- Go to **Settings → Appearance & Behavior → Appearance**
- Change **Theme** from “Island Dark” (or whatever Islands variant) to plain **Dark** (or **IntelliJ Light**)
- Restart the IDE

A ton of Ubuntu users reported this instantly fixed scrolling lag, tab switching, everything. If you like the Islands
look, you can also try disabling “Show Project Gradient” in the same Appearance section.

### 2. Toggle Smooth Scrolling in the editor

- **Settings → Editor → General**
- Check/uncheck **Smooth scrolling**
- Some people need it **on**, some need it **off** — just flip it and test.

### 3. Force native Wayland support (biggest smoothness win on modern Ubuntu)

Ubuntu uses Wayland by default now. IntelliJ still falls back to XWayland in many cases, which feels rough.

- In IntelliJ: **Help → Edit Custom VM Options…**
- Add this line at the very bottom:

```
-Dawt.toolkit.name=WLToolkit
```

- Save and restart the IDE.

This makes IntelliJ talk directly to Wayland instead of going through the compatibility layer. Scrolling becomes much
closer to native apps.

### 4. If still bad, disable the Metal renderer

Add this to the same **Custom VM Options** file:

```
-Dsun.java2d.metal=false
```

Then restart. This helps a lot of Linux users with choppy scrolling and high CPU/GPU spikes while scrolling.

### 5. Test X11 session (quick diagnostic)

Sometimes native Wayland + JetBrains still has quirks.

1. Log out.
2. On the login screen, click the gear icon (bottom right) → choose **Ubuntu on Xorg**.
3. Log in and test scrolling in IntelliJ.

If it becomes smooth, you know it’s a Wayland thing and the VM option above should fix it.

### Extra tips if none of the above fully solve it

- Make sure you’re on the latest stable IntelliJ (2026.1+ has better Wayland support by default).
- If you have NVIDIA GPU → check the Reddit thread about RTX + PRIME + Wayland stuttering (there are specific driver
  tweaks).
- Try running IntelliJ from the Toolbox app instead of the manual .tar.gz (sometimes cleaner).
- Turn off unnecessary plugins temporarily (Help → Diagnostic Tools → Run in Safe Mode) to rule out plugin interference.

**Tell me a bit more so I can narrow it down**:

- Ubuntu version? (`lsb_release -a`)
- IntelliJ version? (Help → About)
- Wayland or X11 right now? (`echo $XDG_SESSION_TYPE`)
- Laptop/desktop + NVIDIA/AMD/Intel GPU?
- Touchpad or mouse?

Drop those and I can give you the exact command or setting you need. You’re not alone — this one drives a lot of us
crazy until the right checkbox/VM flag is flipped.  
