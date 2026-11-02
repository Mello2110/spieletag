---
id: "spieletag"
title: "Spieletag System"
tagline: "Turnkey game night manager with weighted game drawing, live scoring, and real-time cloud sync."
category: "webapp"
status: "production"
featured: false
badge: "Open Source"
problemStatement: "Coordinating game nights and party tournaments is often disrupted by chaotic scorekeeping, decision fatigue, and disjointed rule management. Traditional manual setups lack dynamic replay balancing, turn-by-turn fairness, and instant state sharing across participants' individual devices. Hosts frequently spend more time managing session logistics than actually playing."
technicalSolution: "The application implements a lightweight, dependency-free Progressive Web App driven by a phase-based state machine and a hybrid urn-randomization algorithm with real-time probability redistribution. It combines local state persistence, procedural Web Audio generation, and Canvas animations with Firebase Realtime Database for live guest synchronization and community presets. A custom Service Worker caching strategy ensures full offline operability for local play."
techStack:
  - "JavaScript (ES6+)"
  - "HTML5 & CSS3"
  - "Firebase Realtime Database"
  - "Firebase Authentication"
  - "Service Worker API (PWA)"
  - "Web Audio API"
  - "HTML5 Canvas API"
architectureHighlights:
  - "Zero-dependency single-page architecture with state-driven view transitions"
  - "Hybrid urn-based weighted random algorithm with real-time probability recalculation"
  - "Real-time multi-device synchronization via Firebase Realtime Database and Auth"
  - "Offline-first PWA caching with background state persistence and reload recovery"
links:
  chromeWebStore: ""
  demoUrl: "https://mello2110.github.io/spieletag/"
  githubUrl: "https://github.com/Mello2110/spieletag"
sandbox:
  enabled: true
  type: "remote"
  embedUrl: "https://mello2110.github.io/spieletag/"
  notes: ""
stats:
  version: "v1.0.0"
---

# Spieletag System

