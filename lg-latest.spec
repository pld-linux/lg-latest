Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	93
Release:	1
License:	distributable
Group:		Documentation
Source0:	ftp://ftp.ssc.com/pub/lg/lg-issue91.tar.gz
# Source0-md5:	07c40ae01af90ba1760675ba1d4bbc5a
Source1:	ftp://ftp.ssc.com/pub/lg/lg-issue92.tar.gz
# Source1-md5:	59928e73c7506f5dafedc24881fc7d95
Source2:	ftp://ftp.ssc.com/pub/lg/lg-issue93.tar.gz
# Source2-md5:	3c3148e6e2bccf8e8aefe425a4d6c3a6
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
%setup -q -n lg -b1 -b2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette/issue91
%{_defaultdocdir}/LinuxGazette/issue92
%{_defaultdocdir}/LinuxGazette/issue93
