Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	99
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-issue91.tar.gz
# Source0-md5:	a652b799eaf3f6daa71d59b27cdf7817
Source1:	http://linuxgazette.net/ftpfiles/lg-issue92.tar.gz
# Source1-md5:	ee503aa00810ffaf91c4844598933bf8
Source2:	http://linuxgazette.net/ftpfiles/lg-issue93.tar.gz
# Source2-md5:	ebdf12c1ebeb3ffdb62c904fb4126f63
Source3:	http://linuxgazette.net/ftpfiles/lg-issue94.tar.gz
# Source3-md5:	221526fd6c62808220696eabe1abe504
Source4:	http://linuxgazette.net/ftpfiles/lg-issue95.tar.gz
# Source4-md5:	55049792d023af7b5599878653cb05e4
Source5:	http://linuxgazette.net/ftpfiles/lg-issue96.tar.gz
# Source5-md5:	3f61f13295a8cbbd2cdeb3f2f7416701
Source6:	http://linuxgazette.net/ftpfiles/lg-issue97.tar.gz
# Source6-md5:	879ea894af7e5ab9927cde993986c95b
Source7:	http://linuxgazette.net/ftpfiles/lg-issue98.tar.gz
# Source7-md5:	121997742ab65e19f6e547a87e7dd40c
Source8:	http://linuxgazette.net/ftpfiles/lg-issue99.tar.gz
# Source8-md5:	69bea98df9895ef34b5ef2590b46fe61
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
%setup -q -n lg -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8

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
%{_defaultdocdir}/LinuxGazette/issue99
