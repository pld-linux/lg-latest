Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	122
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-121.tar.gz
# Source0-md5:	acc32256b8a058cdca2abb97271a41ba
Source1:	http://linuxgazette.net/ftpfiles/lg-122.tar.gz
# Source1-md5:	dee1fdc50ba11c0c905d1e413a1f219d
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
%setup -q -n lg -b1
mv -f 121 issue121
mv -f 122 issue122

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
