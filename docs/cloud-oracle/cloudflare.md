# Cloudflare

**✅ Perfect choice!** Using **Cloudflare** is better than direct DNS.

Cloudflare will give you:

- Free HTTPS (SSL)
- Faster loading (CDN)
- DDoS protection
- Easier management

---

### Step-by-step: Set up **hindex.uk** on Cloudflare

#### 1. Add your domain to Cloudflare

1. Go to [https://dash.cloudflare.com](https://dash.cloudflare.com)
2. Click **+ Add a domain** (or **Add site**)
3. Enter `hindex.uk` and click **Add site**
4. Select the **Free** plan → Continue

Cloudflare will scan your current DNS records.

#### 2. Change Nameservers at your Registrar

Cloudflare will show you **two custom nameservers**, for example:

- `ns1.cloudflare.com`
- `ns2.cloudflare.com`  
  (or something like `abby.ns.cloudflare.com` and `luke.ns.cloudflare.com`)

**Action:**

- Go to your domain registrar (where you bought `hindex.uk`)
- Find **Nameservers** / **DNS Settings**
- Change from default to **Custom**
- Paste the two Cloudflare nameservers
- Save changes

---

#### 3. Add DNS Record in Cloudflare

After nameserver change (wait for activation):

1. In Cloudflare dashboard → Your domain → **DNS** tab
2. Click **Add record**
    - **Type**: `A`
    - **Name**: `@` (for hindex.uk)
    - **IPv4 address**: `141.147.71.47`
    - **Proxy status**: ✅ **Proxied** (orange cloud) ← Very important
3. Add another record for www:
    - **Type**: `A`
    - **Name**: `www`
    - **IPv4 address**: `141.147.71.47`
    - **Proxy status**: ✅ **Proxied**

---

### After DNS Propagates

Once the nameservers change is complete (usually 5–60 minutes), run this on your server:

```bash
# Install Certbot
sudo apt update
sudo apt install certbot python3-certbot-apache -y

# Get and install the certificate
sudo certbot --apache -d hindex.uk -d www.hindex.uk

sudo systemctl restart apache2

```

Or even better — since you're using Cloudflare, you can use **Full (strict)** SSL mode.

Would you like me to guide you with screenshots-style instructions for the next part (SSL + Cloudflare settings)?

Just tell me when you've added the domain and changed the nameservers.