Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	112
Release:	2
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-111.tar.gz
# Source0-md5:	6e3e64979922ae30f916c45eb6edc82b
Source1:	http://linuxgazette.net/ftpfiles/lg-112.tar.gz
# Source1-md5:	48026c92297478ae87efe9afbf1bda4c
Source10:	http://linuxgazette.net/ftpfiles/lg-%{version}.tar.gz
# Source10-md5:	6e3e64979922ae30f916c45eb6edc82b
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
%setup -q -n lg -b1
mv -f 111 issue111
mv -f 112 issue112

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
