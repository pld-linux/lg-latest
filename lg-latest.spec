Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	98
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-issue91.tar.gz
# Source0-md5:	eb48d37b0eea8025700ce4485ace9c5f
Source1:	http://linuxgazette.net/ftpfiles/lg-issue92.tar.gz
# Source1-md5:	12091a6b97a7d9e7569b0535e60144f0
Source2:	http://linuxgazette.net/ftpfiles/lg-issue93.tar.gz
# Source2-md5:	e9abe936f337ee2c29a85f15a49d08c0
Source3:	http://linuxgazette.net/ftpfiles/lg-issue94.tar.gz
# Source3-md5:	9028a11669ef00c51428c2f4ab377a84
Source4:	http://linuxgazette.net/ftpfiles/lg-issue95.tar.gz
# Source4-md5:	c8fa731af1bea28c725d118c59ab48f4
Source5:	http://linuxgazette.net/ftpfiles/lg-issue96.tar.gz
# Source5-md5:	f6aa71b8c8144a5e479cdc820e9a45b6
Source6:	http://linuxgazette.net/ftpfiles/lg-issue97.tar.gz
# Source6-md5:	28149e41d42d84e9eaf3064129f704e6
Source7:	http://linuxgazette.net/ftpfiles/lg-issue98.tar.gz
# Source7-md5:	121997742ab65e19f6e547a87e7dd40c
URL:		http://www.linuxgazette.net/
Requires:	lg-base >= %{version}
Conflicts:	lg-issue91to100
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains latest issues of LinuxGazette.

%description -l pl
Ten pakiet zawiera najnowsze wydania LinuxGazette.

%prep
%setup -q -n lg -b1 -b2 -b3 -b4 -b5 -b6 -b7

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
%{_defaultdocdir}/LinuxGazette/issue96
%{_defaultdocdir}/LinuxGazette/issue97
%{_defaultdocdir}/LinuxGazette/issue98
