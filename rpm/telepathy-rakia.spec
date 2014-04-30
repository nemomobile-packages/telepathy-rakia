# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       telepathy-rakia

# >> macros
# << macros

Summary:    SIP connection manager for Telepathy
Version:    0.7.4
Release:    1
Group:      Applications/Communications
License:    LGPLv2+
URL:        http://telepathy.freedesktop.org/wiki/Components
Source0:    http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:    runTest.sh
Source2:    mktests.sh
Source100:  telepathy-rakia.yaml
Patch0:     0001-Check-for-gio-to-avoid-linking-issue.patch
Patch1:     0002-nemo-test-install.patch
Patch2:     0003-switch-to-using-gireactor-to-work-with-new-gi-based-.patch
BuildRequires:  pkgconfig(gobject-2.0) >= 2.30
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(telepathy-glib) >= 0.17.7
BuildRequires:  pkgconfig(sofia-sip-ua-glib) >= 1.12.11
BuildRequires:  libxslt
BuildRequires:  python >= 2.3
BuildRequires:  python-twisted
Provides:   telepathy-sofiasip = %{version}-%{release}
Obsoletes:   telepathy-sofiasip < 0.7.2

%description
%{name} is a SIP connection manager for the Telepathy
framework based on the SofiaSIP-stack.


%package tests
Summary:    Tests package for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   python-twisted
Requires:   dbus-python
Requires:   pygobject2

%description tests
The %{name}-tests package contains tests and
tests.xml for automated testing.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Library, headers, and other files for developing applications
that use Telepathy-Rakia.


%prep
%setup -q -n %{name}-%{version}/%{name}

# 0001-Check-for-gio-to-avoid-linking-issue.patch
%patch0 -p1
# 0002-nemo-test-install.patch
%patch1 -p1
# 0003-switch-to-using-gireactor-to-work-with-new-gi-based-.patch
%patch2 -p1
# >> setup
%__cp $RPM_SOURCE_DIR/mktests.sh tests/
%__chmod 0755 tests/mktests.sh
# << setup

%build
# >> build pre
%autogen --no-configure
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
tests/mktests.sh > tests/tests.xml
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
install -m 0755 $RPM_SOURCE_DIR/runTest.sh $RPM_BUILD_ROOT/opt/tests/%{name}/bin/runTest.sh
install -m 0644 tests/tests.xml $RPM_BUILD_ROOT/opt/tests/%{name}/tests.xml
# << install post

%files
%defattr(-,root,root,-)
# >> files
%doc COPYING README NEWS TODO
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_datadir}/telepathy/managers/*.manager
%{_mandir}/man8/%{name}.8.gz
# << files

%files tests
%defattr(-,root,root,-)
/opt/tests/%{name}/*
# >> files tests
# << files tests

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}-0.7
# >> files devel
# << files devel
