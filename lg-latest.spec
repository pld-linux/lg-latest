# TODO: unpack all in single %setup, w/o '/' in -n (let --clean work)
Summary:	LinuxGazette - latest issues
Summary(pl):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	90
Release:	1
License:	distributable
Group:		Documentation
# Source0-md5:	4a130b8eb86a67fa0d60066c823f8d5a
Source0:	ftp://ftp.ssc.com/pub/lg/lg-issue81.tar.gz
# Source1-md5:	a57396276627e954fe11f133820fdb0d
Source1:	ftp://ftp.ssc.com/pub/lg/lg-issue82.tar.gz
# Source2-md5:	f292624445780daf961c4098f3ce2471
Source2:	ftp://ftp.ssc.com/pub/lg/lg-issue83.tar.gz
# Source3-md5:	fc8dcab6bf809b6b263dc2d05f19ae88
Source3:	ftp://ftp.ssc.com/pub/lg/lg-issue84.tar.gz
# Source4-md5:	e129c7f389e7823613ba223e7a281dd8
Source4:	ftp://ftp.ssc.com/pub/lg/lg-issue85.tar.gz
# Source5-md5:	550717e0af6df020d4caf1d456f5d617
Source5:	ftp://ftp.ssc.com/pub/lg/lg-issue86.tar.gz
# Source6-md5:	6fd5b1506ff38b5aa9286d16ccdb1902
Source6:	ftp://ftp.ssc.com/pub/lg/lg-issue87.tar.gz
# Source7-md5:	8f10ec1d47d1679bbe3491d5c74a064c
Source7:	ftp://ftp.ssc.com/pub/lg/lg-issue88.tar.gz
# Source8-md5:	187f1b1363063ad27be5e82b0503005d
Source8:	ftp://ftp.ssc.com/pub/lg/lg-issue89.tar.gz
# Source9-md5:	94f791e15b689c1ca32854abd8031ce6
Source9:	ftp://ftp.ssc.com/pub/lg/lg-issue90.tar.gz
URL:		http://www.linuxgazette.com/
Requires:	lg-base >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains latest issues of LinuxGazette.

%description -l pl
Ten pakiet zawiera najnowsze wydania LinuxGazette.

%prep
%setup -q -n lg -b1 -b2 -b3 -b4 -b5 -b6 -b7 -b8 -b9

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette
cp -ar * $RPM_BUILD_ROOT%{_defaultdocdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%{_defaultdocdir}/LinuxGazette/issue81
%{_defaultdocdir}/LinuxGazette/issue82
%{_defaultdocdir}/LinuxGazette/issue83
%{_defaultdocdir}/LinuxGazette/issue84
%{_defaultdocdir}/LinuxGazette/issue85
%{_defaultdocdir}/LinuxGazette/issue86
%{_defaultdocdir}/LinuxGazette/issue87
%{_defaultdocdir}/LinuxGazette/issue88
%{_defaultdocdir}/LinuxGazette/issue89
%{_defaultdocdir}/LinuxGazette/issue90
