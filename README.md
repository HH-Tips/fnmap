# fnmap - Fast Nmap Wrapper

[Italian version below / Versione italiana sotto]

`fnmap` is a Python-based CLI wrapper for `nmap` designed to streamline and speed up the scanning process. It automatically organizes output files and comes with pre-configured modes for common penetration testing scenarios.

## Features

- **Automated Organization**: All results are saved in a local `nmap/` directory, named after the scan mode (e.g., `nmap/full.nmap`).
- **Smart Defaults**:
    - Includes `-sV` (Version Detection) and `-sC` (Default Scripts) by default.
    - Default packet rate set to `--min-rate 1000`.
    - If no scan mode is specified, it defaults to the **Common Port Scan**.
- **Scan Modes**:
    - `-F`, `--full`: Full scan of all 65,535 ports (`-p-`).
    - `-c`, `--common`: Common port scan (default nmap ports).
    - `-f`, `--fast`: Fast scan of top 100 ports (`-F`).
- **Transparent Arguments**: Any additional flags not recognized by the wrapper are passed directly to `nmap`.

## Usage

```bash
# Basic common scan (default)
fnmap <target>

# Full port scan
fnmap -F <target>

# Fast scan with custom nmap flags
fnmap -f <target> -Pn --reason
```

## Installation

To install `fnmap`, run the following command:

```bash
curl <raw url setup.sh> | bash
```

---

# fnmap - Wrapper veloce per Nmap

`fnmap` è un wrapper CLI in Python per `nmap` progettato per semplificare e velocizzare il processo di scansione. Organizza automaticamente i file di output e include modalità preconfigurate per i comuni scenari di penetration testing.

## Caratteristiche

- **Organizzazione Automatica**: Tutti i risultati vengono salvati in una cartella locale `nmap/`, rinominati in base alla modalità di scansione (es. `nmap/full.nmap`).
- **Impostazioni Intelligenti**:
    - Include `-sV` (rilevamento versione) e `-sC` (script di default) automaticamente.
    - Rate dei pacchetti predefinito a `--min-rate 1000`.
    - Se non viene specificata alcuna modalità, viene eseguita la **Scansione Porte Comuni**.
- **Modalità di Scansione**:
    - `-F`, `--full`: Scansione completa di tutte le 65.535 porte (`-p-`).
    - `-c`, `--common`: Scansione delle porte comuni.
    - `-f`, `--fast`: Scansione veloce delle top 100 porte (`-F`).
- **Argomenti Trasparenti**: Qualsiasi flag aggiuntivo non riconosciuto dal wrapper viene passato direttamente a `nmap`.

## Utilizzo

```bash
# Scansione comune base (default)
fnmap <target>

# Scansione completa di tutte le porte
fnmap -F <target>

# Scansione veloce con flag nmap personalizzati
fnmap -f <target> -Pn --reason
```

## Installazione

Per installare `fnmap`, lancia il seguente comando:

```bash
curl <raw url setup.sh> | bash
```
