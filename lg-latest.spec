Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	91
Release:	1
License:	distributable
Group:		Documentation
# Source0-md5:	07c40ae01af90ba1760675ba1d4bbc5a
Source0:	ftp://ftp.ssc.com/pub/lg/lg-issue91.tar.gz
URL:		http://www.linuxgazette.com/
Requires:	lg-base >= %{version}
Conflicts:	lg-issue91to100
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains latest issues of LinuxGazette.

%description -l pl
Ten pakiet zawiera najnowsze wydania LinuxGazette.

%prep
%setup -q -n lg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette/issue91
