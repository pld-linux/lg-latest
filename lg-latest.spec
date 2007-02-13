Summary:	LinuxGazette - latest issues
Summary(pl.UTF-8):	LinuxGazette - najnowsze wydania
Name:		lg-latest
Version:	134
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://linuxgazette.net/ftpfiles/lg-131.tar.gz
# Source0-md5:	3037540ededf9d801049ecd7b198c3d5
Source1:	http://linuxgazette.net/ftpfiles/lg-132.tar.gz
# Source1-md5:	f7b01866cb36430f8c95cff29449b6f9
Source2:	http://linuxgazette.net/ftpfiles/lg-133.tar.gz
# Source2-md5:	8448ae9f1cbacef991c99f38c5bcc893
Source3:	http://linuxgazette.net/ftpfiles/lg-134.tar.gz
# Source3-md5:	f0bd337f0840cb2bcada7c2e2b0bdbde
URL:		http://www.linuxgazette.net/
Requires:	lg-base >= %{version}
Conflicts:	lg-issue131to140
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
