Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	95
Release:	1
License:	distributable
Group:		Documentation
Source0:	ftp://ftp.ssc.com/pub/lg/lg-issue91.tar.gz
# Source0-md5:	07c40ae01af90ba1760675ba1d4bbc5a
Source1:	ftp://ftp.ssc.com/pub/lg/lg-issue92.tar.gz
# Source1-md5:	59928e73c7506f5dafedc24881fc7d95
Source2:	ftp://ftp.ssc.com/pub/lg/lg-issue93.tar.gz
# Source2-md5:	3c3148e6e2bccf8e8aefe425a4d6c3a6
Source3:	ftp://ftp.ssc.com/pub/lg/lg-issue94.tar.gz
# Source3-md5:	0dcf298194707abe341fd8fff001a2dd
Source4:	ftp://ftp.ssc.com/pub/lg/lg-issue95.tar.gz
# Source4-md5:	27595659d046b1d88fd933995cfc8111
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
%setup -q -n lg -b1 -b2 -b3 -b4

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
%{_defaultdocdir}/LinuxGazette/issue94
%{_defaultdocdir}/LinuxGazette/issue95
