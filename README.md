# Work Tracker — Setup Guide

## What's in this folder

```
work-tracker/
├── index.html      ← The app itself
├── manifest.json   ← Makes it installable as a PWA
├── sw.js           ← Lets it work offline
└── icons/
    ├── icon-192.png
    └── icon-512.png
```

---

## Step 1 — Create a GitHub account (if you don't have one)

1. Go to https://github.com
2. Click **Sign up** and create a free account

---

## Step 2 — Create a new repository

1. Once logged in, click the **+** icon (top right) → **New repository**
2. Name it: `work-tracker`
3. Make sure it's set to **Public**
4. Check **"Add a README file"**
5. Click **Create repository**

---

## Step 3 — Upload your files

1. Inside your new repo, click **Add file** → **Upload files**
2. Upload ALL files from this folder:
   - `index.html`
   - `manifest.json`
   - `sw.js`
3. For the icons, click **Add file** → **Create new file**
   - Type `icons/` in the name field (this creates the folder)
   - Then upload `icon-192.png` and `icon-512.png`
4. Click **Commit changes**

---

## Step 4 — Enable GitHub Pages

1. In your repo, click **Settings** (top tab)
2. Scroll down to **Pages** in the left sidebar
3. Under **Source**, select **Deploy from a branch**
4. Under **Branch**, select `main` and `/ (root)`
5. Click **Save**
6. Wait 1–2 minutes, then your app will be live at:
   `https://YOUR-USERNAME.github.io/work-tracker`

---

## Step 5 — Install as a desktop app (Chrome)

1. Open Chrome and go to your URL above
2. In the address bar, look for the **install icon** (a circle with a + sign)
3. Click it → **Install**
4. The app opens in its own window with its own icon!

On Mac: it also appears in your Applications folder
On Windows: it appears in your Start menu and taskbar

---

## Adding your Google Sheets URL

1. Open the installed app
2. Tap the ⚙ settings icon (top right)
3. Paste your Apps Script web app URL
4. Optionally add your secret key
5. Save — you're all set!
