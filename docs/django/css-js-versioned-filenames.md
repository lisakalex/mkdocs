# CSS/JS versioned filenames

Excellent question — and it’s one of those details that makes a big difference when you deploy Django (or any web app).

Here’s the full explanation 👇

---

### ✅ What versioned filenames mean

When you enable:

```python
STORAGES = {
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.ManifestStaticFilesStorage",
    },
}
```

Django doesn’t just copy your static files into `STATIC_ROOT` — it **renames them** with a unique hash based on their content.

For example:

```
style.css         →  style.4a87b2.css
app.js            →  app.6d19f0.js
logo.png          →  logo.fda2b3.png
```

And your HTML templates automatically get updated to reference those new names via `{% static '...' %}`.

---

### ✅ Why this is important

1. **Browser caching**

    * Browsers cache static files aggressively for performance.
    * Without versioning, users might see *old* CSS or JS after a deployment, because the browser still thinks `style.css` hasn’t changed.
    * Versioned filenames (like `style.4a87b2.css`) automatically force browsers to fetch the new file when you update it — the hash changes, so it’s treated as a brand new file.

2. **Cache busting**

    * You never need to clear users’ cache manually or append `?v=2.0` to URLs.
    * Django does it automatically based on file content.

3. **CDN friendliness**

    * If you use a CDN (like Cloudflare or AWS CloudFront), cached files can stay for months, because only changed files get new names.
    * This improves load times and reduces bandwidth costs.

4. **Integrity**

    * The hash ensures files match what Django expects — if something is missing or altered on disk, you’ll know immediately (`collectstatic` will fail with a clear error).

---

### ✅ When to use it

Use versioned filenames (`ManifestStaticFilesStorage`) **only in production**.
During development (`DEBUG=True`), it’s better to keep normal filenames — so you can change CSS/JS and see updates instantly without rebuilding.

That’s why Django automatically disables this behavior when `DEBUG=True`.

---

### ✅ Quick summary

| Feature    | Without versioning | With versioning (`ManifestStaticFilesStorage`) |
|------------|--------------------|------------------------------------------------|
| Caching    | May show old files | Always gets fresh files                        |
| CDN use    | Can break easily   | Safe and efficient                             |
| Hashing    | None               | Based on file content                          |
| Deployment | Simple but risky   | Safe, cache-friendly                           |

---

Would you like me to show you a *combined setup* that uses normal filenames in development, but automatic versioning only when `DEBUG=False` (so you don’t have to toggle it manually)?
