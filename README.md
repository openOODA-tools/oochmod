# oochmod: Sovereign PERMISSION MANAGER

<div align="center">

```
================================================================================
                                oochmod
            Sovereign openOODA PERMISSION MANAGER & CHMOD
================================================================================
```

**Sovereign PERMISSION MANAGER**  
*Applies octal and symbolic permission masks with systemd-tmpfiles declarative synthesis.*  
*Two Faces, One Engine:* Modern terminal ergonomics for humans • Zero-leakage MCP for AI agents  
Written in 100% pure [openOODA](https://github.com/openOODA).

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![openOODA](https://img.shields.io/badge/openOODA-1.0-emerald.svg)](https://openooda.org)
[![Architecture: x86_64 | aarch64](https://img.shields.io/badge/Arch-x86__64%20%7C%20aarch64-lightgrey.svg)]()

</div>

---

## 1. Quick Install

### Automated Installer (Linux x86_64 & aarch64)
```bash
curl -fsSL https://openOODA-tools.github.io/oochmod/install.sh | bash
```

### Native Package Managers
```bash
# Arch Linux (AUR / PKGBUILD)
yay -S oochmod-bin
# Or manual PKGBUILD:
cd packaging/arch && makepkg -si

# Debian / Ubuntu (.deb)
curl -fsSL https://openOODA-tools.github.io/oochmod/install.sh | bash -s -- --deb

# Fedora / RHEL (.rpm)
curl -fsSL https://openOODA-tools.github.io/oochmod/install.sh | bash -s -- --rpm
```

### Uninstallation
```bash
oochmod-uninstall
# or: curl -fsSL https://openOODA-tools.github.io/oochmod/uninstall.sh | bash
```

---

## 2. CLI Usage

```
oochmod 0.2.0 (openOODA sovereign files & navigation)
usage: oochmod [OPTION]... MODE[,MODE]... FILE...
  or:  oochmod [OPTION]... OCTAL-MODE FILE...
  or:  oochmod [OPTION]... --reference=RFILE FILE...

Change the mode of each FILE to MODE.

Options:
  -c, --changes          like verbose but report only when a change is made
  -f, --silent, --quiet  suppress most error messages
  -v, --verbose          output a diagnostic for every file processed
  -R, --recursive        change files and directories recursively
      --reference=RFILE  use RFILE's mode rather than MODE values
      --dry-run          simulate permission changes without disk writes
      --tmpfiles         synthesize declarative systemd-tmpfiles rules
      --demo             run demonstration scenarios with synthetic fixtures
      --json             output formatted as JSON Lines
  -h, --help             display this help and exit
  -V, --version          output version information and exit
      --mcp              run as Model Context Protocol stdio server
```

---

## 3. Declarative systemd-tmpfiles Synthesis

Following pure systemd-native server architecture, `oochmod` emits declarative rules for `/etc/tmpfiles.d/*.conf`:

```bash
# Generate declarative non-recursive (z) and recursive (Z) rules:
oochmod --tmpfiles 0755 /usr/local/bin/deploy.sh
oochmod --tmpfiles -R 0750 /var/www/app
```

Output:
```ini
# /etc/tmpfiles.d/oochmod.conf - declarative permission rules
# Type Path Mode UID GID Age Argument
z /usr/local/bin/deploy.sh 0755 - - - -
```

---

## 4. Model Context Protocol (MCP)

When invoked with `--mcp`, `oochmod` runs a JSON-RPC 2.0 stdio server providing structured tools for AI coding agents:

```bash
oochmod --mcp
```

### Registered Tools
* **`chmod_parse`**: Parse symbolic or octal mode string into normalized octal and 9-char symbolic format.
* **`chmod_inspect`**: Inspect filesystem path permission bits in octal and symbolic formats.
* **`chmod_plan`**: Plan permission mode changes for a path without disk modification.
* **`chmod_tmpfiles`**: Synthesize declarative systemd-tmpfiles rule for path.
* **`chmod_audit`**: Audit path permissions against expected baseline mode.

---

## 5. Security & Zero Ambient Authority

* **Pure Capability Bounded:** Operates strictly with explicit tokens (`&FsReadCap`, `&ProcessCap`, `&EnvCap`). Physical absence of ambient disk/net leakage.
* **Negative-Trust Architecture:** Strict input validation and operational limits.
* **Hermetic Binary:** Standalone zero-dependency executable.

---

## 6. License

Apache License, Version 2.0. See [LICENSE](LICENSE) for details.
