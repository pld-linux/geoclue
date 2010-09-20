# git clone --depth 1 git://anongit.freedesktop.org/geoclue
# cd geoclue
# git archive master --prefix geoclue/ | bzip2 > geoclue-$(date +%Y%m%d).tar.bz2

Summary:	A modular geoinformation service
Name:		geoclue
Version:	0.12.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://folks.o-hand.com/jku/geoclue-releases/%{name}-%{version}.tar.gz
# Source0-md5:	33af8307f332e0065af056ecba65fec2
Patch0:		%{name}-configure.patch
URL:		http://geoclue.freedesktop.org/
BuildRequires:	GConf2-devel
BuildRequires:	NetworkManager-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	dbus-glib-devel
BuildRequires:	docbook-dtd412-xml
BuildRequires:	glib2-devel
BuildRequires:	gpsd-devel >= 2.91
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRequires:	gypsy-devel
BuildRequires:	libsoup-gnome-devel >= 2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Geoclue is a modular geoinformation service built on top of the D-Bus
messaging system. The goal of the Geoclue project is to make creating
location-aware applications as simple as possible.

%package devel
Summary:	Development package for geoclue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib-devel
Requires:	libxml2-devel

%description devel
Files for development with geoclue.

%package apidocs
Summary:	Developer documentation for geoclue
Group:		Development/Libraries
Requires:	gtk-doc-common

%description apidocs
Developer documentation for geoclue

%package gpsd
Summary:	gpsd provider for geoclue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gpsd >= 2.91

%description gpsd
A gpsd provider for geoclue

%package gypsy
Summary:	gypsy provider for geoclue
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gypsy

%description gypsy
A gypsy provider for geoclue

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-static \
	--enable-gtk-doc \
	--enable-conic=no \
	--enable-gpsd=yes \
	--enable-gypsy=yes \
	--enable-networkmanager=yes \
	--enable-skyhook=yes \
	--with-html-dir=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%dir %{_datadir}/geoclue-providers
%attr(755,root,root) %{_libdir}/libgeoclue.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgeoclue.so.0
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

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgeoclue.so
%{_libdir}/libgeoclue.la
%{_includedir}/geoclue
%{_pkgconfigdir}/geoclue.pc

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
