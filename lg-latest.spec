Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	128
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-121.tar.gz
# Source0-md5:	acc32256b8a058cdca2abb97271a41ba
Source1:	http://linuxgazette.net/ftpfiles/lg-122.tar.gz
# Source1-md5:	dee1fdc50ba11c0c905d1e413a1f219d
Source2:	http://linuxgazette.net/ftpfiles/lg-123.tar.gz
# Source2-md5:	403922cd1be12e8bb500f33fbeb1101f
Source3:	http://linuxgazette.net/ftpfiles/lg-124.tar.gz
# Source3-md5:	caf1419357d284c9dc0a6abcae9c613c
Source4:	http://linuxgazette.net/ftpfiles/lg-125.tar.gz
# Source4-md5:	2e753f52d40669dee2f644f15b30daa9
Source5:	http://linuxgazette.net/ftpfiles/lg-126.tar.gz
# Source5-md5:	5a68de434a1ce9b57e7dc4319e9871e5
Source6:	http://linuxgazette.net/ftpfiles/lg-127.tar.gz
# Source6-md5:	1894d6a2ce7972daced5a2a1cd18856d
Source7:	http://linuxgazette.net/ftpfiles/lg-128.tar.gz
# Source7-md5:	9d85997cc3280974ce9ec6452a607f4b
URL:		http://www.linuxgazette.net/
Requires:	lg-base >= %{version}
Conflicts:	lg-issue121to130
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains latest issues of LinuxGazette.

%description -l pl
Ten pakiet zawiera najnowsze wydania LinuxGazette.

%prep
%setup -q -n lg -b1 -b2 -b3 -b4 -b5 -b6 -b7
mv -f 121 issue121
mv -f 122 issue122
mv -f 123 issue123
mv -f 124 issue124
mv -f 125 issue125
mv -f 126 issue126
mv -f 127 issue127
mv -f 128 issue128

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette/issue121
%{_defaultdocdir}/LinuxGazette/issue122
%{_defaultdocdir}/LinuxGazette/issue123
%{_defaultdocdir}/LinuxGazette/issue124
%{_defaultdocdir}/LinuxGazette/issue125
%{_defaultdocdir}/LinuxGazette/issue126
%{_defaultdocdir}/LinuxGazette/issue127
%{_defaultdocdir}/LinuxGazette/issue128
