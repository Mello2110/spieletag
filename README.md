# 🎲 Spieletag System

> **Für alle, die Spieleabende lieben – egal ob digital oder analog.**

Das Spieletag System ist eine kostenlose Web-App, die euren Spieleabend organisiert: Spiele mischen, Runden ziehen, Punkte tracken – alles in einem, direkt im Browser, keine Installation nötig.

👉 **[Hier klicken, um die App direkt zu starten](https://mello2110.github.io/spieletag/)**

---

## 📖 Inhaltsverzeichnis

- [🚀 Für Spieler – Schnellstart](#-für-spieler--schnellstart)
- [📱 App auf dem Tablet/Handy speichern](#-app-auf-dem-tablethandy-speichern)
- [⚙️ Was kann die App?](#️-was-kann-die-app)
- [🔧 Für Entwickler – Technische Übersicht](#-für-entwickler--technische-übersicht)
  - [Architektur & Stack](#architektur--stack)
  - [Phasen-System](#phasen-system)
  - [State Management](#state-management)
  - [Zieh-Algorithmus & Wahrscheinlichkeiten](#zieh-algorithmus--wahrscheinlichkeiten)
  - [Punkte-System](#punkte-system)
  - [Dancebreak-Engine](#dancebreak-engine)
  - [UI-Komponenten & Design-System](#ui-komponenten--design-system)
  - [Event-System](#event-system)
- [🌐 Selbst hosten (GitHub Pages)](#-selbst-hosten-github-pages)
- [🔮 Roadmap & Ideen](#-roadmap--ideen)

---

## 🚀 Für Spieler – Schnellstart

Keine Ahnung von Technik? Kein Problem. So geht's:

### 1. App öffnen
Ruf einfach den Link auf deinem Handy, Tablet oder PC auf. Fertig – keine Anmeldung, kein Download.

### 2. Spieler eintragen
Tippe die Namen aller Mitspieler ein und klick auf **＋**. Mindestens 2 Spieler werden gebraucht.

### 3. Spiele hinzufügen
Es gibt drei Spiel-Typen:

| Kategorie | Wofür? | Punkte |
|-----------|--------|--------|
| 🟣 **Hauptspiele** | Die großen, wichtigen Spiele des Abends | Steigen pro Runde (z. B. 3, 4, 5 …) |
| 🟢 **Zwischenspiele** | Schnelle Spiele für zwischendurch | Feste Punkte, die ihr selbst festlegt |
| 🟤 **Strafspiele** | Für Verlierer oder Herausforderungen | Feste Punkte, die ihr selbst festlegt |

Klick einfach auf **＋ Hauptspiel**, **＋ Zwischenspiel** oder **＋ Strafspiel** und trag die Spielnamen ein. Optional kannst du kurze Beschreibungen hinzufügen.

### 4. Spieletag starten
Klick auf **Spieletag starten →**. Die App mischt alles und ihr könnt loslegen!

### 5. Spiele ziehen
Jede Runde drückt ihr auf **🎲 Spiel ziehen**. Ein zufälliges Spiel wird angezeigt. Spielt es, tragt danach ein wer gewonnen hat, und zieht das nächste!

### 6. Überraschung: Dancebreak! 💃🕺
Manchmal passiert's einfach: Die App erzwingt spontan eine **Tanzpause** – alle müssen tanzen, keine Ausnahmen! (Kann in den Einstellungen angepasst oder deaktiviert werden.)

### 7. Siegerehrung
Wenn alle Spiele gespielt wurden, gibt's eine animierte Siegerehrung mit finalem Punktestand!

---

## 📱 App auf dem Tablet/Handy speichern

Die App funktioniert wie eine richtige App auf dem Homescreen – ohne App Store!

**iPhone / iPad:**
1. Öffne den Link in **Safari**
2. Tippe auf das **Teilen-Symbol** (Viereck mit Pfeil nach oben)
3. Wähle **„Zum Home-Bildschirm"**
4. Fertig – die App erscheint als Icon auf dem Homescreen!

**Android:**
1. Öffne den Link in **Chrome**
2. Tippe auf die **drei Punkte** oben rechts
3. Wähle **„Zum Startbildschirm hinzufügen"**

---

## ⚙️ Was kann die App?

| Feature | Beschreibung |
|---------|-------------|
| 🎮 Drei Spielkategorien | Hauptspiele, Zwischenspiele, Strafspiele mit je eigenen Punktregeln |
| 🎲 Zufallsziehung | Zufälliges Ziehen mit einstellbaren Wahrscheinlichkeiten pro Kategorie |
| 📊 Live-Scoreboard | Punkte aller Spieler immer im Blick, automatisch aktualisiert |
| 🔁 Wiederholungen | Jedes Spiel kann 1–9× oder unbegrenzt (∞) spielbar sein |
| ↩️ Undo-Funktion | Letzte Runde rückgängig machen, falls beim Eintragen ein Fehler passiert |
| 💃 Dancebreak | Zufällige Tanzpause mit Timer, Fortschrittsbalken und Skip-Option |
| 🌙 Dark Mode | Automatisch an System-Einstellung angepasst, manuell umschaltbar |
| 📱 PWA-ready | Als App auf iOS & Android installierbar (kein App Store nötig) |
| 🔄 Neustart-Optionen | Gleiche Spiele nochmal / Setup anpassen / Komplett neu |
| 🏆 Siegerehrung | Animierte Abschlussansicht mit Ranking aller Spieler |

---

## 🔧 Für Entwickler – Technische Übersicht

### Architektur & Stack

```
Spieletag System
└── index.html          ← Einzige Datei – Self-contained SPA
    ├── <style>          ← Komplettes CSS-Design-System (~330 Zeilen)
    ├── <body>           ← Semantisches HTML mit 3 Phasen-Views
    └── <script>         ← Vanilla JS (~420 Zeilen), kein Framework
```

- **Stack:** Reines HTML5 / CSS3 / Vanilla JavaScript – zero dependencies
- **Paradigma:** Single-File SPA mit manuellem Phasen-Routing
- **Persistenz:** `localStorage` für Dark-Mode-Präferenz
- **Fonts:** Google Fonts (DM Sans + Playfair Display via CDN)
- **Hosting:** Statisch hostbar auf GitHub Pages, Netlify, Vercel o. ä.
- **PWA-Features:** Apple Web App Meta-Tags, Touch-Icon, Viewport-Lock, iOS-Zoom-Prevention (`font-size: 16px` auf allen Inputs)

---

### Phasen-System

Die App verwendet ein 3-Phasen-Modell mit Dot-Navigation:

```
Phase 0 (Setup) → Phase 1 (Play) → Phase 2 (Winner)
```

```js
function setPhase(n) {
  // Versteckt alle Phase-Views per .hidden-Klasse
  // Aktualisiert Phase-Dots (active / done)
  // Scrollt nach oben
}
```

Phasen-IDs im DOM: `#phase-setup`, `#phase-play`, `#phase-winner`

---

### State Management

Globaler State in Modul-Scope-Variablen (kein Framework):

```js
let players = []           // String[] – Spieler-Namen
let allGames = []          // Game[] – alle konfigurierten Spiele
let remainingGames = []    // Game[] – noch ziehbarer Pool (nach filter)
let history = []           // HistoryEntry[] – gespielte Runden
let scores = {}            // { [name: string]: number }
let mainGameCounter = 0    // Zähler für progressive Hauptspiel-Punkte
let currentGame = null     // Aktuell gezogenes Spiel-Objekt
let savedGames = []        // Snapshot für Neustart ohne Re-Setup
let savedPlayers = []      // Snapshot für Neustart ohne Re-Setup
let dancebreakTimer = null // setInterval-Referenz für Countdown
let dancebreakActive = false

let settings = {
  dancebreak: bool,
  dancebreakDuration: number,    // Sekunden
  dancebreakChance: number,      // 0.0–1.0
  mainPtsStart: number,          // Startpunkte Hauptspiele
  mainPtsStep: number,           // Punkte-Inkrement pro Hauptspiel
  endConditions: {               // Welche Kategorien triggern Spielende
    main: bool, between: bool, penalty: bool
  },
  probRandom: bool,              // Urnen-Modus vs. fixe Gewichtungen
  probWeights: {                 // Prozentuale Gewichtungen pro Kategorie
    main: number|null, between: number|null, penalty: number|null
  },
  probUserSet: {                 // Hat der User diese Kategorie manuell gesetzt?
    main: bool, between: bool, penalty: bool
  }
}
```

**Game-Objekt Schema:**
```js
{
  type: 'main' | 'between' | 'penalty',
  name: string,
  desc: string,
  points: number,          // Für between/penalty; bei main berechnet
  maxRepeats: number,      // 0 = unendlich
  timesPlayed: number,     // Zähler
  uid: string,             // 'g0', 'g1', … – für Undo-Lookups
  _drawPoints: number      // Transient: Punkte zum Zeitpunkt des Ziehens
}
```

---

### Zieh-Algorithmus & Wahrscheinlichkeiten

Das Herzstück der App. Zwei Modi:

**Modus 1: Urnen-Prinzip (Standard)**
```js
// Alle verbleibenden Spiele im Pool gleich wahrscheinlich
currentGame = pool[Math.floor(Math.random() * pool.length)]
```

**Modus 2: Gewichtetes Ziehen mit hybridem Urnen-Prinzip**

Nutzer kann einzelne Kategorien fixieren (z. B. „Hauptspiele immer 50%"), der Rest verteilt sich proportional wie in einer Urne.

```js
// Fixierte Kategorien: Weight = probability / anzahl_spiele_in_kategorie
// Freie Kategorien:    Weight = freeShare / anzahl_freie_spiele_gesamt
// → Weighted Random via kumulativer Summe (linearer Scan)
let roll = Math.random() * totalW;
for (let i = 0; i < weights.length; i++) {
  roll -= weights[i];
  if (roll <= 0) { picked = i; break; }
}
```

Die Wahrscheinlichkeitsvorschau (`calcProbabilities()`) berechnet live, wie sich freie Kategorien den verbleibenden Prozentsatz teilen und zeigt visuelle Balken-Indikatoren.

---

### Punkte-System

**Hauptspiele – Progressive Punkte:**
```js
// Beim Ziehen (nicht beim Konfigurieren)
mainGameCounter++;
drawPoints = settings.mainPtsStart + settings.mainPtsStep * (mainGameCounter - 1)
// Beispiel: Start 3, Step 1 → 3, 4, 5, 6, 7 …
```

**Zwischen-/Strafspiele – Feste Punkte:**
Werden beim Konfigurieren eingetragen und direkt auf `scores[player]` addiert.

**Undo-Logik:**
```js
// Punkte rückabwickeln, mainGameCounter korrigieren, timesPlayed--
// History-Entry wird gespliced, kein vollständiger State-Rebuild nötig
```

---

### Dancebreak-Engine

```js
function showDancebreak(cb) {
  // Injiziert Fullscreen-Overlay ins DOM
  // setInterval() – Countdown in Sekunden
  // Fortschrittsbalken via CSS width-Transition (linear, 1s)
  // Skip-Button ruft endDancebreak(cb) auf
}
function endDancebreak(cb) {
  // clearInterval, Overlay fade-out (CSS opacity 0)
  // setTimeout → remove(), dann callback ausführen
}
```

Trigger: Vor jedem `drawGame()`-Call mit konfigurierbarer Wahrscheinlichkeit (`Math.random() < settings.dancebreakChance`). `dancebreakActive`-Flag verhindert rekursive Trigger.

---

### UI-Komponenten & Design-System

**CSS Custom Properties (Design Tokens):**
```css
:root {
  --accent: #4F253D        /* Primary – Burgund/Dunkelviolett */
  --complement: #25504F    /* Secondary – Dunkelgrün */
  --bg / --bg-card         /* Hintergrundebenen */
  --border / --border-hover
  --shadow-sm/md/lg
  --radius: 12px / --radius-sm: 8px
  --transition: 0.2s ease
}
html.dark { /* Komplettes Dark-Mode Override aller Tokens */ }
```

**Komponenten-Bibliothek:**
| Klasse | Beschreibung |
|--------|-------------|
| `.card` | Container mit Elevation, Border, Border-Radius |
| `.btn`, `.btn-primary`, `.btn-secondary`, `.btn-complement`, `.btn-add` | Button-Varianten |
| `.toggle-switch` | Custom Checkbox-Toggle (touch-optimiert, 52×32px) |
| `.draw-card` | Game-Reveal-Karte mit type-spezifischer Border-Farbe |
| `.scoreboard` | Dark-Background Live-Score-Liste |
| `.history-item` | Spielverlauf-Einträge mit Undo-Button |
| `.shuffle-overlay` | Fullscreen Kartenmisch-Animation |
| `.dancebreak-overlay` | Fullscreen Tanzpausen-Overlay |
| `.prob-bar` | Visuelle Wahrscheinlichkeits-Indikatoren |
| `.phase-dot` | Fortschritts-Navigation (active/done States) |

**Animationen:**
- `slideIn` – neue Input-Felder
- `danceIn` – Dancebreak-Overlay Erscheinen
- `danceBounce` – Emoji-Loop-Animation
- Karten-Flip via `rotateY` + cubic-bezier spring-Easing
- Shuffle-Animation: randomisierte `translate/rotate` via `setInterval`

**Touch-Optimierungen:**
- Alle interaktiven Elemente `min-height: 44px` / `min-width: 44px`
- `-webkit-tap-highlight-color: transparent` überall
- `touch-action: manipulation` gegen Doppeltipp-Zoom
- Inputs `font-size: 16px` (verhindert iOS Auto-Zoom)
- `user-scalable=no` im Viewport-Meta

---

### Event-System

Single event delegation auf `document` für dynamisch erzeugte Elemente:

```js
document.addEventListener('click', function(e) {
  if (t.dataset.removePlayer) { ... }  // Player-Tags
  if (t.dataset.removeField)  { ... }  // Game-Input-Felder
  if (t.dataset.undo !== undefined) { ... }  // History Undo-Buttons
  // Winner-Screen Buttons, Dance-Skip via ID-Checks
})
```

Statische Elemente haben direkte `addEventListener`-Bindungen beim Init.

---

## 🌐 Selbst hosten (GitHub Pages)

### Schritt 1: GitHub Repository erstellen
1. Erstelle einen kostenlosen Account auf [github.com](https://github.com)
2. Klick oben rechts auf **`+`** → **`New repository`**
3. Name vergeben (z. B. `spieletag`), auf **Public** setzen, **Create repository** klicken

### Schritt 2: Datei hochladen
1. Klick auf **`uploading an existing file`**
2. `index.html` und `apple-touch-icon.png` hochladen
3. Auf **Commit changes** klicken

### Schritt 3: GitHub Pages aktivieren
1. Im Repository → **Settings** → **Pages**
2. Unter `Source`: Branch **`main`**, Ordner **`/(root)`** wählen
3. Auf **Save** klicken
4. Nach 1–2 Minuten erscheint euer Link: `https://USERNAME.github.io/spieletag/`

> **Tipp:** Den Link als Favorit speichern oder als App auf dem Homescreen ablegen – fertig!

---

## 🌐 Multiplayer & Firebase Setup

Das System unterstützt einen echten Live-Multiplayer-Modus (Host & Guests), sodass jeder auf seinem eigenen Gerät das Spiel mitverfolgen kann und Gäste Spiele vorschlagen können! 
Damit der Multiplayer-Modus funktioniert, musst du **einmalig ein kostenloses Firebase-Projekt** erstellen und die Zugangsdaten in die `index.html` eintragen.

### Schritt 1: Firebase-Projekt erstellen
1. Gehe zu [console.firebase.google.com](https://console.firebase.google.com/) und logge dich mit einem Google-Account ein.
2. Klicke auf **Projekt hinzufügen** (Name z.B. "Spieletag").
3. Google Analytics kannst du für dieses Projekt **deaktivieren**.

### Schritt 2: Realtime Database einrichten
1. Klicke links im Menü unter *Build* (oder *Erstellen*) auf **Realtime Database**.
2. Klicke auf **Datenbank erstellen**.
3. Wähle den Standort (z.B. *Belgium/Europe*) und starte im **Testmodus**.
4. Wichtig: Gehe nach der Erstellung auf den Reiter **Regeln (Rules)** und kopiere Folgendes hinein:
```json
{
  "rules": {
    "sessions": {
      "$code": {
        ".read": true,
        "meta": { ".write": "auth == null" },
        "proposals": { ".write": true },
        "approvedGames": { ".write": true },
        "gameState": { ".write": true },
        "settings": { ".write": true },
        "players": { ".write": true }
      }
    }
  }
}
```
5. Klicke auf **Veröffentlichen**.

### Schritt 3: Web-App hinzufügen & Config kopieren
1. Gehe zur Projektübersicht (Zahnrad oben links -> Projekteinstellungen).
2. Scrolle nach unten zu "Meine Apps" und klicke auf das **</> Web-Icon**.
3. Gib einen App-Namen ein (z.B. "Web App") und klicke auf App registrieren.
4. Es erscheint ein Code-Block. Kopiere das Objekt `firebaseConfig` (die Zeilen mit apiKey, authDomain, databaseURL, etc.).

### Schritt 4: Config in der `index.html` eintragen
1. Öffne die `index.html` mit einem Texteditor.
2. Scrolle ganz nach unten zum Bereich `<script>`.
3. Gleich am Anfang des Scripts findest du den Platzhalter `const firebaseConfig = { ... }`.
4. Ersetze diesen Block mit der kopierten Config aus Schritt 3.
5. Speichere die Datei. **Fertig! Dein Live-Multiplayer ist jetzt einsatzbereit.**

---

*Made with ❤️ for game nights – built as a single HTML file, no dependencies, no BS.*
