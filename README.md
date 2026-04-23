# 🚀 fnmap - Fast Nmap Wrapper

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Nmap-Wrapper-green?style=for-the-badge&logo=nmap" alt="Nmap">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20macOS-lightgrey?style=for-the-badge" alt="Platform">
</p>

<p align="center">
  <b>[ <a href="#it">Versione Italiana 🇮🇹</a> ]</b>
</p>

`fnmap` is a powerful Python-based CLI wrapper for `nmap` designed to streamline and speed up the scanning process. It eliminates repetitive typing by automating output organization and providing pre-configured modes for common penetration testing scenarios.

---

## ✨ Features

- 📂 **Automated Organization**: All results are automatically saved in a local `nmap/` directory, named logically based on the scan mode (e.g., `nmap/full.nmap`).
- ⚙️ **Smart Defaults**: 
    - Automatically includes `-sV` (Version Detection) and `-sC` (Default Scripts).
    - Performance optimized with `--min-rate 1000`.
    - Fallback to **Common Port Scan** if no mode is specified.
- 🛠️ **Transparent Arguments**: Any flags not recognized by `fnmap` are passed directly to the underlying `nmap` engine.

## 🚀 Scan Modes

| Flag | Mode | Nmap Equivalent | Description |
| :--- | :--- | :--- | :--- |
| `-F` / `--full` | **Full** | `-p-` | Scans all 65,535 ports |
| `-c` / `--common` | **Common** | (Default) | Scans the most common ports |
| `-f` / `--fast` | **Fast** | `-F` | Scans the top 100 ports |

## 💻 Usage

```bash
# 🔹 Basic common scan (default)
fnmap <target>

# 🔹 Full port scan
fnmap -F <target>

# 🔹 Fast scan with custom nmap flags (e.g., disable ping & show reason)
fnmap -f <target> -Pn --reason
```

## 📦 Installation

Install `fnmap` quickly using the one-liner script:

```bash
curl https://raw.githubusercontent.com/HH-Tips/fnmap/refs/heads/main/setup.sh | bash
```

---

# <a name="it"></a>🇮🇹 fnmap - Wrapper veloce per Nmap

`fnmap` è un wrapper CLI in Python per `nmap` progettato per semplificare e velocizzare il processo di scansione. Organizza automaticamente i file di output e include modalità preconfigurate per i comuni scenari di penetration testing.

---

## ✨ Caratteristiche

- 📂 **Organizzazione Automatica**: Tutti i risultati vengono salvati in una cartella locale `nmap/`, rinominati in base alla modalità di scansione (es. `nmap/full.nmap`).
- ⚙️ **Impostazioni Intelligenti**: 
    - Include `-sV` (rilevamento versione) e `-sC` (script di default) automaticamente.
    - Rate dei pacchetti predefinito a `--min-rate 1000`.
    - Se non viene specificata alcuna modalità, viene eseguita la **Scansione Porte Comuni**.
- 🛠️ **Argomenti Trasparenti**: Qualsiasi flag aggiuntivo non riconosciuto dal wrapper viene passato direttamente a `nmap`.

## 🚀 Modalità di Scansione

| Flag | Modalità | Equivalente Nmap | Descrizione |
| :--- | :--- | :--- | :--- |
| `-F` / `--full` | **Completa** | `-p-` | Scansione di tutte le 65.535 porte |
| `-c` / `--common` | **Comuni** | (Default) | Scansione delle porte più comuni |
| `-f` / `--fast` | **Veloce** | `-F` | Scansione delle top 100 porte |

## 💻 Utilizzo

```bash
# 🔹 Scansione comune base (default)
fnmap <target>

# 🔹 Scansione completa di tutte le porte
fnmap -F <target>

# 🔹 Scansione veloce con flag nmap personalizzati (es. senza ping e con motivo)
fnmap -f <target> -Pn --reason
```

## 📦 Installazione

Per installare `fnmap`, lancia il seguente comando:

```bash
curl https://raw.githubusercontent.com/HH-Tips/fnmap/refs/heads/main/setup.sh | bash
```