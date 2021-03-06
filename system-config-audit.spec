%define _disable_rebuild_configure 1
%define _disable_lto 1

Summary:	Audit GUI configuration tool
Name:		system-config-audit
Version:	0.4.21
Release:	3
License:	GPLv2
Group:		System/Base
URL:		https://fedorahosted.org/system-config-audit/
Source0:	https://fedorahosted.org/releases/s/y/system-config-audit/system-config-audit-%{version}.tar.xz
Patch0:		audit-1.6.1-desktopfile.patch
Patch1:		audit-1.6.1-sendmail.patch
Requires:	audit >= 2.0
Requires:	pygtk2.0-libglade
Requires:	python-audit >= 2.0
Requires:	usermode-consoleonly >= 1.92-4
BuildRequires:	audit-devel >= 2.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	python-devel
Obsoletes:	libaudit-common < 1.6.1
Conflicts:	audit < 1.6.1
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This package contains a GUI for configuring the Audit system.

%prep

%setup -q
%patch0 -p0
%patch1 -p0

%build
%configure2_5x \
    --libexecdir=%{_sbindir}
%make

%install
rm -rf %{buildroot}

%makeinstall_std install-fedora

desktop-file-validate %{buildroot}%{_datadir}/applications/system-config-audit.desktop

%find_lang system-config-audit

# let's use our own pam config
rm -f %{buildroot}%{_sysconfdir}/pam.d/system-config-audit-server
ln -s %{_sysconfdir}/pam.d/mandriva-simple-auth \
        %{buildroot}%{_sysconfdir}/pam.d/system-config-audit-server

%clean
rm -rf %{buildroot}

%files -f system-config-audit.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%config(noreplace) %{_sysconfdir}/pam.d/system-config-audit-server
%config(noreplace) %{_sysconfdir}/security/console.apps/system-config-audit-server
%{_bindir}/system-config-audit
%{_datadir}/applications/system-config-audit.desktop
%{_datadir}/system-config-audit
%{_sbindir}/system-config-audit-server-real
%{_sbindir}/system-config-audit-server



%changelog
* Sat Jun 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.4.18-1mdv2011.0
+ Revision: 685946
- 0.4.18

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.4.17-2
+ Revision: 670257
- mass rebuild

* Sun Oct 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.4.17-1mdv2011.0
+ Revision: 584649
- 0.4.17

* Mon Aug 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.4.15-1mdv2011.0
+ Revision: 568096
- 0.4.15

* Sat Mar 27 2010 Oden Eriksson <oeriksson@mandriva.com> 1:0.4.14-1mdv2010.1
+ Revision: 527908
- bump epoch

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.4.14-1mdv2010.1
+ Revision: 521167
- import system-config-audit


* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0:0.4.14-1mdv2010.1
- initial Mandriva package (split out from the main audit package)
