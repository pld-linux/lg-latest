Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	116
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-111.tar.gz
# Source0-md5:	6e3e64979922ae30f916c45eb6edc82b
Source1:	http://linuxgazette.net/ftpfiles/lg-112.tar.gz
# Source1-md5:	48026c92297478ae87efe9afbf1bda4c
Source2:	http://linuxgazette.net/ftpfiles/lg-113.tar.gz
# Source2-md5:	4c8915c4e98d2908dad99c5cfe0de2b5
Source3:	http://linuxgazette.net/ftpfiles/lg-114.tar.gz
# Source3-md5:	2c72b685b3663c664ef74ac6d4d81dbb
Source4:	http://linuxgazette.net/ftpfiles/lg-115.tar.gz
# Source4-md5:	4175c4939f0fbc76f506e596afc965b0
Source5:	http://linuxgazette.net/ftpfiles/lg-116.tar.gz
# Source5-md5:	84f273c5b49f8e5079016bbc85a8bf3c
URL:		http://www.linuxgazette.net/
Requires:	lg-base >= %{version}
Conflicts:	lg-issue111to120
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains latest issues of LinuxGazette.

%description -l pl
Ten pakiet zawiera najnowsze wydania LinuxGazette.

%prep
%setup -q -n lg -b1 -b2 -b3 -b4 -b5
mv -f 111 issue111
mv -f 112 issue112
mv -f 113 issue113
mv -f 114 issue114
mv -f 115 issue115
mv -f 116 issue116

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette/issue111
%{_defaultdocdir}/LinuxGazette/issue112
%{_defaultdocdir}/LinuxGazette/issue113
%{_defaultdocdir}/LinuxGazette/issue114
%{_defaultdocdir}/LinuxGazette/issue115
%{_defaultdocdir}/LinuxGazette/issue116
