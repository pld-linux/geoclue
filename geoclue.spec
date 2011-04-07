Summary:	A modular geoinformation service
Summary(pl.UTF-8):	Modularna usługa geoinformacyjna
Name:		geoclue
Version:	0.12.0
Release:	5
License:	LGPL v2
Group:		Applications
Source0:	http://folks.o-hand.com/jku/geoclue-releases/%{name}-%{version}.tar.gz
# Source0-md5:	33af8307f332e0065af056ecba65fec2
Patch0:		%{name}-configure.patch
Patch1:		%{name}-libsoup.patch
Patch2:		%{name}-nm09.patch
URL:		http://geoclue.freedesktop.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	dbus-glib-devel >= 0.60
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel >= 1:2.0
BuildRequires:	gpsd-devel >= 2.91
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	gypsy-devel
BuildRequires:	libsoup-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	libxslt-progs
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geoclue is a modular geoinformation service built on top of the D-Bus
messaging system. The goal of the Geoclue project is to make creating
location-aware applications as simple as possible.

%description -l pl.UTF-8
Geoclue to modularna usługa geoinformacyjna zbudowana w oparciu o
system komunikacji D-Bus. Celem projektu jest jak największe
ułatwienie tworzenia aplikacji uwzględniających lokalizację.

%package libs
Summary:	Geoclue modular geoinformation service library
Summary(pl.UTF-8):	Biblioteka geoclue - modularnej usługi geoinformacyjnej
Group:		Libraries
Requires:	dbus-glib >= 0.60
Conflicts:	geoclue < 0.12.0-3

%description libs
geoclue modular geoinformation service library.

%description libs -l pl.UTF-8
Biblioteka geoclue - modularnej usługi geoinformacyjnej.

%package devel
Summary:	Development package for geoclue
Summary(pl.UTF-8):	Pakiet programistyczny geoclue
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	dbus-glib-devel >= 0.60
Requires:	libxml2-devel >= 2.0

%description devel
Header files for development with geoclue.

%description devel -l pl.UTF-8
Pliki nagłówkowe do programowania z użyciem geoclue.

%package static
Summary:	Static geoclue library
Summary(pl.UTF-8):	Statyczna biblioteka geoclue
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static geoclue library.

%description static -l pl.UTF-8
Statyczna biblioteka geoclue.

%package apidocs
Summary:	Developer documentation for geoclue
Summary(pl.UTF-8):	Dokumentacja programisty do geoclue
Group:		Development/Libraries
Requires:	gtk-doc-common

%description apidocs
Developer documentation for geoclue.

%description apidocs -l pl.UTF-8
Dokumentacja programisty do geoclue.

%package gpsd
Summary:	gpsd provider for geoclue
Summary(pl.UTF-8):	Interfejs geoclue do gpsd
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gpsd >= 2.91

%description gpsd
A gpsd provider for geoclue.

%description gpsd -l pl.UTF-8
Interfejs geoclue do gpsd.

%package gypsy
Summary:	gypsy provider for geoclue
Summary(pl.UTF-8):	Interfejs geoclue do gypsy
Group:		Applications
Requires:	%{name} = %{version}-%{release}
Requires:	gypsy

%description gypsy
A gypsy provider for geoclue.

%description gypsy -l pl.UTF-8
Interfejs geoclue do gypsy.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gtk-doc \
	--disable-conic \
	--enable-gpsd \
	--enable-gypsy \
	--enable-networkmanager \
	--enable-skyhook \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libexecdir}/geoclue-example
%attr(755,root,root) %{_libexecdir}/geoclue-geonames
%attr(755,root,root) %{_libexecdir}/geoclue-gsmloc
%attr(755,root,root) %{_libexecdir}/geoclue-hostip
%attr(755,root,root) %{_libexecdir}/geoclue-localnet
%attr(755,root,root) %{_libexecdir}/geoclue-manual
%attr(755,root,root) %{_libexecdir}/geoclue-master
%attr(755,root,root) %{_libexecdir}/geoclue-nominatim
%attr(755,root,root) %{_libexecdir}/geoclue-plazes
%attr(755,root,root) %{_libexecdir}/geoclue-skyhook
%attr(755,root,root) %{_libexecdir}/geoclue-yahoo
%dir %{_datadir}/geoclue-providers
%{_datadir}/geoclue-providers/geoclue-example.provider
%{_datadir}/geoclue-providers/geoclue-geonames.provider
%{_datadir}/geoclue-providers/geoclue-gsmloc.provider
%{_datadir}/geoclue-providers/geoclue-hostip.provider
%{_datadir}/geoclue-providers/geoclue-localnet.provider
%{_datadir}/geoclue-providers/geoclue-manual.provider
%{_datadir}/geoclue-providers/geoclue-nominatim.provider
%{_datadir}/geoclue-providers/geoclue-plazes.provider
%{_datadir}/geoclue-providers/geoclue-skyhook.provider
%{_datadir}/geoclue-providers/geoclue-yahoo.provider
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Master.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Example.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Geonames.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Gsmloc.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Hostip.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Localnet.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Manual.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Nominatim.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Plazes.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Skyhook.service
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Yahoo.service

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgeoclue.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgeoclue.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgeoclue.so
%{_includedir}/geoclue
%{_pkgconfigdir}/geoclue.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgeoclue.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/geoclue

%files gpsd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/geoclue-gpsd
%{_datadir}/geoclue-providers/geoclue-gpsd.provider
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Gpsd.service

%files gypsy
%defattr(644,root,root,755)
%attr(755,root,root) %{_libexecdir}/geoclue-gypsy
%{_datadir}/geoclue-providers/geoclue-gypsy.provider
%{_datadir}/dbus-1/services/org.freedesktop.Geoclue.Providers.Gypsy.service
