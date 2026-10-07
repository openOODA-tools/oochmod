Name:           oochmod
Version:        0.1.0
Release:        1%{?dist}
Summary:        Applies octal and symbolic permission masks with capability boundary constraints.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oochmod
Source0:        oochmod-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oochmod is a sovereign, capability-bounded MODE CHANGER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oochmod
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oochmod-uninstall

%files
/usr/bin/oochmod
/usr/bin/oochmod-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