[![Status](https://img.shields.io/badge/Status-Active-emerald?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](#)
[![PWA](https://img.shields.io/badge/PWA-Ready-orange?style=flat-square)](#)
[![Firebase](https://img.shields.io/badge/Backend-Firebase%20RTDB-amber?style=flat-square)](#)

> Turnkey game night manager with weighted game drawing, live scoring, and real-time cloud sync.

<!-- QUICK ACCESS / CALL TO ACTION -->
<p align="left">
  <a href="https://mello2110.github.io/spieletag/"><b>🚀 Live Demo / Web App</b></a> &nbsp;|&nbsp;
  <a href="https://github.com/Mello2110/spieletag"><b>💻 GitHub Repository</b></a> &nbsp;|&nbsp;
  <a href="https://github.com/Mello2110"><b>🌐 Mellow Solutions Hub</b></a>
</p>

---

## 📌 Problem & Motivation

Organizing structured board and party game events involves significant friction:
- **Decision Fatigue & Pacing:** Deciding what game to play next usually leads to prolonged debates, while balancing quick mini-games against main events requires active moderation.
- **Error-Prone Manual Scoring:** Paper notes or general note-taking apps do not adapt to progressive point scales (e.g., escalating stakes as the evening unfolds) and lack instant audit trails or undo capabilities.
- **Display Bottlenecks:** Guests gathered around a table have to lean over a single notepad or screen to check who is leading, or ask the host for constant updates.
- **Setup Overhead & Fragility:** Dedicated apps often demand native installation or mandatory account registrations before guests can even view the current game status. Accidental browser refreshes frequently wipe in-memory progress entirely.

**Spieletag System** solves this by providing a zero-install, browser-based management engine that handles randomized game drawing, progressive scoring, and multi-device cloud synchronization seamlessly.

---

## ⚡ The Solution

Spieletag System is constructed as a self-contained, zero-dependency Progressive Web App (PWA). It acts as an autonomous referee and game-master for physical and digital game sessions:

1. **State Machine Navigation:** A deterministic multi-phase lifecycle (`#phase-session` &rarr; `#phase-lobby` &rarr; `#phase-setup` &rarr; `#phase-play` &rarr; `#phase-winner`) ensures clean transitions and predictable DOM state.
2. **Hybrid Urn & Weighted Selection Algorithm:** Supports both equal-probability urn sampling and fine-grained category weights with dynamic recalculation of unconstrained categories.
3. **Real-Time Multi-Device Sync:** Powered by Firebase Realtime Database, a host generates a 4-letter room code or QR code; guests join instantly on their smartphones to follow live draws and propose games.
4. **Resilient Local Play & Offline Execution:** A custom Service Worker caches all core assets for offline play. An active session snapshot is mirrored to `localStorage` on every turn, protecting ongoing tournaments against accidental browser refreshes.

---

## 🚀 Key Features

- 🎲 **Three Distinct Game Categories:**
  - **Main Games (Hauptspiele):** High-stake tournament games with customizable progressive point scaling (e.g., 3, 4, 5, 6... points per round).
  - **Intermediary Games (Zwischenspiele):** Quick filler rounds with custom fixed point rewards.
  - **Penalty Games (Strafspiele):** Challenge games configured for trailing players or specific punishment rules.
- ⚖️ **Hybrid Weighted Random Drawing:** Draw games using either an urn-sampling model or user-defined percentage allocations across categories, complete with real-time probability bar indicators.
- ☁️ **Live Cloud Multiplayer & Guest Participation:**
  - One-tap QR code and invitation link (`?join=ROOM`) joining.
  - Live broadcast of game draws, timers, and updated leaderboards to all connected devices.
  - Guest proposal queue allowing participants to submit games directly from their phones.
- ⚡ **1-Tap Winner Chips & Undo Stack:** Select single winners, "All", or "None" with a single touch. Integrated immutable-style undo stack allows rewinding misrecorded rounds without resetting game state.
- 📚 **Game Library & Preset Management:** Save personal favorites or browse global community games. Store entire session presets (players, game collections, and rule sets) for instant one-click reloading.
- 💃 **Procedural "Dancebreak" Intermissions:** Configurable surprise mini-events with an animated progress bar and countdown to energize player groups.
- 🔊 **Zero-Asset Web Audio Synthesizer:** Built-in procedural sound synthesis generates custom chimes, card flips, buzzers, and victory fanfares without downloading audio files.
- 📱 **Installable PWA & Responsive Touch UI:** Designed with 44px touch targets, iOS safe-area compliance, native standalone manifest support, and full dark/light theme switching.

---

## 🛠️ Architecture & Tech Stack

### Technology Stack
- **Frontend Core:** Pure Vanilla JavaScript (ES6+), semantic HTML5, modern CSS3 (Custom Properties & Design Tokens).
- **Backend & Persistence:** Firebase Realtime Database (`firebase-database-compat.js`) for room state & proposals; Firebase Authentication (`firebase-auth-compat.js`) with pseudonymized user credentials (`username@spieletag.local`).
- **Offline & PWA:** Service Worker API (`sw.js`) utilizing a network-first strategy for navigation and cache-first for static assets; W3C Web App Manifest.
- **Multimedia:** Native Web Audio API for synthesized acoustic feedback; HTML5 Canvas API for real-time confetti particle simulations.

### Core Architecture

```
Spieletag System
├── index.html          ← Self-contained SPA (markup, CSS tokens, phase engine, UI handlers)
├── sw.js               ← Service Worker (offline cache management & network strategies)
├── manifest.json       ← W3C Web App Manifest (PWA metadata & standalone display config)
└── icon.png            ← High-resolution application icon (1024x1024 maskable)
```

- **Phased State Lifecycle:** View rendering is managed without external frameworks through declarative phase toggling:
  ```js
  // Session Choice -> Lobby -> Setup -> Play -> Winner
  function setPhase(phaseId) {
    document.querySelectorAll('.phase').forEach(el => el.classList.add('hidden'));
    document.getElementById(phaseId).classList.remove('hidden');
    updateNavigationIndicators();
  }
  ```
- **Hybrid Urn Weighted Algorithm:**
  ```js
  // Fixed category weight: Weight = probability / items_in_category
  // Floating categories:   Weight = remaining_probability / total_floating_items
  // Cumulative weighted distribution sampling:
  let roll = Math.random() * totalWeight;
  for (let i = 0; i < pool.length; i++) {
    roll -= pool[i].weight;
    if (roll <= 0) { pickedGame = pool[i]; break; }
  }
  ```
- **Event-Driven DOM Delegation:** Dynamic list entries (player tags, library chips, history entries) use centralized delegation on `document` to maintain minimal memory footprint and zero leak risks.

---

## 📦 Installation & Usage

### 1. Direct Browser Access (End Users)
No compilation or installation required. Open the official web app in any standard browser:
👉 **[Launch Spieletag System](https://mello2110.github.io/spieletag/)**

To install as an app on your smartphone or tablet:
- **iOS (Safari):** Tap the **Share** button &rarr; Select **Add to Home Screen**.
- **Android (Chrome):** Tap the **three-dot menu** &rarr; Select **Install app** or **Add to Home Screen**.

### 2. Local Development & Self-Hosting

Clone the repository and serve it using any static web server:

```bash
# Clone the repository
git clone https://github.com/Mello2110/spieletag.git
cd spieletag

# Serve locally using Python 3
python -m http.server 8080

# Or serve using Node.js / npx
npx serve .
```

Open `http://localhost:8080` in your web browser.

### 3. Optional: Configuring Your Own Firebase Backend
For custom multiplayer hosting and private database instances:
1. Create a free project at [Firebase Console](https://console.firebase.google.com/).
2. Enable **Realtime Database** and **Authentication** (Email/Password provider).
3. Copy your project configuration object and replace the `firebaseConfig` object at the bottom of `index.html`:
   ```javascript
   const firebaseConfig = {
     apiKey: "YOUR_API_KEY",
     authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
     databaseURL: "https://YOUR_PROJECT_ID-default-rtdb.firebaseio.com",
     projectId: "YOUR_PROJECT_ID",
     storageBucket: "YOUR_PROJECT_ID.appspot.com",
     messagingSenderId: "...",
     appId: "..."
   };
   ```

---

## 📄 License & Disclaimer

Part of the **Mellow Solutions** portfolio. Provided under the MIT License as-is for non-commercial and personal utility.
