Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	106
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-101.tar.gz
# Source0-md5:	3c97a73ea6b25f93962c58e9c922d5eb
Source1:	http://linuxgazette.net/ftpfiles/lg-102.tar.gz
# Source1-md5:	1a8ba95afe1d1b927848af954e6336e5
Source2:	http://linuxgazette.net/ftpfiles/lg-103.tar.gz
# Source2-md5:	4d31e314689a639af8276cf9dfa7117d
Source3:	http://linuxgazette.net/ftpfiles/lg-104.tar.gz
# Source3-md5:	b48ba115aab375603fafd53cf308d37c
Source4:	http://linuxgazette.net/ftpfiles/lg-105.tar.gz
# Source4-md5:	2edc2b26e9fc935ff833ad318e26eb10
Source5:	http://linuxgazette.net/ftpfiles/lg-106.tar.gz
# Source5-md5:	90c66a5bc6ae856b6d0cec511d9e68d4
URL:		http://www.linuxgazette.net/
Requires:	lg-base >= %{version}
Conflicts:	lg-issue101to110
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains latest issues of LinuxGazette.

%description -l pl
Ten pakiet zawiera najnowsze wydania LinuxGazette.

%prep
%setup -q -n lg -b1 -b2 -b3 -b4 -b5
mv -f 101 issue101
mv -f 102 issue102
mv -f 103 issue103
mv -f 104 issue104
mv -f 105 issue105
mv -f 106 issue106

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette/issue101
%{_defaultdocdir}/LinuxGazette/issue102
%{_defaultdocdir}/LinuxGazette/issue103
%{_defaultdocdir}/LinuxGazette/issue104
%{_defaultdocdir}/LinuxGazette/issue105
%{_defaultdocdir}/LinuxGazette/issue106
