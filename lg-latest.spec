Summary:	LinuxGazette - latest issues
Summary(pl.UTF-8):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	154
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-151.tar.gz
# Source0-md5:	323a599056403da8d01a271067100036
Source1:	http://linuxgazette.net/ftpfiles/lg-152.tar.gz
# Source1-md5:	9f0fb42dcb73771c962a3db1261b4390
Source2:	http://linuxgazette.net/ftpfiles/lg-153.tar.gz
# Source2-md5:	7f6f3bb001e37b5ddd7112bf17b32185
Source3:	http://linuxgazette.net/ftpfiles/lg-154.tar.gz
# Source3-md5:	64d363501a9b60bcc9d4980e770d0651
URL:		http://www.linuxgazette.net/
Requires:	lg-base >= %{version}
Conflicts:	lg-issue151to160
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains latest issues of LinuxGazette.

%description -l pl.UTF-8
Ten pakiet zawiera najnowsze wydania LinuxGazette.

%prep
%setup -q -n lg -b1 -b2 -b3
for i in 1*; do mv $i issue$i; done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LinuxGazette
cp -a * $RPM_BUILD_ROOT%{_docdir}/LinuxGazette

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LinuxGazette/*
