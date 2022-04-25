Name:    bp_watchdog
Version: %{__version}
Release: %{__release}%{?dist}

License: GNU AGPLv3
URL: https://github.com/redBorder/bp_watchdog
Source0: %{name}-%{version}.tar.gz

Requires: bpctl 

Summary: bypass watchdog 
Group:   Development/Utilities

%description
%{summary}

%prep
%setup -qn %{name}-%{version}

%build
make

%install
pwd
ls
mkdir -p %{buildroot}/usr/bin
install -D -m 755 bp_watchdog %{buildroot}/usr/bin
install -D -m 644 service/bp_watchdog.service %{buildroot}%{_unitdir}/bp_watchdog.service

%clean
rm -rf %{buildroot}

%pre

%post
systemctl daemon-reload

%preun
%systemd_preun bp_watchdog.service

%postun
%systemd_postun_with_restart bp_watchdog.service

%files
%defattr(755,root,root)
/usr/bin/%{name}
%defattr(644,root,root)
%{_unitdir}/bp_watchdog.service

%changelog
* Wed Apr 23 2022 David Vanhoucke <dvanhoucke@redborder.com>
- first spec version
